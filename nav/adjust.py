'''
Created on Feb 19, 2019

@author: rs
'''

import math

def adjust(values = None):
    
    # Validate input values
    if (not('observation' in values)):
        values['error'] = 'mandatory information is missing'
        return values
    
    if ('altitude' in values):
        values['error'] = 'altitude already exists in the input'
        return values
       
    # parse values['observation']  ---> extract to support function: parseObservation()
    degreeX = int(values['observation'].split('d')[0])
    minuteY = float(values['observation'].split('d')[1])
    if (degreeX<1 or degreeX>=90 or minuteY<0.0 or minuteY>=60.0):
        values['error'] = 'observation is invalid'
        return values   

    # parse values['height']
    if ('height' in values):
        try:
            heightValue = float(values['height']) 
        except Exception as e:
            values['error'] = 'height is invalid'    
        return values
   
  
    # ------------------------------
    # Perform operation adjust
    # ------------------------------
    
    # step 1: tested ---> extract to support function: calculateDip()
    if (values['horizon'].lower() == 'natural'):  
        heightValue = float(values['height'])          
        dip = ( -0.97 * math.sqrt( heightValue ) ) / 60
    else:
        dip = 0

    
    # step 2: tested ---> extract to support function: calculateRefraction()
    
    # parse values['observation']  ---> extract to support function: parseObservation()
    degreeX = int(values['observation'].split('d')[0])
    minuteY = float(values['observation'].split('d')[1])
    # calculate tangent of observation angle ---> extract to support function
    observationDegrees = degreeX + ( minuteY / 60.0)
    observationRadians = math.radians(observationDegrees)
    observationTan = math.tan(observationRadians)
     
    # convertToCelcius()
    temperatureF = int( values['temperature'] )
    temperatureC = (temperatureF - 32) * 5.0 / 9.0
     
    pressureValue = int( values['pressure'] )
       
    refraction = (-0.00452*pressureValue) / (273+temperatureC) / observationTan           
       

    # step 3: tested  
    altitudeDegrees = observationDegrees + dip + refraction
      
     
    # step 4:    ---> extract to support function
    # round altitude to the nearest 0.1 arc-minute
    degreePortion = int(math.modf(altitudeDegrees)[1])
    minutePortion = round(math.modf(altitudeDegrees)[0] * 60.0, 1)
    # convert altitude to a string with the format xdyy.y     
    altitudeString = str(degreePortion) + 'd' + str(minutePortion)

    # step 5
    values['altitude'] = altitudeString
    
    return values





