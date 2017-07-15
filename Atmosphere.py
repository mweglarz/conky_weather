
import Utility as util


class Atmosphere:

    def __init__(self, data, units):
        self.isImperialUnits = util.isImperialUnits(units)
        self.humidity = int(data['humidity'])
        self.pressure = float(data['pressure'])
        self.rising = data['rising']

        if self.isImperialUnits:
            self.__transformToMetric()
        else:
            self.metricPressure = self.pressure

    def getString(self):
        return " atmosphere:\n  humidity: %d\n  pressure: %.1f\n  rising: %s\n" % (self.humidity, self.metricPressure, self.rising)

    def __transformToMetric(self):
        self.metricPressure = util.InTohPa(self.pressure)
        self.metricPressure = self.pressure
