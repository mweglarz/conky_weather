
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
        return "\t\tday%d:\n\t\t\tcode:\t%s\n\t\t\tday:\t%s\n\t\t\tlow:\t%d\n\t\t\thigh:\t%d\n\t\t\ttext:\t%s\n" % (self.number, self.code, self.day, self.metricLow, self.metricHigh, self.text)

class Forecast:

    def __init__(self, data, units):
        print(data)
        data0 = data['forecast'][0]
        data1 = data['forecast'][1]
        data2 = data['forecast'][2]
        data3 = data['forecast'][3]

        self.day0 = ForecastDay(data0, units, 0)
        self.day1 = ForecastDay(data1, units, 1)
        self.day2 = ForecastDay(data2, units, 2)
        self.day3 = ForecastDat(data3, units, 3)

    def getString(self):
        return "\tforecast:\n\t\tday0:\n%s\t\tday1:\n%s\t\tday2:\n%s\t\tday3:\n%s" % (self.day0.getString, self.day1.getString(), self.day2.getString(), self.day3.getString())
