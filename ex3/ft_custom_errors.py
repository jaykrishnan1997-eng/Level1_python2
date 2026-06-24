#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="The tomato plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!") -> None:
        super().__init__(message)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError()
    except PlantError as e1:
        print("Caught PlantError:" + str(e1))

    print("\nTesting WaterError...")
    try:
        raise WaterError()
    except WaterError as e2:
        print("Caught WaterError:", e2)

    print("\nTesting catching all garden errors...")

    for error in (PlantError, WaterError):
        try:
            raise error
        except GardenError as e:
            print("Caught GardenError:", e)

    print("\nAll custom error types work correctly!")
