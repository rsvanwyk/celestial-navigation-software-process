'''
    Assignment 8 - operation 'correct'
    
    Created on Mar 27, 2019
    
    @author: Rong Song
'''





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


    # validate 'lat' ---> extract method: isValidAngleStrFormat()
#     try:
#         # validate x: degree portion of the angle
#         degreeXstr = values['lat'].split('d')[0]
#         degreeX = int(degreeXstr)
#         
#         # validate y.y: minute portion of the angle
#         minuteYdotYstr = values['lat'].split('d')[1]
#         minuteYdotY = float(minuteYdotYstr)
#         if (minuteYdotY < 0.0 or minuteYdotY >= 60.0):
#             values['error'] = 'invalid lat'
#             return values        
#         
#         intPartYdotYstr = minuteYdotYstr.split('.')[0]        
#         fractPartYdotYstr = minuteYdotYstr.split('.')[1]
#         if (len(intPartYdotYstr) == 0 or len(fractPartYdotYstr) == 0):
#             values['error'] = 'invalid lat'
#             return values     
#     
#     except Exception:
#         values['error'] = 'invalid lat'
#         return values    
    if (not isValidAngleStrFormat(values['lat'])):
        values['error'] = 'invalid lat'
        return values



    # validate 'long'


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
    

    
    
    
    
    
    
    
    
    
    
    














