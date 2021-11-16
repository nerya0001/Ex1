import random
import classes.elevator_class
import classes.building_class
import classes.call_class
from classes.our_timer import Timer


class Algo:
    def __init__(self, building: classes.building_class.Building, calls:list):
        self.return_calls = calls
        self.work_calls = calls.copy()
        self.building = building

    def foreign(self):
        for elev in self.building.elevators:
            vacate = 0
            curr_elev_calls = []
            for call in self.work_calls:
                if not curr_elev_calls:# if curr_elev_calls is empty
                    curr_elev_calls.append(call)
                    vacate = call.time + self.time_to_end(call, elev)
                    self.work_calls.remove(call)

                if (call.time > vacate):
                    curr_elev_calls.append(call)
                    vacate = call.time + self.time_to_end(call, elev)
                    self.work_calls.remove(call)

            for call in curr_elev_calls:
                for allocat_call in self.return_calls:
                    if (call.time == allocat_call.time):
                        allocat_call.elev_allocate = self.building.elevators.index(elev)
                        break

        for call in self.return_calls:
            if (call.elev_allocate == -1):
                call.elev_allocate = random.randrange(0, self.building.number_of_elevators(), 1)


    def time_to_end(self, call, elev):
        time = elev.close_time + elev.open_time + elev.stop_time + elev.start_time
        return (time + abs(call.src - call.dest)/elev.speed)


    def overlap(self):

        pass



    def allocate(self, call):
        pass


