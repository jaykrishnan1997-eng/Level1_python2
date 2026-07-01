#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_finally_block.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/01 11:29:47 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/01 13:08:18 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class PlantError(Exception):
    def __init__(self, message: str = "Invalid plant name to water:") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if not plant_name == plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:

    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for valid_plant in ("Tomato", "Lettuce", "Carrots"):
            water_plant(valid_plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for invalid_plant in ("Tomato", "lettuce"):
            water_plant(invalid_plant)
    except PlantError as e1:
        print(f"Caught PlantError: {e1}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("Cleanup always happens, even with errors!")
