'''
    Assignment 10 - operation 'locate'
    
    Created on Apr 26, 2019

    @author: Rong Song
'''

from nav.correct import isValidAngleStrFormat
from nav.adjust import convertAngleStrToDegrees
import math
from nav.predict import convertDegreesToAngleStr


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
    
    
    # convert 'corrections' string to list of lists and validate
    correctionsStr = values['corrections']
    correctionsList = parseCorrections(correctionsStr)
    
    # validate: check for empty list
    if (correctionsList[0][0] == ''):
        values['error'] = 'corrections can not be empty'
        return values
    
    # validate: check for invalid corrected distance
    try:
        for l in correctionsList:
            crtDistanceStr = l[0]
            crtDistance = int(crtDistanceStr)
            if (crtDistance <= 0):
                values['error'] = 'invalid corrections'
                return values
    except Exception:
        values['error'] = 'invalid corrections'
        return values  
    
    # validate: check for invalid corrected azimuth
    for l in correctionsList:
        crtAzimuthStr = l[1]
        if (not isValidAngleStrFormat(crtAzimuthStr)):
            values['error'] = "invalid corrections"
            return values
        crtAzimuthDegrees = convertAngleStrToDegrees(crtAzimuthStr)
        if (crtAzimuthDegrees < 0.0 or crtAzimuthDegrees >= 360.0):
            values['error'] = "invalid corrections"    
    
    
    
    # -----------------------------
    # Perform operation locate
    # -----------------------------
    
    # Step A. Calculate the present position
    presentPositionList = calcPresentPosition(correctionsList, assumedLatDegrees, assumedLongDegrees)
    presentLatStr = presentPositionList[0]
    presentLongStr = presentPositionList[1]
    
    values['presentLat'] = presentLatStr
    values['presentLong'] = presentLongStr
    

    # Step B. Estimate the precision
    
    
    return values
    
    
    # Step C.
    
    
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
    
    
# Step A. calculate present position (correctionsList validated)
def calcPresentPosition(correctionsList = None, assumedLatDegrees = None, assumedLongDegrees = None):
    
    nsCorrectionSum = 0.0
    ewCorrectionSum = 0.0
    n = len(correctionsList)
    
    for l in correctionsList:
        crtDistanceStr = l[0]        
        crtAzimuthStr = l[1]
        
        crtDistance = int(crtDistanceStr)
        crtAzimuthDegrees = convertAngleStrToDegrees(crtAzimuthStr)
        crtAzimuthRadians = crtAzimuthDegrees * math.pi / 180
        
        nsCorrectionSum += crtDistance * math.cos(crtAzimuthRadians)
        ewCorrectionSum += crtDistance * math.sin(crtAzimuthRadians)
       
        nsCorrection = nsCorrectionSum / n
        ewCorrection = ewCorrectionSum / n 
        
    presentLatDegrees = assumedLatDegrees + nsCorrection / 60
    presentLongDegrees = assumedLongDegrees + ewCorrection / 60
    
    presentLatStr = convertDegreesToAngleStr(presentLatDegrees)
    presentLongStr = convertDegreesToAngleStr(presentLongDegrees)
    
    presentPositionList = [presentLatStr, presentLongStr]
    
    return presentPositionList    
        
        
# Step B. Estimate the precision of the present position
def estimatePrecision(correctionsList = None):
    pass        
         
        


    
    





