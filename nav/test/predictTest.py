'''
Created on Mar 5, 2019
tests for predict()
@author: rs
'''
import unittest
from pip._internal.utils.outdated import SELFCHECK_DATE_FMT
#import nav.predict as nav
#import math

class predictTest(unittest.TestCase):


    def setUp(self):
        self.inputDictionary = {'op':'predict'}
        self.errorKey = "error"
        self.errorValue = "diagnostic msg"
        self.solutionKey1 = "long"
        self.solutionKey2 = "lat"

    def tearDown(self):
        self.inputDictionary = {}


    def setParm(self, key, value):
        self.inputDictionary[key] = value
        
        
        
    # ----------------------------------------------------------
    # Acceptance Tests -----> add tests for dispatchTest.py
    # ----------------------------------------------------------
    # 300 predict operation
    #     Desired level of confidence: boundary value analysis
    #     Input Analysis
    #         values: mandatory
    #                 python dictionary
    #                 elements: 
    #                     'op':'predict', validated
    #                     'body': unvalidated, mandatory, case-independent string,
    #                             match the name of one of the navigable stars 
    #                     'date': unvalidated, optional, string, yyyy-mm-dd format,
    #                             defaults to "2001-01-01" if missing
    #                         yyyy: .GE.2001 and .LE.2100 
    #                         mm,dd: two digit integers follow conventional rules
    #                             
    #                     'time': unvalidated, optional, string, hh:mm:ss format,
    #                             defaults to "00:00:00" if missing
    #                         hh,mm,ss: two digit integers follow conventional rules
    #
    # Happy path analysis:
    #     010    nominal input values
    #     020    optional elements missing, set to default
    #     025    
    #     030    input extra elements, ignore
    #     040    boundary values for 'date'
    #     050    boundary values for 'time'
    #     060    'long' and/or 'lat' already exist in the input values
    #
    #
    # Sad path analysis:
    #     910    missing mandatory information 'body' 
    #     920    invalid 'body'
    #     930    invalid 'date'
    #     940    invalid 'time'
    #
    #
    #
    # Happy path tests
    
     

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        


