import json
import os.path
from os import listdir

path = os.path.abspath(os.path.dirname(__file__))
# do not forget to make /data dir or edit the code as you need
data_path = os.path.join(path, "data")


class DataManager:
    
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = self.path_join(file_name)

    def make_file(self):
        with open(self.file_name, mode="w") as f:
            f.write("{}")
    
    def remove_file(self):
        os.remove(self.file_name)
    
    def read_file(self):
        with open(self.file_name, mode="r") as f:
            file_data = json.load(f)
        return file_data

    def write_data(self, data):
        with open(self.file_name, "w") as f:
            json.dump(data, f)

    def path_join(self, name):
        return os.path.join(data_path, name)

    def file_exists(self, name):
        return os.path.exists(self.path_join(name))
    
    def change_file(self, file_name):
        self.file_name = self.path_join(file_name)

    def data_files(self):
        return listdir(data_path)

if __name__ == "__main__":
    dataManager = DataManager("test.json")
    dataManager.make_file()
    dataManager.write_data({"wkeg":[308e10, 0]})
    print(dataManager.read_file())
    print(dataManager.file_exists("test.json"))
    print(dataManager.file_exists("teggst.json"))
    print(dataManager.file_exists("")) #dir
    dataManager.remove_file()
    

