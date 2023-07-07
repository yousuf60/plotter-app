import json
import os.path

path = os.path.abspath(os.path.dirname(__file__))
data_path = os.path.join(path, "data")


class DataManager:
    def make_file(self, name):
        with open(self.path_join(name), mode="w") as f:
            f.write("{}")
    
    def remove_file(self, name):
        os.remove(self.path_join(name))
    
    def read_file(self, file_name):
        with open(self.path_join(file_name), mode="r") as f:
            file_data = json.load(f)
        return file_data

    def write_data(self, file_name, data):
        with open(self.path_join(file_name), "w") as f:
            json.dump(data, f)

    def path_join(self, name):
        return os.path.join(data_path, name)


if __name__ == "__main__":
    dataManager = DataManager()
    dataManager.make_file("test.json")
    dataManager.write_data("test.json", {"wkeg":[308e10, 0]})
    print(dataManager.read_file("test.json"))
    dataManager.remove_file("test.json")
    

