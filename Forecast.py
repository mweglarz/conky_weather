
import Utility as util


class ForecastDay:

    def __init__(self, data, units, number):
        self.isImperialUnits = util.isImperialUnits(units)
        self.number = number
        self.code = data['code']
        self.high = int(data['high'])
        self.low = int(data['low'])
        self.day  = data['day']
        self.text = data['text']

        if util.isImperialUnits(units):
            self.metricHigh = util.FtoC(self.high)
            self.metricLow = util.FtoC(self.low)
        else:
            self.metricHigh = self.high
            self.metricLow = self.low


    def getString(self):
        return "  day%d:\n   code: %s\n   day: %s\n   low: %d\n   high: %d\n   text: %s\n" % (self.number, self.code, self.day, self.metricLow, self.metricHigh, self.text)

class Forecast:

    def __init__(self, data, units):
        data0 = data[1]
        data1 = data[2]
        data2 = data[3]
        data3 = data[4]
        data4 = data[5]

        self.day0 = ForecastDay(data0, units, 0)
        self.day1 = ForecastDay(data1, units, 1)
        self.day2 = ForecastDay(data2, units, 2)
        self.day3 = ForecastDay(data3, units, 3)
        self.day4 = ForecastDay(data4, units, 4)

    def getString(self):
        return " forecast:\n%s%s%s%s%s" % (self.day0.getString(), self.day1.getString(), self.day2.getString(), self.day3.getString(), self.day4.getString())
