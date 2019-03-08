'''
Created on Mar 7, 2019
assignment 7 - operation predict
@author: rs
'''


import datetime
import math


def predict(values = None):
    
    # validate mandatory information 'body'
    if (not('body' in values)):
        values['error'] = 'mandatory information is missing'
        return values
    
    starIndex = findIndexOfStar(values['body'])
    
    if (starIndex == -1):
        values['error'] = 'star not in catalog'
        return values
    
    # validate values['date']
    if ('date' in values):
        try:
            dateList = values['date'].split('-')
            year = int(dateList[0])
            month = int(dateList[1])
            day = int(dateList[2])
            if (year < 2001 or year > 2100 or month < 01 or month > 12 
                or day < 01 or day > 31):
                values['error'] = 'invalid date'
                return values
        except Exception:
            values['error'] = 'invalid date'
            return values
    
    # validate values['time']
    if ('time' in values):
        try:
            timeList = values['time'].split(':')
            hour = int(timeList[0])
            minute = int(timeList[1])
            second = int(timeList[2])
            if (hour < 0 or hour > 23 or minute < 0 or minute > 59 or second < 0 or second > 59):
                values['error'] = 'invalid time'
                return values
        except Exception:
            values['error'] = 'invalid time'
            return values
        

    # --------------------------------------
    # Perform operation predict
    # --------------------------------------
    
    # Step A. Find the angular displacement of the star relative to Aries             
    starSHA = findStarSHA(starIndex)
    starSHAdegrees = convertAngleStrToDegrees(starSHA)
    
    declinationAngle = findStarDec(starIndex)
     
    # this is the final 'lat' value
    latitude = declinationAngle
  
  
    # Step B. Calculate the ariesGHA for the date and time of the observation. 
    observAriesGHAdegrees = calculateAriesGHA(values)
   

    # Step C. Calculate the star's GHA
    # C.1 
    starGHAdegrees = observAriesGHAdegrees + starSHAdegrees    
  
    # C.2 clean up
    starGHAdegrees %= 360.0
        
    starGHA = convertDegreesToAngleStr(starGHAdegrees)

    values['long'] = starGHA
    values['lat'] = latitude  

      
    return values        
     
    
    
    

# ------------------------------------------------------
# supporting function for predict
# ------------------------------------------------------
  
def convertAngleStrToDegrees(angleStr = None): 
       
    # ---> validate angleStr to be a string in form xdy.y
    # note: doesn't work for x < 0
    
    degreePortion = int(angleStr.split('d')[0])
    minutePortion = float(angleStr.split('d')[1])
    
    degrees = degreePortion + minutePortion / 60.0
    
    return degrees
    
def convertDegreesToAngleStr(degrees = None):
    
    degreePortion = int(math.modf(degrees)[1])
    minutePortion = round(math.modf(degrees)[0] * 60.0, 1)
    
    angleStr = str(degreePortion) + 'd' + str(minutePortion)
    
    return angleStr 
    
    
def findIndexOfStar(starName = None):
    
    starsList = ['achernar',   'acrux',         'adara',     'alcaid',          'aldebaran', 
                 'alioth',     'alnair',        'alnilam',   'alphard',         'alphecca', 
                 'alpheratz',  'altair',        'ankaa',     'antares',         'arcturus', 
                 'atria',      'avior',         'bellatrix', 'betelgeuse',      'canopus', 
                 'capella',    'deneb',         'denebola',  'diphda',          'dubhe', 
                 'elnath',     'enif',          'etamin',    'fomalhaut',       'gacrux', 
                 'gienah',     'hadar',         'hamal',     'kaus australis',  'kochab', 
                 'markab',     'menkar',        'menkent',   'miaplacidus',     'mirfak', 
                 'nunki',      'peacock',       'polaris',   'pollux',          'procyon', 
                 'rasalhague', 'regulus',       'rigel',     'rigil kentaurus', 'sabik', 
                 'schedar',    'shaula',        'sirius',    'spica',           'suhail', 
                 'vega',       'zubenelgenubi']
    
    try: 
        starIndex = starsList.index(starName.lower())         
    
    except Exception:
        starIndex = -1
    
    return starIndex
    
def findStarSHA(index = None): 
       
    starsSHAlist = ['335d25.5', '173d07.2', '255d10.8', '152d57.8', '290d47.1', 
                    '166d19.4', '27d42.0',  '275d44.3', '217d54.1', '126d09.9', 
                    '357d41.7', '62d06.9',  '353d14.1', '112d24.4', '145d54.2', 
                    '107d25.2', '234d16.6', '278d29.8', '270d59.1', '263d54.8', 
                    '280d31.4', '49d30.7',  '182d31.8', '348d54.1', '193d49.4', 
                    '278d10.1', '33d45.7',  '90d45.9',  '15d22.4',  '171d58.8', 
                    '175d50.4', '148d45.5', '327d58.7', '83d41.9',  '137d21.0', 
                    '13d36.7',  '314d13.0', '148d05.6', '221d38.4', '308d37.4', 
                    '75d56.6',  '53d17.2',  '316d41.3', '243d25.2', '244d57.5', 
                    '96d05.2',  '207d41.4', '281d10.1', '139d49.6', '102d10.9', 
                    '349d38.4', '96d20.0',  '258d31.7', '158d29.5', '222d50.7', 
                    '80d38.2',  '137d03.7']

    starSHA = starsSHAlist[index]         
   
    return starSHA   
    
def findStarDec(index = None):
    
    starsDecList = ['-57d09.7', '-63d10.9', '-28d59.9', '49d13.8',  '16d32.3', 
                    '55d52.1',  '-46d53.1', '-1d11.8',  '-8d43.8',  '26d39.7', 
                    '29d10.9',  '8d54.8',   '-42d13.4', '-26d27.8', '19d06.2', 
                    '-69d03.0', '-59d33.7', '6d21.6',   '7d24.3',   '-52d42.5', 
                    '46d00.7',  '45d20.5',  '14d28.9',  '-17d54.1', '61d39.5', 
                    '28d37.1',  '9d57.0',   '51d29.3',  '-29d32.3', '-57d11.9', 
                    '-17d37.7', '-60d26.6', '23d32.3',  '-34d22.4', '74d05.2', 
                    '15d17.6',  '4d09.0',   '-36d26.6', '-69d46.9', '49d55.1',                      
                    '-26d16.4', '-56d41.0', '89d20.1',  '27d59.0',  '5d10.9', 
                    '12d33.1',  '11d53.2',  '-8d11.3',  '-60d53.6', '-15d44.4', 
                    '56d37.7',  '-37d06.6', '-16d44.3', '-11d14.5', '-43d29.8',                     
                    '38d48.1',  '-16d06.3']
    
    starDec = starsDecList[index]
    
    return starDec
    
def calculateAriesGHA(values = None):
    
    # B.1. Establish a reference angle based on a known ariesGHA.            
    baseYear = 2001
    baseMonth = 01
    baseDay = 01
    baseHour = 00
    baseMinute = 00
    baseSecond = 00
    baseAriesGHA = '100d42.6'
    baseAriesGHAdegrees = convertAngleStrToDegrees(baseAriesGHA)
     
    # B.2. Determine where the prime meridian is relative to Aries for the year of the observation            
    # B.2.a. Determine angular difference for each year
    referenceYear = baseYear
    
    if ('date' not in values):
        observYear = 2001
        observMonth = 01
        observDay = 01
    else:
        dateList = values['date'].split('-')
        observYear = int(dateList[0])
        observMonth = int(dateList[1])
        observDay = int(dateList[2])        

    yearDiff = observYear - referenceYear

    ariesGHAdecrease = '0d14.31667'
    ariesGHAdecreaseDegrees = convertAngleStrToDegrees(ariesGHAdecrease)
    
    cumProgDegrees = yearDiff * ariesGHAdecreaseDegrees
  
    # B.2.b. Take into account leap years
    leapYearNum = yearDiff % 4

    rotaPeriod = 86164.1
    clockPeriod = 86400
      
    dailyRotaDegrees = abs(360.0 - rotaPeriod / clockPeriod * 360.0 )
    
    leapProgDegrees = dailyRotaDegrees * leapYearNum
    
    # B.2.c. Calculate how far the prime meridian has rotated since the beginning of the observation year
    beginningOfObservAriesGHAdegrees = baseAriesGHAdegrees - cumProgDegrees + leapProgDegrees

    # B.2.d. Calculate the angle of the earth's rotation since the beginning of the observation year
    if ('time' not in values):
        observHour = 00
        observMinute = 00
        observSecond = 00
    else:
        timeList = values['time'].split(':')
        observHour = int(timeList[0])
        observMinute = int(timeList[1])
        observSecond = int(timeList[2])        

    observBeginningDateTime = datetime.datetime(observYear, baseMonth, baseDay,
                                                baseHour, baseMinute, baseSecond)
    observDateTime = datetime.datetime(observYear, observMonth, observDay, 
                                       observHour, observMinute, observSecond)
    totalSeconds = (observDateTime - observBeginningDateTime).total_seconds()
    
    totalRotationDegrees = totalSeconds / rotaPeriod * 360.0 
     
    rotationDegrees = math.modf(totalRotationDegrees / 360.0)[0] * 360.0
 
    # B.2.e. Calculate total
    observAriesGHAdegrees = beginningOfObservAriesGHAdegrees + rotationDegrees 
    
    return observAriesGHAdegrees    
    
    
    
    
            
