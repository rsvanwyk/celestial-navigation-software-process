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
        values['error'] = 'assumedLat is missing'
        return values
    if (not("assumedLong") in values):
        values['error'] = 'assumedLong is missing'
        return values
    if (not("corrections") in values):
        values['error'] = 'corrections is missing'
        return values
    
    # validate 'assumedLat'
    if (not isValidAngleStrFormat(values['assumedLat'])):
        values['error'] = 'invalid assumedLat'
        return values
    assumedLatDegrees = convertAngleStrToDegrees(values['assumedLat'])
    if (assumedLatDegrees <= -90.0 or assumedLatDegrees >= 90.0):
        values['error'] = 'invalid assumedLat'
        return values
    
    # validate 'assumedLong'
    if (not isValidAngleStrFormat(values['assumedLong'])):
        values['error'] = 'invalid assumedLong'
        return values    
    assumedLongDegrees = convertAngleStrToDegrees(values['assumedLong'])
    if (assumedLongDegrees < 0.0 or assumedLongDegrees >= 360.0):
        values['error'] = 'invalid assumedLong'
        return values     
    
    
    # convert 'corrections' string to list of lists
    correctionsStr = values['corrections']
    correctionsList = parseCorrections(correctionsStr)
    
    # check for empty list
    if (correctionsList[0][0] == ''):
        values['error'] = 'corrections can not be empty'
        return values
    
    # check for invalid corrected distance
    try:
        for l in correctionsList:
            crtDistance = int(l[0])
            if (crtDistance <= 0):
                values['error'] = 'invalid corrections'
    except Exception:
        values['error'] = 'invalid corrections'
        return values  
    
    
    
    
# -------------------------------
# supporting functions
# -------------------------------

# convert corrections string to corrections list
def parseCorrections(correctionsStr = None):
    
    list1 = correctionsStr.replace('[', '').split('],')
    
    # list2 is a list of strings, each string represents one set of correction data    
    list2 = [s.replace(']', '') for s in list1]
    
    # correctionsList is a list of lists, each list consists of two string elements
    # the first string element represents corrected distance
    # the second string element represents corrected azimuth 
    correctionsList = [s.split(',') for s in list2]
    
    return correctionsList
    
    

        
    




    
    





