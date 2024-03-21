import json


class GeneralHelpers:

    @staticmethod
    def list_to_jsonl(dictionary_list: list,):
        """
            Converts a list of dictionaries to a JSONL file.

            Arguments:
            - dictionary_list: A list of dictionaries to write to the JSONL file.
        """
        with open("/files/cache/data_cache.jsonl", 'a') as archivo:
            for diccionario in dictionary_list:
                json.dump(diccionario, archivo)
                archivo.write('\n')
