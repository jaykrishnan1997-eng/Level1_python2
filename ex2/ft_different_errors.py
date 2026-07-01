#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/01 11:29:39 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/01 12:01:44 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        1/0
    elif operation_number == 2:
        open('/non/existent/file')
    elif operation_number == 3:
        'hi' + 123
    else:
        return


def test_error_types() -> None:

    for i in range(0, 5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as e1:
            print("Caught ValueError: " + str(e1))
        except ZeroDivisionError as e2:
            print("Caught ZeroDivisionError: " + str(e2))
        except FileNotFoundError as e3:
            print("Caught FileNotFoundError: " + str(e3))
        except TypeError as e4:
            print("Caught TypeError: " + str(e4))
        else:
            print("Operation completed successfully\n")


if __name__ == "__main__":

    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!")
