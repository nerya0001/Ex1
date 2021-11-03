import json


class Building:
    def __init__(self, min_floor: int = None, max_floor: int = None, elevators: list = None):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elevators = elevators

    def _init_from_file(self, file_name: str) -> None:
        new_building_dict = {}
        with open(file_name, "r") as f:
            dict_building = json.load(f)
            pass
