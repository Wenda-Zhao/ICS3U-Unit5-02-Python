#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Jan 2021
# This program for calculate area of triangle


def calculate_area(length, high):
    # this function is calculate the area

    # process & output
    try:
        length_int = int(length)
        try:
            high_int = int(high)
            area = 1/2 * length_int * high_int
            print("The area of the triangle is:{0}cm²".format(area))
        except Exception:
            print("The high is not a integer")
    except Exception:
        print("The length is not a integer")


def main():
    # This function is get the length and high

    # input
    length = input("Enter the length: ")
    high = input("Enter the high: ")

    # call functions
    calculate_area(length, high)


if __name__ == "__main__":
    main()
