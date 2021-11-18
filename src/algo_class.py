import classes.building_class
import classes.call_class

'''this class is the main algorithm of the assignment.'''


#
class Algo:
    def __init__(self, building: classes.building_class.Building, calls: list):
        ''' return_calls -> list of calls with the final allocation of elevators.
            work_calls -> list of calls the algorithm works on, and delete calls that recived an allocation.
            building -> generated from a json file (contain all the necessary info on the building and elevators).
            used_list -> list that keep track of all the calls that we are done with.
        '''
        self.return_calls = calls
        self.work_calls = calls.copy()
        self.building = building
        self.used_list = []

    '''this function calculat the time it will take the elevator to reach the destination'''

    def time_to_end(self, call, elev):
        time = elev.close_time + elev.open_time + elev.stop_time + elev.start_time
        return (time + abs(call.src - call.dest) / elev.speed)

    ''' this function is responsible on running the main algorithm function as many time it takes,
        until it get an error (out of list boundaries)'''

    def final_overlap(self):
        while True:
            try:
                self.overlap()
            except:
                break
        for i in self.return_calls:
            print(i)

    ''' this function is the main function of this algorithm.
        it does the following steps:
        # for every elevator loop on every call in the call list, and for every call loop again on the rest of the calls
        # and build a list for every elevator that contain lists that each start in a specific call,
        # and contain all of the calls that are in the same time frame,
        # going in the same direction and in the same floors range
        # in the end the function will choose the longest list for each elevator, 
        # and allocate this elevator for this calls.
        # then the allocated calls are removed form the work_calls.'''

    def overlap(self):
        for elev in self.building.elevators:
            elev_call_lists = []
            for call in self.work_calls:
                if (self.used_list.__contains__(call)):
                    continue
                call_list = []
                call_list.append(call)
                time_to_end = self.time_to_end(call, elev)
                call_dir_up = call.src < call.dest
                for curr_call in range(self.work_calls.index(call), len(self.work_calls)):
                    if self.work_calls[curr_call].time > time_to_end:
                        break
                    # and self.work_calls[curr_call].src < self.work_calls[curr_call].dest
                    if call_dir_up and call.dest > self.work_calls[curr_call].src > call.src and self.work_calls[
                        curr_call].src < self.work_calls[curr_call].dest:
                        call_list.append(self.work_calls[curr_call])

                    elif (not call_dir_up) and call.dest < self.work_calls[curr_call].src < call.src and \
                            self.work_calls[curr_call].src > self.work_calls[curr_call].dest:
                        call_list.append(self.work_calls[curr_call])

                elev_call_lists.append(call_list)

            longest = elev_call_lists[0]
            for i in elev_call_lists:
                if len(i) > len(longest):
                    longest = i

            elev_index = self.building.elevators.index(elev)
            for call in self.return_calls:
                if (longest.__contains__(call)):
                    call.elev_allocate = elev_index
                    self.used_list.append(call)

            for call in self.work_calls:
                if (longest.__contains__(call)):
                    self.work_calls.remove(call)
