import csv
class Call:
    def __init__(self, time:float = None, src: int = None, dest: int = None, elev_allocate:int = -1):
        self.time = time
        self.elev_allocate = elev_allocate
        self.src = src
        self.dest = dest


    def init_from_file(file_path:str):
        calls_list = []
        with open(file_path, "r")as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                curr_call = Call(time=float(row[1]), src=int(row[2]), dest=int(row[3]),
                                 elev_allocate=row[5])
                calls_list.append(curr_call)
        return calls_list

    def __str__(self):
        return f"time = {self.time}, src = {self.src}, dest = {self.dest}, elev_allocate = {self.elev_allocate}"


# if __name__ == '__main__':
#     calls = Call.init_from_file("../../input_data/csv_calls/Calls_a.csv")
#     for i in calls:
#         print(f"{i}\n")




