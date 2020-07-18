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
    pass

#child of vehicle
class FlightVehicle(Vehicle):
    pass

#child of flight vehicle
class Starship(FlightVehicle):
    pass

#child of flight vehicle
class Airplane(FlightVehicle):
    pass

#child of vehicle
class GroundVehicle(Vehicle):
    pass

#child of ground vehicle
class Car(GroundVehicle):
    pass

#child of ground vehicle
class Motorcycle(GroundVehicle):
    pass
