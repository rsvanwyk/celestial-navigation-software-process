'''
Created on Feb 19, 2019

@author: rs
'''



def adjust(values = None):
    
    # Validate input values
    if (not('observation' in values)):
        values['error'] = 'mandatory information is missing'
    if ('altitude' in values):
        values['error'] = 'altitude already exists in the input'
    
    # parse values['observation']   
# test200_930  
#     degreeX = int(values['observation'].split('d')[0])
#     minuteY = float(values['observation'].split('d')[1])
#     if (degreeX<1 or degreeX>=90 or minuteY<0.0 or minuteY>=60.0):
#         values['error'] = 'observation is invalid'
      
    
    return values





