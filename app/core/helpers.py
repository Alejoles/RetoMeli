import os
import json
from . import constants


class GeneralHelpers:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archivo_cache = constants.CACHE_FILE_NAME
            cls._instance.lista_ids = cls._instance.cargar_ids()
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'lista_ids'):
            self.lista_ids = self.cargar_ids()

    @staticmethod
    def list_to_jsonl(dictionary_list: list, file_path: str):
        """
            Converts a list of dictionaries to a JSONL file.

            Arguments:
            - dictionary_list: A list of dictionaries to write to the JSONL file.
        """
        if not os.path.exists(file_path):
            with open(file_path, 'w') as archivo:
                # Crear archivo JSONLines vacío
                pass
        with open(file_path, 'a') as archivo:
            for diccionario in dictionary_list:
                json.dump(diccionario, archivo)
                archivo.write('\n')

    def cargar_ids(self):
        lista_ids = []
        for lote in self.leer_jsonl_lote():
            for obj in lote:
                id_obj = obj.get('id')
                if id_obj:
                    lista_ids.append(id_obj)
        return lista_ids

    def leer_jsonl_lote(self):
        if not os.path.exists(self.archivo_cache):
            with open(self.archivo_cache, 'w') as f:
                # Crear archivo JSONLines vacío
                pass
        with open(self.archivo_cache, 'r') as f:
            lote = []
            for idx, linea in enumerate(f):
                lote.append(json.loads(linea))
                if (idx + 1) % int(constants.BATCH_SIZE) == 0:
                    yield lote
                    lote = []
            if lote:
                yield lote

    def revisar_cache(self, nuevo_id):
        print("Checking cache")
        return nuevo_id in self.lista_ids

    def buscar_por_id(self, id_buscado):
        with open(self.archivo_cache, 'r') as f:
            for linea in f:
                objeto = json.loads(linea)
                id_objeto = objeto.get('id')
                if id_objeto == id_buscado:
                    return objeto
        return None

    def guardar_diccionario(self, diccionario):
        with open(self.archivo_cache, 'a') as archivo:
            json.dump(diccionario, archivo)
            archivo.write('\n')
