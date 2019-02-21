'''
Created on Feb 19, 2019

@author: rs
'''



def adjust(values = None):
    
    # Validate input values
    if (not('observation' in values)):
        values['error'] = 'mandatory information is missing'
    elif ('altitude' in values):
        values['error'] = 'altitude already exists in the input'
    
    # function to parse values['observation']     
    #  
    
    return values





