#!/usr/bin/env python3

def garden_operations(operation_number) -> None:
    if operation_number == 0:
        return (int('abc'))
    elif operation_number == 1:
        return (1/0)
    elif operation_number == 2:
        return (open('/non/existent/file'))
    elif operation_number == 3:
        return ('hi' + 123)
    else:
        return ()


def test_error_types() -> None:

    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as e1:
        print("Caught ValueError: " + str(e1))

    print("Testing operation 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as e2:
        print("Caught ZeroDivisionError: " + str(e2))

    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as e3:
        print("Caught FileNotFoundError: " + str(e3))

    print("Testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as e4:
        print("Caught TypeError: " + str(e4))

    print("Testing operation 4...")
    garden_operations(4)
    print("Operation completed successfully\n")


if __name__ == "__main__":

    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All error types tested successfully!")
