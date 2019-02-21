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
    # parse values['observation']  
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
    
    # step 1 ---> extract to support function: calculateDip()
    if (values['horizon'].lower() == 'natural'):  
        heightValue = float(values['height'])          
        dip = ( -0.97 * math.sqrt( heightValue ) ) / 60
    else:
        dip = 0

    
    # step 2
    
    # • refraction=(-0.00452*pressure) / (273+convert_to_celsius(temperature))/tangent(observation)            
    
    #refraction = (-0.00452*values["pressure"]) / ( 273+convertToCelsius(values["temperature"])) / tangent(values["observation"])            
    #---> support function: tangent(obervation)    

      
    
    #return values





