# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    def __init__(self, vehicle):
        self.vehicle = vehicle


#child of vehicle
class FlightVehicle(Vehicle):
    def __init__(self, vehicle, flightvehicle):
        super().__init__(vehicle)
        self.flightvehicle = flightvehicle

#child of flight vehicle
class Starship(FlightVehicle):
    def __init__(self, vehicle, flightvehicle, starship):
        super().__init__(vehicle, flightvehicle)
        self.starship = starship

#child of flight vehicle
class Airplane(FlightVehicle):
    def __init__(self, vehicle, flightvehicle, airplane):
        super().__init__(vehicle, flightvehicle)
        self.airplane = airplane

#child of vehicle
class GroundVehicle(Vehicle):
    def __init__(self, vehicle, groundvehicle):
        super().__init__(vehicle)
        self.groundvehicle = groundvehicle

#child of ground vehicle
class Car(GroundVehicle):
    def __init__(self, vehicle, groundvehicle, car):
        super().__init__(vehicle, groundvehicle)
        self.car = car

#child of ground vehicle
class Motorcycle(GroundVehicle):
    def __init__(self, vehicle, groundvehicle, motorcycle):
        super().__init__(vehicle, groundvehicle)
        self.motorcycle = motorcycle
