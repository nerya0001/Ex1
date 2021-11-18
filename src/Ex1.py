import sys
import classes.building_class
import classes.call_class
import algo_class

''' this is the main function
    it receive input as arguments: building.jason file, calls.csv file and a output.csv file'''

if __name__ == '__main__':
    building = classes.building_class.Building()
    building.init_from_file(sys.argv[1])
    calls = classes.call_class.Call.init_from_file(sys.argv[2])
    out_name = str(sys.argv[3])
    # building = classes.building_class.Building()
    # building.init_from_file("../input_data/json_buildings/b5.json")
    # calls = classes.call_class.Call.init_from_file("../input_data/csv_calls/Calls_d.csv")
    algo = algo_class.Algo(building, calls)
    algo.final_overlap()
    classes.call_class.Call.write_to(algo.return_calls, out_name)
