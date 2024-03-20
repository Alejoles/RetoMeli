import csv
import json
import yaml
import pandas as pd
import logging as log
from . import constants


class FileReader:
    def __init__(self, has_header=True, skip_lines=0):
        self.filename = constants.FILE_NAME
        self.format_type = str(constants.FILE_NAME).split(".")[-1]
        self.delimiter = constants.SEPARATOR
        self.encoding = constants.ENCODING
        self.has_header = has_header
        self.skip_lines = skip_lines
        self.batch_size = int(constants.BATCH_SIZE)

    def read_file(self):
        with open(self.filename, 'r', encoding=self.encoding) as file:
            if self.format_type == 'csv':
                yield from self.read_csv(file)
            elif self.format_type == 'jsonl':
                yield from self.read_jsonlines(file)
            elif self.format_type == 'txt':
                yield from self.read_text(file)
            elif self.format_type == 'json':
                yield from self.read_json(file)
            elif self.format_type == 'xlsx' or self.format_type == 'xls':
                yield from self.read_excel()
            elif self.format_type == 'yaml':
                yield from self.read_yaml(file)
            else:
                raise ValueError('Format not supported.')

    def read_csv(self, file):
        try:
            reader = csv.DictReader(file, delimiter=self.delimiter)
            if self.has_header:
                next(reader)  # Skip header
            for _ in range(self.skip_lines):
                next(reader)  # Skip lines
            batch = []
            for row in reader:
                batch.append(row)
                if len(batch) >= self.batch_size:
                    yield batch
                    batch = []
            if batch:
                yield batch
        except Exception as e:
            log.error(f"Error loading CSV: {e}")

    def read_jsonlines(self, file):
        batch = []
        for line in file:
            batch.append(json.loads(line.strip()))
            if len(batch) >= self.batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

    def read_text(self, file):
        try:
            batch = []
            for line_number, line in enumerate(file, start=1):
                if line_number > self.skip_lines:
                    parts = line.strip().split(self.delimiter)
                    if len(parts) == 2:
                        data = {'site': parts[0], 'id': parts[1]}
                        batch.append(data)
                        if len(batch) >= self.batch_size:
                            yield batch
                            batch = []
            if batch:
                yield batch
        except Exception as e:
            log.error(f"Error loading TXT: {e}")

    def read_json(self, file):
        try:
            data = json.load(file)
            batch = []
            for item in data:
                if isinstance(item, dict) and 'site' in item and 'id' in item:
                    batch.append(item)
                    if len(batch) >= self.batch_size:
                        yield batch
                        batch = []
            if batch:
                yield batch
        except Exception as e:
            log.error(f"Error loading JSON: {e}")

    def read_excel(self):
        try:
            df = pd.read_excel(self.filename)
            batch = []
            for _, row in df.iterrows():
                batch.append(row.to_dict())
                if len(batch) >= self.batch_size:
                    yield batch
                    batch = []
            if batch:
                yield batch
        except Exception as e:
            log.error(f"Error loading XLSX (excel): {e}")

    def read_yaml(self, file):
        batch = []
        try:
            data_list = yaml.safe_load(file)
            for data in data_list:
                if isinstance(data, dict) and 'site' in data and 'id' in data:
                    batch.append(data)
                    if len(batch) >= self.batch_size:
                        yield batch
                        batch = []
        except Exception as e:
            log.error(f"Error loading YAML: {e}")
        if batch:
            yield batch
