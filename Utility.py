


def isImperialUnits(units):
    return units['temperature'] == 'F'

def mphToKph(value):
    speedToMetric = 1.609344
    return value * speedToMetric

def FtoC(value):
    return (value - 32.0) * (5.0/9.0)

# inches Hg to hPa
def InTohPa(value):
    # inches Hg to milibars
    value = float(value)
    iTb = 33.8637526
    mb = value * iTb
    # mb == hPa
    return mb
