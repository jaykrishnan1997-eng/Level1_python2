#!/usr/bin/env python3


class PlantError(Exception):
    def __init__(self, message="Invalid plant name to water:") -> None:
        super().__init__(message)


def water_plant(plant_name):
    if not plant_name[0].isupper():
        try:
            raise PlantError(f"'{plant_name}'")
        except PlantError as e:
            print(f"Caught PlantError: Invalid plant name to water:{e}")
            print(".. ending tests and returning to main")
    else:
        print(f"Watering {plant_name}: [OK]")        

if __name__ == "__main__":
    print("=== Garden Watering System ===\n")

    print("Testing valid plants...")
    print("Opening watering system")
    water_plant("Tomato")
    water_plant("Lettuce")
    water_plant("Carrots")
    print("Closing watering system\n")


    print("Testing invalid plants...")
    print("Opening watering system")
    water_plant("Tomato")
    water_plant("lettuce")
    print("Closing watering system\n")

    print("Cleanup always happens, even with errors!")
