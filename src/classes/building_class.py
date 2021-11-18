import json
import classes.elevator_class

'''this class hold a building object that is generated from a json file'''


class Building(object):
    def __init__(self, min_floor: int = None, max_floor: int = None, elevators: list = None):
        '''
        :param min_floor: min floor in the building.
        :param max_floor: max floor in the building.
        :param elevators: elevators list.
        '''
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.elevators = elevators

    '''this function initialize a building object from a json file, and make an elevators list.'''

    def init_from_file(self, file_path: str):
        with open(file_path, "r") as f:
            dict_building = json.load(f)
            self.min_floor = dict_building["_minFloor"]
            self.max_floor = dict_building["_maxFloor"]
            temp_elev = dict_building["_elevators"]
            self.elevators = classes.elevator_class.Elevator.init_from_list(temp_elev)

    '''return how many elevators are in the building'''

    def number_of_elevators(self):
        return len(self.elevators)

    def __str__(self):
        str = f"min floor: {self.min_floor}, max floor: {self.max_floor} elevators:["
        for i in self.elevators:
            str += f"({i})"
        str += "]"
        return str

# if __name__ == '__main__':
#     pass
# b = Building()
# b.init_from_file("../../input_data/json_buildings/b3.json")
# print(b)
# print(b.number_of_elevators())
# b._init_from_file("../../input_data/b2.json")
# print(b)
# b._init_from_file("../../input_data/b3.json")
# print(b)
# b._init_from_file("../../input_data/b4.json")
# print(b)
# b._init_from_file("../../input_data/b5.json")
# print(b)
