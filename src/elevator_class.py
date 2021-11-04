class Elevator(object):
    def __init__(self, id: int = None, speed: float = None, min_floor: int = None, max_floor: int = None,
                 close_time: float = None, open_time: float = None, start_time: float = None, stop_time: float = None):
        self.id = id
        self.speed = speed
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time
