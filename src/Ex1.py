import sys
from classes.building_class import Building
from classes.call_class import Call
from our_algo import Our_algo


if __name__ == '__main__':
    buliding = Building.init_from_file(sys.argv[1])
    calls = Call.init_from_file(sys.argv[2])
    out_name = str(sys.argv[3])
    algo = Our_algo(buliding)
    algo.timer.start()
    for i in calls:
        algo.allocate_elev(i)

    Call.write_to(calls, out_name)
