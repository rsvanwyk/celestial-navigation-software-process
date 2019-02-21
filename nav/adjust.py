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
    
    
# --------> to pass 920 ??? should pass -------------  
#     if ('altitude' in values):
#         values['error'] = 'altitude already exists in the input'
#         return values
       
       
# -------->to pass 930 ??? same problem with 920 assertTrue ------------
    # parse values['observation']  ---> extract to support function: parseObservation()
#     degreeX = int(values['observation'].split('d')[0])
#     minuteY = float(values['observation'].split('d')[1])
#     if (degreeX<1 or degreeX>=90 or minuteY<0.0 or minuteY>=60.0):
#         values['error'] = 'observation is invalid'
#         return values   


# -------->to pass 940, production code not finish --------------
    # parse values['height']
#     if ('height' in values):
#         heightValue = values['height'] 
#
#         return values
  
  
    # ------------------------------
    # Perform operation adjust
    # ------------------------------
    
    # step 1: tested ---> extract to support function: calculateDip()
#     if (values['horizon'].lower() == 'natural'):  
#         heightValue = float(values['height'])          
#         dip = ( -0.97 * math.sqrt( heightValue ) ) / 60
#     else:
#         dip = 0

    
    
    # step 2: tested ---> extract to support function: calculateRefraction()
    
#     # parse values['observation']  ---> extract to support function: parseObservation()
#     degreeX = int(values['observation'].split('d')[0])
#     minuteY = float(values['observation'].split('d')[1])
#     # calculate tangent of observation angle ---> extract to support function
#     angleDegrees = degreeX + ( minuteY / 60.0)
#     angleRadians = math.radians(angleDegrees)
#     tanObservation = math.tan(angleRadians)
#     
#     # convertToCelcius()
#     temperatureF = int( values['temperature'] )
#     temperatureC = (temperatureF - 32) * 5.0 / 9.0
#     
#     pressureValue = int( values['pressure'] )
#       
#     refraction = (-0.00452*pressureValue) / (273+temperatureC) / tanObservation           
       

      
    # step 3:  
      
      
      
      
      
      
    
    return values





