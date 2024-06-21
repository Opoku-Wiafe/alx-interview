#!/usr/bin/python3

import sys


def display_message(dictStatus, file_size):
    """
    Write a script that reads stdin line by line and computes metrics:
    Args:
        dictStatus: dict of status codes
        file_size: total file size
    Returns:
        Nothing
    """

    print("File size: {}".format(file_size))
    for key, value in sorted(dictStatus.items()):
        if value != 0:
            print("{}: {}".format(key, value))


file_size = 0
code = 0
counter = 0
dictStatus = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if (code in dictStatus.keys()):
                    dictStatus[code] += 1

            if (counter == 10):
                display_message(dictStatus, file_size)
                counter = 0

finally:
    display_message(dictStatus, file_size)
