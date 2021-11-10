import csv
import random
from  building_class import Building


class Call:
    def __init__(self, data):
        self.name = data[0]
        self.time = data[1]
        self.src = data[2]
        self.dest = data[3]
        self.state = data[4]
        self.elev_allocate = data[5]

    def init_from_file(file_path:str):
        calls_list = []
        with open(file_path, "r")as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                curr_call = Call(row)
                calls_list.append(curr_call)
        return calls_list

    def write_to(calls):
        call = []
        for i in calls:
            call.append(i.__dict__.values())
        with open('../../input_data/out/out.csv', "w", newline="") as ans:
            writer = csv.writer(ans)
            writer.writerows(call)

    def __str__(self):
        return f"time = {self.time}, src = {self.src}, dest = {self.dest}, elev_allocate = {self.elev_allocate}"


if __name__ == '__main__':
    calls = Call.init_from_file("../../input_data/csv_calls/Calls_a.csv")
    b = Building()
    b.init_from_file("../../input_data/json_buildings/b5.json")
    print(len(b.elevators))
    for i in calls:
        i.elev_allocate = random.randrange(0, len(b.elevators), 1)
    Call.write_to(calls)
#     for i in calls:
#         print(f"{i}\n")




