from unittest import TestCase
import classes.building_class


class TestBuilding(TestCase):

    def test_init_from_file(self):
        b = classes.building_class.Building()
        b.init_from_file("../input_data/json_buildings/b3.json")
        c = classes.building_class.Building()
        c.init_from_file("../input_data/json_buildings/b3.json")
        d = classes.building_class.Building()
        d.init_from_file("../input_data/json_buildings/b4.json")
        self.assertEqual(b.max_floor, c.max_floor)
        self.assertNotEqual(b.number_of_elevators(), d.number_of_elevators())

    def test_number_of_elevators(self):
        c = classes.building_class.Building()
        c.init_from_file("../input_data/json_buildings/b3.json")
        d = classes.building_class.Building()
        d.init_from_file("../input_data/json_buildings/b4.json")
        self.assertTrue(c.number_of_elevators(), 2)
        self.assertTrue(d.number_of_elevators(), 5)
        self.assertNotEqual(d.number_of_elevators(), 7)
