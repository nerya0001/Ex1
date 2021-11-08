import sys
from classes.building_class import Building
if __name__ == '__main__':
    b = Building()
    b._init_from_file(sys.argv.pop(1))
    print(b)
