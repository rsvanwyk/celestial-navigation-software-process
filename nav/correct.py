'''
    Assignment 8 - operation 'correct'
    
    Created on Mar 27, 2019
    
    @author: Rong Song
'''
from nav.adjust import convertAngleStrToDegrees





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
    

    
    
    
    
    
    
    
    
    
    
    














