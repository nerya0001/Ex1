from classes.elevator_class import Elevator
from classes.building_class import Building
from enum import Enum
from classes.call_class import Call
from classes.our_timer import Timer


class State(Enum):
    DOWN = -1
    UP = 1
    LEVEL = 0


class Q_Node:

    def __init__(self, floor: int, elev: Elevator, elev_pos: int):
        self.floor = floor
        self.arrival_time = Our_algo.time_to_end(floor, elev, elev_pos)


class Elev_queue:

    def __init__(self):
        self.elev_state = State.LEVEL
        self.elev_pos = 0
        self.queue = []


class Our_algo:

    def __init__(self, building: Building):
        self.timer = Timer()
        self.building = building
        self.elev_list = []  # list of queues for each elevator
        for i in range(building.number_of_elevators()):
            self.elev_list.append(Elev_queue())

    def allocate_elev(self, call: Call):
        self.update()
        allo_elev = -1
        best_time = 9223372036854775807
        if (call.src < call.dest):
            for i in range(self.building.number_of_elevators()):
                curr_time = Our_algo.time_to_end(call.src, self.building.elevators[i], self.elev_list[i].elev_pos)
                if (self.elev_list[i].elev_state == State.UP and
                        self.elev_list[i].elev_pos < call.src and
                        curr_time < best_time):
                    best_time = curr_time
                    allo_elev = i
        else:
            for i in range(self.building.number_of_elevators()):
                curr_time = Our_algo.time_to_end(call.src, self.building.elevators[i], self.elev_list[i].elev_pos)
                if (self.elev_list[i].elev_state == State.DOWN and
                        self.elev_list[i].elev_pos > call.src and
                        curr_time < best_time):
                    best_time = curr_time
                    allo_elev = i

        if (allo_elev == -1):
            for i in range(self.building.number_of_elevators()):
                curr_time = Our_algo.time_to_end(call.src, self.building.elevators[i], self.elev_list[i].elev_pos)
                if (self.elev_list[i].elev_pos == State.LEVEL and curr_time < best_time):
                    best_time = curr_time
                    allo_elev = i

        if (allo_elev == -1):
            pass #allocate to the fastest elevator

        self.elev_list[allo_elev].queue.append(Q_Node(call.src, self.building.elevators[allo_elev],
                                                      self.elev_list[allo_elev].elev_pos))
        self.elev_list[allo_elev].queue.append(Q_Node(call.dest, self.building.elevators[allo_elev],
                                                      self.elev_list[allo_elev].elev_pos))
        call.elev_allocate = allo_elev
        self.update()

    def update(self):
        self.update_queue()
        self.update_state()
        self.update_pos()

    def update_queue(self):
        for i in self.elev_list:
            for q_node in i.queue:
                if (q_node.arrival_time <= self.timer.get_time()):
                    i.queue.remove(q_node)

    def update_pos(self):

        pass

    def update_state(self):
        pass

    def time_to_end(self, floor: int, elev: Elevator, elev_pos: int):
        floors = abs(elev_pos - floor)
        time = elev.close_time + elev.start_time + elev.stop_time + elev.open_time
        time += floors / elev.speed
        return time
