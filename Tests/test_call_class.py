from unittest import TestCase
import classes.call_class
import algo_class

class TestCall(TestCase):
    def test_init_from_file(self):
        calls = classes.call_class.Call.init_from_file("../input_data/csv_calls/Calls_a.csv")
        self.assertTrue(calls[3].src, 3)
        self.assertTrue(calls[3].dest, 2)
        self.assertTrue(calls[3].time, 85.52096662)

    def test_write_to(self):
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

