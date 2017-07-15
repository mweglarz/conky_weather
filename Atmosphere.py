
import Utility as util


class Atmosphere:

    def __init__(self, data, units):
        self.isImperialUnits = util.isImperialUnits(units)
        self.humidity = data['humidity']
        self.pressure = data['pressure']
        self.rising = data['rising']

        if self.isImperialUnits:
            self.__transformToMetric()
        else:
            self.metricPressure = self.pressure
