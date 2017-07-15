
import Utility as util


class Condition:

    def __init__(self, data, units):
        self.isImperialUnits = util.isImperialUnits(units)
        self.code = data['code']
        self.temp = int(data['temp'])
        if util.isImperialUnits(units):
            self.metricTemp = util.FtoC(self.temp)
        else:
            self.metricTemp = self.temp
        self.text = data['text']

    def getString(self):
        return " condition:\n  code: %s\n  temp: %d\n  text: %s\n" % (self.code, self.metricTemp, self.text)
