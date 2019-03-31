'''
    Assignment 8 - operation 'correct'
    
    Created on Mar 27, 2019
    
    @author: Rong Song
'''





def correct(values = None):
    
    # validate mandatory element 'lat'
    if (not('lat') in values):
        values['error'] = 'mandatory information is missing'
        return values
    
    # validate mandatory element 'long'
    if (not('long') in values):
        values['error'] = 'mandatory information is missing'
        return values

    # validate mandatory element 'altitude'
    if (not('altitude') in values):
        values['error'] = 'mandatory information is missing'
        return values

    # validate mandatory element 'assumedLat'
    if (not('assumedLat') in values):
        values['error'] = 'mandatory information is missing'
        return values

    # validate mandatory element 'assumedLong'
    if (not('assumedLong') in values):
        values['error'] = 'mandatory information is missing'
        return values











