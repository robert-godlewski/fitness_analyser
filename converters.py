# This is a group of functions that do a number of calculation conversions
# Converts binary data to a floating point number
def binaryToFloat(bin) -> float:
    if bin == b'':
        return -1.0
    else:
        return float(bin)

# Converts binary data to a string
def binaryToString(bin) -> str:
    return str(bin, 'utf-8')

def metersToInch(meters: float) -> float:
    return 39.37*meters

def inchesToMeters(inches: float) -> float:
    return inches/39.37

def poundsToKilograms(lbs: float) -> float:
    return lbs/2.205

def kilogramsToPounds(kg: float) -> float:
    return 2.205*kg

def bodyFatPercentage(height: float, waist: float, is_metric: bool) -> float:
    if is_metric:
        height = metersToInch(height)
        waist = metersToInch(waist)
    return waist/height

def bmiCalc(weight: float, height: float, is_metric: bool) -> float:
    if not is_metric:
        weight = poundsToKilograms(weight)
        height = inchesToMeters(height)
    return weight / (height**2)

def waistHipRatio(waist: float, hip: float, is_metric: bool) -> float:
    if is_metric:
        waist = metersToInch(waist)
        hip = metersToInch(hip)
    return waist/hip