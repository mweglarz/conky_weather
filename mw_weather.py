#!/bin/python

import json
import urllib.parse
import urllib.request
from sys import argv
from Wind import Wind
from Atmosphere import Atmosphere
from Condition import Condition

# print(data['query']['results'])

class Weather:

    def __init__(self, woeid):
        self.woeid = woeid

    def getWeather(self):
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        # woeid = 502075
        woeid = self.woeid
        yql_query = "select item, wind, atmosphere, units from weather.forecast where woeid=%d" % woeid
        yql_url = baseurl + urllib.parse.urlencode({'q':yql_query}) + "&format=json"
        print("request = %s" % yql_url)
        print()
        result = urllib.request.urlopen(yql_url).read()
        data = json.loads(result)
        self.__handleResponse(data)

    def __handleResponse(self, data):
        # print(data)
        channel = data['query']['results']['channel']
        item = channel['item']
        units = channel['units']

        wind = channel['wind']
        windString = self.__transformWind(wind, units)
        print(windString)

        atmosphere = channel['atmosphere']
        atmosphereString = self.__transformAthmosphere(atmosphere, units)
        print(atmosphereString)

        condition = item['condition']
        conditionString = self.__transformCondition(condition, units)
        print(conditionString)

        forecast = item['forecast']
        forecastString = self.__transformForecast(forecast, units)

    def __transformWind(self, wind, units):
        wind = Wind(wind, units)
        return wind.getString()

    def __transformAthmosphere(self, atmosphere, units):
        atmosphere = Atmosphere(atmosphere, units)
        return atmosphere.getString()

    def __transformCondition(self, condition, units):
        condition = Condition(condition, units)
        return condition.getString()

    def __transformForecast(self, forecast, units):
        return ""


if __name__ == '__main__':
    # woeid = int(argv[1])
    woeid = 502075
    weather = Weather(woeid)
    weather.getWeather()
