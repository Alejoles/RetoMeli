from core.querysets import ItemRepository
import logging as log
from api.webservice import WebService
from .load_data import FileReader
import threading
from .helpers import GeneralHelpers


def process_row(row, list_of_failed, semaphore, items_processed):
    """
        Processes a row of data.

        This function processes a row of data, obtaining information from Mercadolibre's API
        based on the 'site' and 'id' fields of the row. It constructs a document to be saved
        in the database, including information such as site, file ID, price, name, description,
        and nickname. The document is then inserted into the database.

        Parameters:
        - row (dict): A dictionary containing data for processing, including 'site' and 'id'.
        - list_of_failed (list): A list to store any failed data retrieval attempts.
        - semaphore (Semaphore): A semaphore to control threads.

        Return: None
    """
    site_id = f"{row['site']}{str(row['id'])}"

    # Obtain data from mercadolibre's API
    item_obtained = WebService().get_data_from_items(site_id, items_processed)

    if 'error' in item_obtained:
        list_of_failed.append(item_obtained)
        GeneralHelpers().guardar_diccionario({'id': site_id, 'status': 'Error',
                                              'error': item_obtained["error"]})
        semaphore.release()  # Release semaphore in case of error
        return

    document_to_save = {
        'site': row['site'],
        'file_id': str(row['id']),
        'price': int(item_obtained['price'])
    }
    # Obtain data from mercadolibre's API
    field_name = WebService().get_data_from_categories(item_obtained['category_id'])
    if 'error' in field_name:
        list_of_failed.append(field_name)
        GeneralHelpers().guardar_diccionario({'id': site_id, 'status': 'Error',
                                              'error': field_name["error"]})
        semaphore.release()  # Release semaphore in case of error
        return

    description = WebService().get_data_from_currencies(item_obtained['currency_id'])
    if 'error' in description:
        list_of_failed.append(description)
        GeneralHelpers().guardar_diccionario({'id': site_id, 'status': 'Error',
                                              'error': description["error"]})
        semaphore.release()  # Release semaphore in case of error
        return

    nickname = WebService().get_data_from_users(item_obtained['seller_id'])
    if 'error' in nickname:
        list_of_failed.append(nickname)
        GeneralHelpers().guardar_diccionario({'id': site_id, 'status': 'Error',
                                              'error': nickname["error"]})
        semaphore.release()  # Release semaphore in case of error
        return

    document_to_save['name'] = field_name
    document_to_save['description'] = description
    document_to_save['nickname'] = nickname

    # Insert document inside database
    ItemRepository.insert_one_item(document_to_save)
    GeneralHelpers().guardar_diccionario({'id': site_id, 'status': 'Ok'})
    semaphore.release()  # Release semaphore after completing the insert


def process_data_with_threads(num_threads):
    """
        Processes data using multiple threads.

        This function reads data from a file in batches using FileReader and processes
        each batch of data concurrently using multiple threads. Each thread acquires a
        semaphore before starting its execution to limit the number of concurrent threads.
        The function waits for all threads to finish their execution before returning.

        Parameters:
        - num_threads (int): The maximum number of threads to be used for processing.

        Returns:
        dict: A dictionary containing the result of the operation, including a message
        indicating the success or failure of the operation and an HTTP status code.
    """
    try:
        file_reader = FileReader()
        list_of_failed = []
        threads = []
        semaphore = threading.Semaphore(num_threads)
        items_processed = [0]
        helpers = GeneralHelpers()

        # Iterating over batches of data and processing them
        for batch in file_reader.read_file():
            # Process each batch of data in one thread
            for row in batch:
                site_id = f"{row['site']}{str(row['id'])}"

                # --------------- Checking if id exists in cache ---------------
                # exists_in_cache = helpers.revisar_cache(site_id) # Ocupaba más memoria
                exists_in_cache = helpers.buscar_por_id(site_id)
                if exists_in_cache:
                    continue

                semaphore.acquire()  # Acquiring the semaphore before starting a thread
                thread = threading.Thread(target=process_row, args=(row, list_of_failed,
                                                                    semaphore, items_processed))
                thread.start()
                threads.append(thread)

        helpers.list_to_jsonl(list_of_failed, "/files/data_failed_test.jsonl")
        list_of_failed = []

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        print(f"!!!!!!!!!! {items_processed}")

        return {
            "message": "Successfully Executed",
            "http_code": 200
        }
    except Exception as e:
        log.error(f"An error has been found inside process_data, Error: {e}")
        return {
                "message": f"Internal Server Error, datails: {e}",
                "http_code": 500
            }


def get_item_from_db(id: str):
    site = id[:3]
    file_id = id[3:]
    element = ItemRepository.find_one_active(site=site, file_id=file_id)
    if element:
        return {
                "message": element.to_json(),
                "http_code": 200
            }
    return {
                "message": "No element found with id given",
                "http_code": 404
            }
