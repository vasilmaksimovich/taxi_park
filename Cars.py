# -*- coding: utf-8 -*-
##
##
class Taxi_park:
    def __init__(self):
        pass


class Constants:  # Constants for calculation
    class Fuel:  # Cost of fuel
        FUEL_DIESEL_PRICE = 1.8
        FUEL_BENZIN_92_PRICE = 2.2
        FUEL_BENZIN_95_PRICE = 2.4

    class Consumption:   # Consumption
        FUEL_DIESEL_CONS = 6
        FUEL_BENZIN_CONS = 8

    class Repair_cost:  # Coasts of different repairs
        GENERAL_REPAIR_DIESEL_COST = 700
        GENERAL_REPAIR_BENZIN_COST = 500
        ENFINE_REPLACEMENT = 3000

    class Periods_of_service:     #  Periods of service
        GENERAL_REPAIR_DIESEL_PERIOD = 150000
        GENERAL_REPAIR_BENZIN_PERIOD = 100000
        CHANGE_BENZIN_PERIOD = 50000
        CHANGE_ENGINE_DIESEL = 5000000
        CHANGE_ENGINE_BENZIN = 4000000

    class Amortization:
        AMORTIZATION_DIESEL = 10.5
        AMORTIZATION_BENZIN = 9.5
        PERIOD_OF_AMORTIZATION = 1000





class Car(Taxi_park):
    all_cars = []

    def __init__(self):
        self.engine = self.calculate_engine_type()

    def calculate_engine_type(self):
        if not len(Car.all_cars) % 3:
            return Engine('diesel')
        else:
            return Engine('benzin')

        # Cars generator
        # for i in range(1, 101):
        #     if not i % 3 and i % 5:
        #         Car('diesel', 75.0)
        #     elif not i % 3:
        #         Car('diesel, 60.0')
        #     elif not i % 5:
        #         Car('benzin', 75.0)
        #     else:
        #         Car('benzine', 60.0)
        # return Car


class Engine(Car):
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    @property
    def is_diesel(self):
        return self.fuel_type == 'diesel'

    @property
    def is_benzin(self):
        return self.fuel_type == 'benzine'


all_car = (Car() for i in range(12))
for machine in all_car:
    print machine.engine.fuel_type
