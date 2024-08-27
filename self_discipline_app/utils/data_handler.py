import json
import os

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
        return {}

    def write_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def create(self, key, value):
        data = self.read_data()
        data[key] = value
        self.write_data(data)

    def read(self, key):
        data = self.read_data()
        return data.get(key, None)

    def update(self, key, value):
        data = self.read_data()
        if key in data:
            data[key] = value
            self.write_data(data)

    def delete(self, key):
        data = self.read_data()
        if key in data:
            del data[key]
            self.write_data(data)