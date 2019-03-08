'''
Created on Mar 7, 2019
assignment 7 - operation predict
@author: rs
'''


def predict(values = None):
    
    # validate input values
    if (not('body' in values)):
        values['error'] = 'mandatory information is missing'
        return values

    
    # check if values['body'] in stars catalog (list of strings)   
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
    

    
    
    
    
    
    
    
    
