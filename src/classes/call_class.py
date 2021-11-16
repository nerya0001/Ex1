import csv
import random
import algo_class
import classes.building_class


class Call:
    def __init__(self, data):
        self.name = data[0]
        self.time = float(data[1])
        self.src = int(data[2])
        self.dest = int(data[3])
        self.state = data[4]
        self.elev_allocate = int(data[5])

    def init_from_file(file_path:str):
        calls_list = []
        with open(file_path, "r")as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                curr_call = Call(row)
                calls_list.append(curr_call)
        return calls_list

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


if __name__ == '__main__':
    pass
    # calls = Call.init_from_file("../../input_data/csv_calls/Calls_a.csv")
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







