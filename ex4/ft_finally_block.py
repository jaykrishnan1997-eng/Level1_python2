#!/usr/bin/env python3


class PlantError(Exception):
    def __init__(self, message="Invalid plant name to water:") -> None:
        super().__init__(message)


def water_plant(plant_name):
    if not plant_name == plant_name.capitalize():
        raise PlantError(f"'{plant_name}'")
        return (0)
    else:
        print(f"Watering {plant_name}: [OK]")
        return (1)


def test_watering_sysytem():

    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for valid_plant in ("Tomato", "Lettuce", "Carrots"):
            water_plant(valid_plant)
    except PlantError as e:
        print(f"Caught PlantError: Invalid plant name to water: {e}")
        print(".. ending tests and returning to main")
        return ()
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for invalid_plant in ("Tomato", "lettuce"):
            water_plant(invalid_plant)
    except PlantError as e1:
        print(f"Caught PlantError: Invalid plant name to water: {e1}")
        print(".. ending tests and returning to main")
        return ()
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_sysytem()
    print("Cleanup always happens, even with errors!")
