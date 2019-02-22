'''
Created on Feb 16, 2019

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
            if (heightValue<0.0):
                values['error'] = 'height is invalid'    
                return values
        except Exception:
            values['error'] = 'height is invalid'    
            return values
   
    # parse values['horizon']
    if ('horizon' in values):
        try:
            horizonValue = values['horizon'].lower()
            if (horizonValue != 'natural' and horizonValue != 'artificial'):
                values['error'] = 'horizon is invalid'
                return values
        except Exception:
            values['error'] = 'horizon is invalid'
            return values
         
    # parse values['temperature']
    if ('temperature' in values):
        try:
            temperatureF = int(values['temperature'])
            if (temperatureF<-20 or temperatureF>120):
                values['error'] = 'temperature is invalid'
                return values
        except Exception:
            values['error'] = 'temperature is invalid'
            return values
                
    # parse values['pressure']
    if ('pressure' in values):
        try:
            pressureValue = int(values['pressure'])
            if (pressureValue<100 or pressureValue>1100):
                values['error'] = 'pressure is invalid'
                return values
        except Exception:
            values['error'] = 'pressure is invalid'
            return values
        
         
                
    # -----------------------------
    # Perform operation adjust
    # ------------------------------
    
    # step 1: tested ---> extract to support function: calculateDip()
    if (not('horizon' in values)):
        horizonValue = 'natural'
    else:
        horizonValue = values['horizon'].lower()  
    
    if (horizonValue == 'natural'): 
        if (not('height' in values)):
            heightValue = 0
        else: 
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
    if (not('temperature' in values)):
        temperatureF = 72
    else:
        temperatureF = int( values['temperature'] )
    temperatureC = (temperatureF - 32) * 5.0 / 9.0
    
    if (not('pressure' in values)):
        pressureValue = 1010
    else: 
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





