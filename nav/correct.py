'''
    Assignment 8 - operation 'correct'
    
    Created on Mar 27, 2019
    
    @author: Rong Song
'''

from nav.adjust import convertAngleStrToDegrees
import math
from nav.predict import convertDegreesToAngleStr


def correct(values = None):
    
    # check if mandatory elements exist in input values
    if (not('lat') in values):
        values['error'] = 'mandatory information is missing'
        return values
    
    if (not('long') in values):
        values['error'] = 'mandatory information is missing'
        return values
  
    if (not('altitude') in values):
        values['error'] = 'mandatory information is missing'
        return values
  
    if (not('assumedLat') in values):
        values['error'] = 'mandatory information is missing'
        return values
  
    if (not('assumedLong') in values):
        values['error'] = 'mandatory information is missing'
        return values


    # validate 'lat'   
    if (not isValidAngleStrFormat(values['lat'])):
        values['error'] = 'invalid lat'
        return values
    
    latDegrees = convertAngleStrToDegrees(values['lat'])
    if (latDegrees <= -90.0 or latDegrees >= 90.0):
        values['error'] = 'invalid lat'
        return values        

    # validate 'long'
    if (not isValidAngleStrFormat(values['long'])):
        values['error'] = 'invalid long'
        return values

    longDegrees = convertAngleStrToDegrees(values['long'])
    if (longDegrees < 0.0 or longDegrees >= 360.0):
        values['error'] = 'invalid long'
        return values        

    # validate 'altitude'
    if (not isValidAngleStrFormat(values['altitude'])):
        values['error'] = 'invalid altitude'
        return values    

    altitudeDegrees = convertAngleStrToDegrees(values['altitude'])
    if (altitudeDegrees <= 0.0 or altitudeDegrees >= 90.0):
        values['error'] = 'invalid altitude'
        return values    

    # validate 'assumedLat'
    if (not isValidAngleStrFormat(values['assumedLat'])):
        values['error'] = 'invalid assumedLat'
        return values    

    assumedLatDegrees = convertAngleStrToDegrees(values['assumedLat'])
    if (assumedLatDegrees <= -90.0 or assumedLatDegrees >= 90.0):
        values['error'] = 'invalid assumedLat'
        return values 

    # validate 'assumedLong'
    if (not isValidAngleStrFormat(values['assumedLong'])):
        values['error'] = 'invalid assumedLong'
        return values    

    assumedLongDegrees = convertAngleStrToDegrees(values['assumedLong'])
    if (assumedLongDegrees < 0.0 or assumedLongDegrees >= 360.0):
        values['error'] = 'invalid assumedLong'
        return values 


    # --------------------------------------
    # Perform operation correct
    # --------------------------------------

    # step A. Calculate the local hour angle of the navigator
    lhaDegrees = longDegrees + assumedLongDegrees

    # step B. ---> ? extract method calcCorrectedAltitude()
    latRadians = latDegrees * math.pi / 180
    assumedLatRadians = assumedLatDegrees * math.pi / 180
    lhaRadians = lhaDegrees * math.pi / 180
    
    intermediateDistance = (math.sin(latRadians) * math.sin(assumedLatRadians)) + \
        (math.cos(latRadians) * math.cos(assumedLatRadians) * math.cos(lhaRadians))
                                              
    correctedAltitudeRadians = math.asin(intermediateDistance)
    
    correctedAltitudeDegrees = correctedAltitudeRadians * 180 / math.pi
     
    
    # step C. Calculate correctedDistance in arc-minutes and round to the nearest 1 arc-minute
    correctedDistance = (altitudeDegrees - correctedAltitudeDegrees) * 60
    correctedDistance = int(round(correctedDistance))
    
    # step D. 
    correctedAzimuthRadians = math.acos(
        (math.sin(latRadians) - (math.sin(assumedLatRadians) * intermediateDistance))/
        (math.cos(assumedLatRadians) * math.cos(correctedAltitudeRadians))
        )
    correctedAzimuthDegrees = correctedAzimuthRadians * 180 / math.pi
    
    # step E. normalize if
    if (correctedDistance < 0):
        correctedDistance = int(math.fabs(correctedDistance))
        correctedAzimuthDegrees = (correctedAzimuthDegrees + 180) % 360
    
    # step F. 
    correctedAzimuthStr = convertDegreesToAngleStr(correctedAzimuthDegrees)
    values['correctedAzimuth'] = correctedAzimuthStr
    values['correctedDistance'] = str(correctedDistance)
    
    return values



# ------------------------------------------------------
# supporting functions
# ------------------------------------------------------
def isValidAngleStrFormat(angleStr = None):     
    try:
        # validate x: degree portion of the angle
        degreeXstr = angleStr.split('d')[0]
        int(degreeXstr)
        
        # validate y.y: minute portion of the angle
        minuteYdotYstr = angleStr.split('d')[1]
        minuteYdotY = float(minuteYdotYstr)
        if (minuteYdotY < 0.0 or minuteYdotY >= 60.0):
            return False
        
        intPartYdotYstr = minuteYdotYstr.split('.')[0]        
        fractPartYdotYstr = minuteYdotYstr.split('.')[1]
        if (len(intPartYdotYstr) == 0 or len(fractPartYdotYstr) == 0):
            return False
    
        return True
    
    except Exception:
        return False    
    

    
    
    
    
    
    
    
    
    
    
    














