from classes.elevator_class import Elevator
from classes.building_class import Building
from classes.call_class import Call


class Out_algo:

    def __init__(self, building: Building):
        pass

    def allocat_elev(call):
        pass

    def time_to_end(call: Call, elev: Elevator, elev_pos: int):
        floors = abs(call.dest - call.src)
        time = elev.close_time + elev.start_time + elev.stop_time + elev.open_time
        time += floors / elev.speed
        return time
