import random
import classes.elevator_class
import classes.building_class
import classes.call_class
from classes.our_timer import Timer


class Algo:
    def __init__(self, building: classes.building_class.Building, calls: list):
        self.return_calls = calls
        self.work_calls = calls.copy()
        self.building = building


    def time_to_end(self, call, elev):
        time = elev.close_time + elev.open_time + elev.stop_time + elev.start_time
        return (time + abs(call.src - call.dest) / elev.speed)


    def foreign(self):
        for elev in self.building.elevators:
            vacate = 0
            curr_elev_calls = []
            for call in self.work_calls:
                if not curr_elev_calls:  # if curr_elev_calls is empty
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


    def overlap(self):
        for elev in self.building.elevators:
            print("new elev\n")
            elev_call_lists = []
            for call in self.work_calls:
                call_list = []
                call_list.append(call)
                time_to_end = self.time_to_end(call, elev)
                call_dir_up = call.src < call.dest
                for curr_call in range(self.work_calls.index(call), len(self.work_calls)):
                    if self.work_calls[curr_call].time > time_to_end:
                        break
                    if ((self.work_calls[curr_call].time < time_to_end) and (
                            self.work_calls[curr_call].src < self.work_calls[curr_call].dest) == call_dir_up):

                        if call_dir_up and  call.dest > self.work_calls[curr_call].src > call.src:

                            call_list.append(curr_call)

                        elif (not call_dir_up) and call.dest < self.work_calls[curr_call].src < call.src:
                            call_list.append(curr_call)

            elev_call_lists.append(call_list)

            longest = elev_call_lists[0]
            for i in elev_call_lists:
                if len(i) > len(longest):
                    longest = i

            elev_index = self.building.elevators.index(elev)
            for call in self.return_calls:
                if (longest.__contains__(call)):
                    call.elev_allocate = elev_index

            for call in longest:
                self.work_calls.remove(call)
            if elev == self.building.elevators[0]:
                for i in elev_call_lists:
                    for j in i:
                        print(j)
                    print("\n")