'''
Created on Mar 7, 2019
assignment 7 - operation predict
@author: rs
'''


def predict(values = None):
    
    # validate mandatory information 'body'
    if (not('body' in values)):
        values['error'] = 'mandatory information is missing'
        return values

    # check if values['body'] in stars catalog (a list of strings)   
    stars = ['achernar',   'acrux',         'adara',     'alcaid',          'aldebaran', 
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
    if (not(values['body'].lower() in stars)):
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
        
    # if date not in values, set to default '2001-01-01'
    yyyy = 2001
    mm = 01
    dd = 01
    
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
        
    # if time not in values, set to default '00:00:00'
    hh = 00
    mm = 00
    ss = 00
    
    
    
    
    
    
    
    
    
    
