#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_raise_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/01 11:29:36 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/01 11:54:42 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    else:
        return temp


def test_temperature() -> None:

    print("Input data is '25'")
    print(f"Temperature is now {input_temperature('25')}°C\n")

    print("Input data is 'abc'")
    try:
        input_temperature('abc')
    except ValueError as e1:
        print("Caught input_temperature error: " + str(e1) + "\n")

    print("Input data is '100'")
    try:
        input_temperature('100')
    except ValueError as e2:
        print("Caught input_temperature error: " + str(e2) + "\n")

    print("Input data is '-50'")
    try:
        input_temperature('-50')
    except ValueError as e3:
        print("Caught input_temperature error: " + str(e3) + "\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("All tests completed - program didn't crash!")
