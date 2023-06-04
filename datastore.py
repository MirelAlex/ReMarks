import json
import os
import copy


class Store():
    def __init__(self, path: str):
        self.file_path = path.strip('/')
        self.data_read = self.read_json()

    def read_json(self):
        folder_path, file_name = os.path.split(self.file_path)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data["remarks"]
        else:
            print(
                f"File '{self.file_path}' doesn't exist. Creating a new file.")
            with open(self.file_path, 'w') as file:
                empty_obj = {"remarks": []}
                json.dump(empty_obj, file)
            return empty_obj

    def save_data(self, data):
        _data = {"remarks": data}
        # Save JSON data to a file
        with open(self.file_path, "w") as file:
            json.dump(_data, file, indent=4)

        print(f"JSON data saved to '{file_path}'.")


file_path = '/data/data.json'
datastore = Store(file_path)
data = datastore.read_json()
print(data)
