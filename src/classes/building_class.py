import json


class Building(object):
    def __init__(self, min_floor: int = None, max_floor: int = None, elevators: list = None):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elevators = elevators

    def _init_from_file(self, file_name: str):
        with open(file_name, "r") as f:
            dict_building = json.load(f)
            self.min_floor = dict_building["_minFloor"]
            self.max_floor = dict_building["_maxFloor"]
            self.elevators = dict_building["_elevators"]

    def number_of_elevators(self):
        return len(self.elevators)

    def __str__(self):
        return f"min floor: {self.min_floor}, max floor: {self.max_floor} elevators: {self.elevators}"


if __name__ == '__main__':
    b = Building()
    b._init_from_file("../../input_data/b1.json")
    print(b)
    print(b.number_of_elevators())
    # b._init_from_file("../../input_data/b2.json")
    # print(b)
    # b._init_from_file("../../input_data/b3.json")
    # print(b)
    # b._init_from_file("../../input_data/b4.json")
    # print(b)
    # b._init_from_file("../../input_data/b5.json")
    # print(b)
