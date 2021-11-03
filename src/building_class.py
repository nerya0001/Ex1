import json


class Building:
    def __init__(self, min_floor: int = None, max_floor: int = None, elevators: list = None):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elevators = elevators

    def _init_from_file(self, file_name: str):
        new_building_dict = {}
        with open(file_name, "r") as f:
            dict_building = json.load(f)
            self.min_floor = dict_building["_minFloor"]
            self.max_floor = dict_building["_maxFloor"]
            self.elevators = dict_building["_elevators"]

    def __str__(self):
        return f"min floor: {self.min_floor}, max floor: {self.max_floor}, elevators: {self.elevators}"




if __name__ == '__main__':

    b2 = Building()
    b2._init_from_file("C:/Users/Nery0001/PycharmProjects/Ex1/input_data/b2.json")
    print(b2)


