#!/bin/python

import yaml
from sys import argv

city = 'city'
temp = 'temp'
code = 'code'
text = 'text'
windSpeed = 'speed'
windUnits = 'speedUnits'
humidity = 'humidity'

# needs number after key
day = 'day'
dayCode = 'dayCode'
dayHigh = 'dayHigh'
dayLow = 'dayLow'


def read(key, number):
    with open('weather_data.yml', 'r') as ymlFile:
        data = yaml.load(ymlFile)
        data = data['weather']

        if key == city:
            return data['city']
        elif key == temp:
            return data['condition']['temp']
        elif key == code:
            return data['condition']['code']
        elif key == text:
            return data['condition']['text']
        elif key == windSpeed:
            return data['wind']['speed']
        elif key == windUnits:
            return 'km/h'
        elif key == humidity:
            return data['atmosphere']['humidity']
        elif number is not None:
            mKey = "%s%d" % ('day', number)
            data = data['forecast'][mKey]

            if key == day:
                return data['day']
            elif key == dayCode:
                return data['code']
            elif key == dayHigh:
                return data['high']
            elif key == dayLow:
                return data['low']

        return 'unknown'

if __name__ == '__main__':
    key = argv[1]
    number = None
    if len(argv) > 2:
        number = int(argv[2])
    result = read(key, number)
    print(result)
