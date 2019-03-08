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



