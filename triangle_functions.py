#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Oct 2021
# This program calculates the area of a traingle with user input


def calculates_area(base, height):
    # calculates the area of a traingle

    # process
    area = base * height / 2

    print("The area of the triangle is {0} cm²".format(area))


def main():
    # this function just calls other functions

    # input
    base_from_user = input("Enter the base length of a triangle (cm): ")
    height_from_user = input("Enter the height of a triangle (cm): ")
    print("")

    try:
        base_int = int(base_from_user)
        height_int = int(height_from_user)
        # call finction
        calculates_area(base_int, height_int)

    except Exception:
        print("This is an invaild number!")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
