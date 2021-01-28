# Project 1


class Car:
    def __init__(self, make, mode, edition, color, average_mileage, gas_tank_capacity,
                 moon_roof=False):
        self.mode = mode
        self.make = make
        self.edition = edition
        self.color = color
        self.average_mileage = average_mileage
        self.gas_tank_capacity = gas_tank_capacity
        self.moon_roof = moon_roof
        self.start_engine = False
        self.max_speed_in_miles = 120  # convert to property

    def start(self):
        pass

    def stop(self):
        pass

    def increase_speed_by(self, increase_by):
        pass

    def decrease_speed_by(self, decrease_by):
        pass
