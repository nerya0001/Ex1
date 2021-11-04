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

    def __str__(self):
        return f"id: {self.id}, speed: {self.speed}, min floor: {self.min_floor}, max floor: {self.max_floor}, close " \
               f"time: {self.close_time}, open time: {self.open_time}, start time: {self.start_time}, stop" \
               f" time: {self.stop_time} "


if __name__ == '__main__':
    e = Elevator(2, 2.0, 0, 10, 0.2, 0.3, 0.1, 0.4)
    print(e)
