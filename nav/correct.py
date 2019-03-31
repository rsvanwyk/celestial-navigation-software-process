'''
    Assignment 8 - operation 'correct'
    
    Created on Mar 27, 2019
    
    @author: Rong Song
'''





def correct(values = None):
    
    # check if mandatory elements exist in input values
    if (not('lat') in values):
        values['error'] = 'mandatory information is missing'
        return values
    
    if (not('long') in values):
        values['error'] = 'mandatory information is missing'
        return values

    if (not('altitude') in values):
        values['error'] = 'mandatory information is missing'
        return values

    if (not('assumedLat') in values):
        values['error'] = 'mandatory information is missing'
        return values

    if (not('assumedLong') in values):
        values['error'] = 'mandatory information is missing'
        return values


    # validate 








