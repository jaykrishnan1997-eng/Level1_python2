#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/01 11:29:33 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/01 11:30:10 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:

    print("Input data is '25'")
    print(f"Temperature is now {input_temperature('25')}°C\n")

    print("Input data is 'abc'")
    try:
        input_temperature('abc')
    except ValueError as e:
        print("Caught input_temperature error: " + str(e))


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
