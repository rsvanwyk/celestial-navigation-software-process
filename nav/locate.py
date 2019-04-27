'''
    Assignment 10 - operation 'locate'
    
    Created on Apr 26, 2019

    @author: Rong Song
'''



def locate(values = None):
    
    # check if mandatory elements exist in input values
    if (not("assumedLat") in values):
        values['error'] = 'mandatory information is missing'
        return values
    if (not("assumedLong") in values):
        values['error'] = 'mandatory information is missing'
        return values
    if (not("corrections") in values):
        values['error'] = 'mandatory information is missing'
        return values
    
    





