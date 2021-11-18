from unittest import TestCase
import classes.building_class
import classes.elevator_class

class TestElevator(TestCase):
    def test_init_from_list(self):
        b = classes.building_class.Building()
        b.init_from_file("../input_data/json_buildings/b3.json")
        self.assertTrue(type(b.elevators), list)
        self.assertTrue(type(b.elevators[1]), classes.elevator_class.Elevator)
        self.assertEqual(b.elevators[0].speed, 3.0)
