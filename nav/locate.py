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
    

    # Step B. Estimate the precision of the present position
    precisionStr = estimatePrecision(correctionsList)
    values['precision'] = precisionStr
    
    
    # Step C. Estimate accuracy of the present position
    #accuracyStr = estimateAccuracy(correctionsList)
    
    #values['accuracy'] = accuracyStr
    
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
    
    
# Step A. calculate present position (correctionsList validated)
# unit tested
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
# unit tested
def estimatePrecision(correctionsList = None):

    nsCorrectionSum = 0.0
    ewCorrectionSum = 0.0
    n = len(correctionsList)
    
    precisionSum = 0
    
    for l in correctionsList:
        crtDistanceStr = l[0]        
        crtAzimuthStr = l[1]       
        crtDistance = int(crtDistanceStr)
        crtAzimuthDegrees = convertAngleStrToDegrees(crtAzimuthStr)
        crtAzimuthRadians = crtAzimuthDegrees * math.pi / 180
        #math.radians function--->try
        
        nsCorrectionSum += crtDistance * math.cos(crtAzimuthRadians)
        ewCorrectionSum += crtDistance * math.sin(crtAzimuthRadians)
       
    nsCorrection = nsCorrectionSum / n
    ewCorrection = ewCorrectionSum / n 
        
    for l in correctionsList:
        crtDistanceStr = l[0]        
        crtAzimuthStr = l[1]       
        crtDistance = int(crtDistanceStr)
        crtAzimuthDegrees = convertAngleStrToDegrees(crtAzimuthStr)
        crtAzimuthRadians = crtAzimuthDegrees * math.pi / 180
               
        precisionSum += math.sqrt( (crtDistance*math.cos(crtAzimuthRadians)-nsCorrection)**2 + \
                                   (crtDistance*math.sin(crtAzimuthRadians)-ewCorrection)**2     )
        
    precisionInt = int(precisionSum/n)
        
    precisionStr = str(precisionInt)
    
    return precisionStr    
        
            
# Step C. Estimate accuracy of the present position
# 
def estimateAccuracy(correctionsList = None):
    
    n = len(correctionsList)
    
    if (n < 3):
        accuracyStr = 'NA'
        return accuracyStr
    
    # otherwise, determine the value of "accuracy" as follows
    
    # build points list, each point in the list is a tuple 
    pointsList = []
    for l in correctionsList:
        crtDistanceStr = l[0]        
        crtAzimuthStr = l[1]
        crtDistance = int(crtDistanceStr)
        crtAzimuthDegrees = convertAngleStrToDegrees(crtAzimuthStr)
        crtAzimuthRadians = crtAzimuthDegrees * math.pi / 180
        
        x = crtDistance * math.cos(crtAzimuthRadians)
        y = crtDistance * math.sin(crtAzimuthRadians)
        point = (x,y) 
        pointsList.append(point) 
     
    # Andrew's monotone chain convex hull algorithm:
    #    Constructs the convex hull of a set of 2-dimensional points in O(n log n) time.
    # Input: 
    #    A list of points (tuple) in the plane.
    # Precondition: 
    #    There must be at least 3 points.
    
    # 1. sort the points by x-coordinate, in case of a tie, sort by y-coordinate
    pointsList.sort()

    # 2. initialize empty lists to hold the vertices of upper and lower hulls respectively
    upper = []
    lower = []
    
     
    # calculate 2d cross product of OA and OB vectors
    #    return positive value, if OAB makes a counter-clockwise turn
    #    return negative value, if OAB makes a clockwise turn
    #    return zero, if points OAB are collinear 
    def cross(pO, pA, pB):
        return (pA[0] - pO[0]) * (pB[1] - pO[1]) - (pA[1] - pO[1]) * (pB[0] - pO[0])
        
    # 3. build the lower hull points list    
    for p in pointsList:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)    
    
    # 4. build the upper hull points list 
    for p in reversed(pointsList):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
            
    # 5. remove the last point of each list 
    #    it's the same as the first point of the other list 
    upper = upper[:-1]
    lower = lower[:-1]
    
    # 6. concatenate the upper list and the lower list to obtain the convex hull list
    #    points in the result will be listed in counter-clockwise order
    convexHullList = upper + lower 
    
    # Calculate accuracy as the area of the polygon circumscribed by convex hull list
    num = len(convexHullList)
    area = 0.0
    for i in range(num):
        j = (i+1) % num
        area += convexHullList[i][0] * convexHullList[j][1]
        area -= convexHullList[j][0] * convexHullList[i][1]
    area = abs(area) / 2.0    
    
    accuracy = int(area)
    accuracyStr = str(accuracy)     
    
    return accuracyStr
         
        


    
    





