from core.querysets import ItemRepository
import logging as log
from api.webservice import WebService
from .load_data import FileReader
from . import constants


def process_data():
    try:
        file_reader = FileReader()
        webservice = WebService()
        list_of_ids = []
        list_of_documents = []
        list_of_failed = []
        index = 0
        # Iterate over batches of data and process them
        for batch in file_reader.read_file():
            # Process each batch of data
            for row in batch:
                site_id = f"{row['site']}{str(row['id'])}"
                list_of_ids.append(site_id)
                if (len(list_of_ids) == int(constants.MULTIGET_SIZE) or
                   len(batch) < int(constants.BATCH_SIZE) or
                   index == len(batch) - 1):
                    index += 1
                    # Get items from mercadolibre's api through a multiget
                    items_obtained = webservice.get_data_from_items(list_of_ids)
                    if items_obtained is None:
                        list_of_failed.extend(list_of_ids)
                        list_of_ids = []
                        continue
                    for item in items_obtained:
                        document_to_save = {}
                        document_to_save['site'] = row['site']
                        document_to_save['file_id'] = str(row['id'])
                        document_to_save['price'] = int(item['body']['price'])
                        document_to_save['start_time'] = item['body']['start_time']

                        field_name = webservice.get_data_from_categories(item['body']['category_id'])
                        description = webservice.get_data_from_currencies(item['body']['currency_id'])
                        nickname = webservice.get_data_from_users(item['body']['seller_id'])

                        document_to_save['name'] = field_name
                        document_to_save['description'] = description
                        document_to_save['nickname'] = nickname

                        # Could be used for inserting several documents at once
                        list_of_documents.append(document_to_save)

                        ItemRepository.insert_one_item(document_to_save)
                    list_of_ids = []

        return {
                "message": "Successfully executed",
                "http_code": 200
            }
    except Exception as e:
        log.error(f"An error has been found inside process_data, Error: {e}")
        return {
                "message": "Internal Server Error",
                "http_code": 500
            }
