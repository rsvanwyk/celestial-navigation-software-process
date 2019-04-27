'''
    Assignment 10 - operation 'locate'
    
    Created on Apr 26, 2019

    @author: Rong Song
'''

from nav.correct import isValidAngleStrFormat
from nav.adjust import convertAngleStrToDegrees



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
    
    # validate 'assumedLat'
    if (not isValidAngleStrFormat(values['assumedLat'])):
        values['error'] = 'invalid assumedLat'
        return values
#     assumedLatDegrees = convertAngleStrToDegrees(values['assumedLat'])
#     if (assumedLatDegrees <= -90.0 or assumedLatDegrees >= 90.0):
#         values['error'] = 'invalid assumedLat'
#         return values
    
    
    
    
    
    
    
    
    
    
    
    
    





