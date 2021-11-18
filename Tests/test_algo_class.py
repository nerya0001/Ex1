from unittest import TestCase
import classes.call_class
import classes.building_class
import algo_class
import classes.elevator_class

class TestAlgo(TestCase):
    def test_time_to_end(self):
        b = classes.building_class.Building()
        b.init_from_file("../input_data/json_buildings/b3.json")
        calls = classes.call_class.Call.init_from_file("../input_data/csv_calls/Calls_a.csv")
        elevator1 = b.elevators[0]
        call1 = calls[0]
        time_to_end = algo_class.Algo.time_to_end(algo_class.Algo, call1, elevator1)
        self.assertTrue(time_to_end, 10.333333333333334)

    def test_final_overlap(self):
        b = classes.building_class.Building()
        b.init_from_file("../input_data/json_buildings/b3.json")
        calls = classes.call_class.Call.init_from_file("../input_data/csv_calls/Calls_a.csv")
        algo = algo_class.Algo(b, calls)
        algo.final_overlap()
        classes.call_class.Call.write_to(algo.return_calls, 'out.csv')
        result = classes.call_class.Call.init_from_file("../out/out.csv")
        self.assertEqual(result[5].src, 0)
        self.assertEqual(result[5].dest, 4)
        self.assertEqual(result[5].time, 104.1370124)
        self.assertTrue(calls[3].src, 3)
        self.assertTrue(calls[3].dest, 2)
        self.assertTrue(calls[3].time, 85.52096662)

    def test_overlap(self):
        b = classes.building_class.Building()
        b.init_from_file("../input_data/json_buildings/b3.json")
        calls = classes.call_class.Call.init_from_file("../input_data/csv_calls/Calls_a.csv")
        algo = algo_class.Algo(b, calls)
        algo.final_overlap()
        classes.call_class.Call.write_to(algo.return_calls, 'out.csv')
        result = classes.call_class.Call.init_from_file("../out/out.csv")
        self.assertEqual(result[5].src, 0)
        self.assertEqual(result[5].dest, 4)
        self.assertEqual(result[5].time, 104.1370124)
        self.assertEqual(calls[11].src, 0)
        self.assertTrue(calls[11].dest, 4)
        self.assertTrue(calls[11].time, 137.9515274)