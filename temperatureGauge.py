# Author: Maxwell Herron
# This program will activate the ADT7410 temperature sensor once every hour and
# log the current temperature in a CSV file.

import time
import csv
import datetime
import board
import busio
import adafruit_adt7410

i2c_bus = busio.I2C(board.SCL, board.SDA)
adt = adafruit_adt7410.ADT7410(i2c_bus, address=0x48)
adt.high_resolution = True

csvData = [['Date', 'Time', 'Temperature']]


def main():

    while True:
        now = datetime.datetime.now()
        date = str(now.month) + '/' + str(now.day) + '/' + str(now.year)
        current_time = str(now.hour) + ':' + str(now.minute)
        temp = str(adt.temperature)

        row = [date, current_time, temp]
        write_to_file(row)
        time.sleep(3600.0)


if __name__ == '__main__':
    main()


def write_to_file(row):
    with open('temperature.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
