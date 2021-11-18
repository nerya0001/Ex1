import csv

'''this class hold a call object that is generated from a csv file'''


class Call:
    def __init__(self, data):
        '''
        name -> hold a string "Elevator call".
        time -> hold the specific second from the start of the actual operation that the call is entering the system.
        src -> hold the source floor of the call.
        dest -> hold the destination floor of the call.
        state -> non relevant but necessary for correct output
        elev_allocation -> hold the index of the elevator allocated for this call
        '''
        self.name = data[0]
        self.time = float(data[1])
        self.src = int(data[2])
        self.dest = int(data[3])
        self.state = data[4]
        self.elev_allocate = int(data[5])

    '''this function initialize a calls list from a csv file'''

    def init_from_file(file_path: str):
        calls_list = []
        with open(file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                curr_call = Call(row)
                calls_list.append(curr_call)
        return calls_list

    '''this function write from an allocated calls list to an output csv file'''

    def write_to(calls, file_name):
        call = []
        for i in calls:
            call.append(i.__dict__.values())
        with open(f'../out/{file_name}', "w", newline="") as ans:
            writer = csv.writer(ans)
            writer.writerows(call)

    def __contains__(self, item):
        return (self.time == Call(item).time)

    def __str__(self):
        return f"time = {self.time}, src = {self.src}, dest = {self.dest}, elev_allocate = {self.elev_allocate}"

# if __name__ == '__main__':
#     pass
#     calls = Call.init_from_file("../../input_data/csv_calls/Calls_a.csv")
#     l = [calls[0],calls[2],calls[3]]
#     l1 = [calls[0],calls[2],calls[3]]
#     print(l.__contains__(l1[0]))
#     print(l.__contains__(calls[5]))
# b = classes.building_class.Building()
# b.init_from_file("../../input_data/json_buildings/b4.json")
# b.elevators.sort()
# for i in calls:
#     i.elev_allocate = random.randrange(0, b.number_of_elevators(), 1)
# Call.write_to(calls, "out.csv")
# for i in calls:
#     print(f"{i}\n")
# algo = algo_class.Algo(b, calls)
# algo.foreign()
# Call.write_to(algo.return_calls, "out.csv")
