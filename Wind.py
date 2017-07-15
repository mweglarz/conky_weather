import Utility as util

class Wind:

    def __init__(self, wind, units):
        self.isImperialUnits = util.isImperialUnits(units)
        self.chill = int(wind['chill'])
        self.direction = int(wind['direction'])
        self.speed = int(wind['speed'])
        if self.isImperialUnits:
            self.__transformUnitsToMetric()
        else:
            self.metricChill = self.chill
            self.metricDirection = self.direction
            self.metricSpeed = self.speed

    def getString(self):
        return " wind:\n  chill: %d\n  direction: %d\n  speed: %d\n" % (self.metricChill, self.metricDirection, self.metricSpeed)

    def __transformUnitsToMetric(self):
        speedToMetric = 1.609344
        self.metricSpeed = int(util.mphToKph(self.speed))
        self.metricChill = int(util.FtoC(self.chill))
        self.metricDirection = self.direction
