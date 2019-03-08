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

    # check if values['body'] in stars catalog (a list of strings)   
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
    if (not(values['body'].lower() in starsList)):
        values['error'] = 'star not in catalog'
        return values
    
    # validate values['date']
    if ('date' in values):
        try:
            dateList = values['date'].split('-')
            yyyy = int(dateList[0])
            mm = int(dateList[1])
            dd = int(dateList[2])
            if (yyyy < 2001 or yyyy > 2100 or mm < 01 or mm > 12 
                or dd < 01 or dd > 31):
                values['error'] = 'invalid date'
                return values
        except Exception:
            values['error'] = 'invalid date'
            return values
        
    # if 'date' not in values, set to default '2001-01-01'
    defaultYear = 2001
    defaultMonth = 01
    defaultDay = 01
    
    # validate values['time']
    if ('time' in values):
        try:
            timeList = values['time'].split(':')
            hh = int(timeList[0])
            mm = int(timeList[1])
            ss = int(timeList[2])
            if (hh < 0 or hh > 23 or mm < 0 or mm > 59 or ss < 0 or ss > 59):
                values['error'] = 'invalid time'
                return values
        except Exception:
            values['error'] = 'invalid time'
            return values
        
    # if 'time' not in values, set to default '00:00:00'
    defaultHour = 00
    defaultMinute = 00
    defaultSecond = 00
    
    
    # --------------------------------------
    # Perform operation predict
    # --------------------------------------
    
#     # A. Find the angular displacement of the star relative to Aries.           
#     starIndex = starsList.index(values['body']) 
#     
#     starsSHAlist = ['335d25.5', '173d07.2', '255d10.8', '152d57.8', '290d47.1', 
#                     '166d19.4', '27d42.0',  '275d44.3', '217d54.1', '126d09.9', 
#                     '357d41.7', '62d06.9',  '353d14.1', '112d24.4', '145d54.2', 
#                     '107d25.2', '234d16.6', '278d29.8', '270d59.1', '263d54.8', 
#                     '280d31.4', '49d30.7',  '182d31.8', '348d54.1', '193d49.4', 
#                     '278d10.1', '33d45.7',  '90d45.9',  '15d22.4',  '171d58.8', 
#                     '175d50.4', '148d45.5', '327d58.7', '83d41.9',  '137d21.0', 
#                     '13d36.7',  '314d13.0', '148d05.6', '221d38.4', '308d37.4', 
#                     '75d56.6',  '53d17.2',  '316d41.3', '243d25.2', '244d57.5', 
#                     '96d05.2',  '207d41.4', '281d10.1', '139d49.6', '102d10.9', 
#                     '349d38.4', '96d20.0',  '258d31.7', '158d29.5', '222d50.7', 
#                     '80d38.2',  '137d03.7']
#     starSHA = starsSHAlist[starIndex]
#     starSHAdegree = starSHA.split('d')[0]
#     starSHAminute = starSHA.split('d')[1]
#     #starSHAdegrees = convertAngleToDegrees(starSHA)
#     
#     starsDecList = ['-57d09.7', '-63d10.9', '-28d59.9', '49d13.8',  '16d32.3', 
#                     '55d52.1',  '-46d53.1', '-1d11.8',  '-8d43.8',  '26d39.7', 
#                     '29d10.9',  '8d54.8',   '-42d13.4', '-26d27.8', '19d06.2', 
#                     '-69d03.0', '-59d33.7', '6d21.6',   '7d24.3',   '-52d42.5', 
#                     '46d00.7',  '45d20.5',  '14d28.9',  '-17d54.1', '61d39.5', 
#                     '28d37.1',  '9d57.0',   '51d29.3',  '-29d32.3', '-57d11.9', 
#                     '-17d37.7', '-60d26.6', '23d32.3',  '-34d22.4', '74d05.2', 
#                     '15d17.6',  '4d09.0',   '-36d26.6', '-69d46.9', '49d55.1',                      
#                     '-26d16.4', '-56d41.0', '89d20.1',  '27d59.0',  '5d10.9', 
#                     '12d33.1',  '11d53.2',  '-8d11.3',  '-60d53.6', '-15d44.4', 
#                     '56d37.7',  '-37d06.6', '-16d44.3', '-11d14.5', '-43d29.8',                     
#                     '38d48.1',  '-16d06.3']
#     declination = starsDecList[starIndex]
#     #declinationDegrees = convertAngleToDegrees(declination)
#     
#     # this is the final 'lat' value
#     latitude = declination
#     
#     
#     # B. Calculate the ariesGHA for the date and time of the observation. 
#     
#     # B.1. Establish a reference angle based on a known ariesGHA.            
#     baseYear = 2001
#     baseMonth = 01
#     baseDay = 01
#     baseHour = 00
#     baseMinute = 00
#     baseSecond = 00
#     baseAriesGHA = '100d42.6'
#     #baseAriesGHAdegrees = convertAngleToDegrees(baseAriesGHA)
#     baseAriesGHAdegree = 100
#     baseAriesGHAminute = 42.6
#     
#     # B.2. Determine where the prime meridian is relative to Aries for the year of the observation            
#     
#     # B.2.a. Determine angular difference for each year
#     refYear = baseYear
#     
#     if ('date' not in values):
#         observYear = defaultYear
#         observMonth = defaultMonth
#         observDay = defaultDay
#     else:
#         observYear = values['date'].split('-')[0]
#         observMonth = values['date'].splis('-')[1]
#         observDay = values['date'].splis('-')[2]
#         
# 
#     yearDifference = observYear - refYear
#     
#     ariesGHAchange = '-0d14.31667'
#     #ariesGHAchangeDegrees = convertAngleToDegrees(ariesGHAchange)
#     ariesGHAchangeDegree = 0
#     ariesGHAchangeMinute = -14.31667
#     
#     cumProgDegree = yearDifference * ariesGHAchangeDegree
#     cumProgMinute = yearDifference * ariesGHAchangeMinute
#     #cumProg = yearDifference * ariesGHAchangeDegrees
#     
#     # B.2.b. Take into account leap years
#     leapYearNum = yearDifference % 4
#     
#     rotaPeriod = 86164.1
#     clockPeriod = 86400
#       
#     dailyRotaDegrees = abs(360 - rotaPeriod / clockPeriod * 360 )
#     
#     leapProgDegree = dailyRotaDegrees * leapYearNum 
#     leapProgMinute = 0
#     #leapProgDegrees = dailyROtaDegrees * leapYearNum
#     
#     # B.2.c. Calculate how far the prime meridian has rotated since the beginning of the observation year.            
#     beginningOfObservAriesGHAdegree = baseAriesGHAdegree + cumProgDegree + leapProgDegree
#     beginningOfObservAriesGHAminute = baseAriesGHAminute + cumProgMinute + leapProgMinute
#     #beginningOfObservAriesGHAdegrees = baseAriesGHAdegrees + cumProg + leapProgDegrees
#     
#     # B.2.d.
#     if ('time' not in values):
#         observHour = defaultHour
#         observMinute = defaultMinute
#         observSecond = defaultSecond
#     else:
#         observHour = values['time'].split(':')[0]
#         observMinute = values['time'].splis(':')[1]
#         observSecond = values['time'].splis(':')[2]    
#     
#     observBeginningDateTime = datetime.datetime(observYear, baseMonth, baseDay, 
#                                                 baseHour, baseMinute, baseSecond)
#     observDateTime = datetime.datetime(observYear, observMonth, observDay, 
#                                        observHour, observMinute, observSecond)
#     totalSeconds = (observDateTime - observBeginningDateTime).total_seconds()
#     
#     totalRotation = totalSeconds / rotaPeriod * 360 
#      
#     rotation = math.modf(totalRotation / 360)[0] * 360
#     rotationDegree = math.modf(rotation)[1]
#     rotationMinute = round(math.modf(rotation)[0] * 60.0, 1)
#     
#     # B.2.e. Calculate total
#     observAriesGHAdegree = beginningOfObservAriesGHAdegree + rotationDegree
#     observAriesGHAminute = beginningOfObservAriesGHAminute + rotationMinute
#     # need to adjust minute part to degree part
#     
#     # C.  Calculate the star's GHA
#     # C.1
#     starGHAdegree = observAriesGHAdegree + starSHAdegree
#     starGHAminute = observAriesGHAminute + starSHAminute
#     
#     # C.2 clean up
#     starGHAdegree = starGHAdegree + int(math.modf(starGHAminute/60)[1]) 
#     starGHAminute = round(starGHAminute % 60.0, 1)
#      
# 
#     starGHA = str(starGHAdegree) + 'd' + str(starGHAminute)     
#      
#      
#     values['long'] = starGHA
#     values['lat'] = latitude  
#      
#     return values        
#     
    
    
    
