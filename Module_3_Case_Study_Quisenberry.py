# Name: Nathan Quisenberry
# File: module3_case_study.py
# Description: This program demonstrates the use of classes and inheritance.
# The vehicle class serves as a superclass, and the automobile class inherits from vehicle.
# The user enter sinformstion about a car, and the program displays the vehicle
# information in an easy-to-read format.

# Variables:
# year - stores the vehicle year
# make - stores the vehicle manufacturer
# model - stores the vehicle model
# doors - stores the number of doors (2 or 4)
# roof - stores the roof type (solid or sun roof)

# Superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Subclass
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Gather usesr input
year = input("Enter the vehicle year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")

# Validate doors
while True:
    doors = input("Enter the number of doors (2 or 4): ")
    if doors in ("2", "4"):
        break
    print("Invalid entry, Please enter 2 or 4.")

# Validate roof
while True:
    roof = input("Enter the roof type (solid or sun roof): ").lower()
    if roof in ("solid", "sun roof"):
        break
    print("Invalid Entry, Please enter 'solid' or 'sun roof'.")

# Create automobile object
car = Automobile("car", year, make, model, doors, roof)

# Display results
print("\nVehicle Information")
print("-------------------")
print(f"Vehicle type: {car.vehicle_type}")
print(f"Year: {car.year}")
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Number of doors: {car.doors}")
print(f"Type of roor: {car.roof}")


