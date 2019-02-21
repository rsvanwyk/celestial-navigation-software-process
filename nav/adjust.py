'''
Created on Feb 19, 2019

@author: rs
'''



def adjust(values = None):
    
    values = {'op':'adjust'}
    if (not('observation' in values)):
        values['error'] = 'mandatory information is missing'
        
        
    
    
    return values