#!/usr/bin/env python3\
# Created By:Kamche
# Created on: October 29, 2026
# This program asks the user to enter
# a year so it can calculate
# and determine if it is a leap year or not


def main():
    # Ask the user to enter a year
    leap_year_str = input("Enter a year that could be a leap year:")

    try:
        leap_year_int = int(leap_year_str)

        # Check if the year is positive
        if leap_year_int <= 0:
            print("This year is not positive, but it is an integer.")
            print("Please enter a positive year in order to do the program.")

        # Check if the year is a leap year
        if leap_year_int % 4 == 0:
            if leap_year_int % 100 == 0:
                if leap_year_int % 400 == 0:
                    print("{0} is a leap year.".format(leap_year_str))
                else:
                    print("{0} is not a leap year.".format(leap_year_str))
            else:
                print("{0} is a leap year.".format(leap_year_str))
        else:
            print("{0} is not a leap year.".format(leap_year_str))

    except:
        print("{} is not a valid entry or integer.".format(leap_year_str))
        print("Please enter a valid integer.")
    finally:
        print("Thank you for playing")


if __name__ == "__main__":
    main()
