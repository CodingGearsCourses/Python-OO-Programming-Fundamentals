# https://www.globaletraining.com/
# Methods


class Car:
    # Class Attributes/Variables
    no_of_tires = 4

    # Class Constructor/Initializer (Method with a special name)
    def __init__(self):
        # Object Attributes/Variables
        self.make = "Ford"
        self.model = "Mustang"
        self.year = 2010
        self.color = "Blue"
        self.moon_roof = True
        self.engine_running = False

    #  Methods
    def start_the_engine(self):
        self.engine_running = True

    def stop_the_engine(self):
        self.engine_running = False
