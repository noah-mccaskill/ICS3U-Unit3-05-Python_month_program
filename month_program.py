#!/usr/bin/env python3

# Created by: Noah McCaskill
# Created on: April 2022
# This is a month integer program


def main():

    # input
    month_number = int(input("Enter your number here! : "))

    # process & output
    if month_number == 1:
        print(
            "\nYour number corresponds to January, since you wrote {0}!".format(
                month_number
            )
        )
    elif month_number == 2:
        print(
            "\nYour number corresponds to February, since you wrote {0}!".format(
                month_number
            )
        )
    elif month_number == 3:
        print(
            "\nYour number corresponds to March, since you wrote {0}!".format(
                month_number
            )
        )
    elif month_number == 4:
        print(
            "\nYour number corresponds to April, since you wrote {0}!".format(
                month_number
            )
        )
    elif month_number == 5:
        print(
            "\nYour number corresponds to May, since you wrote {0}!".format(
                month_number
            )
        )
    elif month_number == 6:
        print(
            "\nYour number corresponds to June, since you wrote {0}!".format(
                month_number
            )
        )
    elif month_number == 7:
        print(
            "\nYour number corresponds to July, since you wrote {0}!".format(
                month_number
            )
        )
    elif month_number == 8:
        print(
            "\nYour number corresponds to August, since you wrote {0}!".format(
                month_number
            )
        )
    elif month_number == 9:
        print(
            "\nYour number corresponds to September, since you wrote {0}!".format(
                month_number
            )
        )
    elif month_number == 10:
        print(
            "\nYour number corresponds to October, since you wrote {0}!".format(
                month_number
            )
        )
    elif month_number == 11:
        print(
            "\nYour number corresponds to November, since you wrote {0}!".format(
                month_number
            )
        )
    elif month_number == 12:
        print(
            "\nYour number corresponds to December, since you wrote {0}!".format(
                month_number
            )
        )
    else:
        print("\nThat is not a month, since you wrote {0}!".format(month_number))
    print("\nDone!")


if __name__ == "__main__":
    main()
