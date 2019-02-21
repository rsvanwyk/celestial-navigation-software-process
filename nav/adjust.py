'''
Created on Feb 19, 2019

@author: rs
'''



def adjust(values = None):
    
    # Validate input values
    if (not('observation' in values)):
        values['error'] = 'mandatory information is missing'
        return values
    
# --------> to pass 920 ??? should pass   
#    if ('altitude' in values):
#        values['error'] = 'altitude already exists in the input'
    
       
# -------->to pass 930 ??? should pass, same problem with 920 assertTrue
    # parse values['observation']  
#     degreeX = int(values['observation'].split('d')[0])
#     minuteY = float(values['observation'].split('d')[1])
#     if (degreeX<1 or degreeX>=90 or minuteY<0.0 or minuteY>=60.0):
#         values['error'] = 'observation is invalid'
     

# -------->to pass 940, implement not finished...
    # parse values['height']
#     if ('height' in values):
#         heightValue = values['height'] 
      
  
  
    # ------------------------------
    # Perform operation adjust
    # ------------------------------
    
    # step 1
#     if (values["horizon"].lower() == "natural"):
#         dip = ( -0.97 * math.sqrt(values["height"]) ) / 60
#     else:
#         dip = 0

    
      
    
    #return values





