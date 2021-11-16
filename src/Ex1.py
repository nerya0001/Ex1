import sys
import classes.building_class
import classes.call_class
import algo_class


if __name__ == '__main__':
    # buliding = Building.init_from_file(sys.argv[1])
    # calls = Call.init_from_file(sys.argv[2])
    # out_name = str(sys.argv[3])
    building = classes.building_class.Building()
    building.init_from_file("../input_data/json_buildings/b4.json")
    calls = classes.call_class.Call.init_from_file("../input_data/csv_calls/Calls_b.csv")
    algo = algo_class.Algo(building, calls)
    algo.overlap()
    # algo.foreign()
    classes.call_class.Call.write_to(algo.return_calls, "out.csv")
