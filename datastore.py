import json
import os


class Store():
    def __init__(self, path: str):
        self.file_path = path.strip('/')

    def read_json(self):
        folder_path, file_name = os.path.split(self.file_path)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data
        else:
            print(
                f"File '{self.file_path}' doesn't exist. Creating a new file.")
            with open(self.file_path, 'w') as file:
                json.dump({}, file)
            return {}


file_path = '/data/data.json'
datastore = Store(file_path)
data = datastore.read_json()
print(data)
