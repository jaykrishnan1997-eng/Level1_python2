#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_custom_errors.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/01 11:29:44 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/01 12:52:14 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "The tomato plant is wilting!") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        raise PlantError()
    except PlantError as e1:
        print("Caught PlantError: " + str(e1))

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
