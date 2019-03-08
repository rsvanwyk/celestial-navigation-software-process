'''
Created on Mar 5, 2019
assignment 7 - tests for predict()
@author: rs
'''


import unittest
import nav.predict as nav
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
        
            
    # -----------------------------------------------------------------
    # Acceptance Tests -----> add tests to dispatchTest.py and modify
    # -----------------------------------------------------------------
    # 300 predict operation
    #     
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
    #     300_010    nominal input values
    #     300_020    optional element 'date' missing, set to default
    #     300_025    optional element 'time' missing, set to default
    #     300_030    input extra elements, ignore
    #     300_040    'long' and/or 'lat' already exist in the input values
    #
    #
    # Sad path analysis:
    #     300_910    missing mandatory element 'body' 
    #     300_920    invalid 'body'
    #     300_930    invalid 'date'
    #     300_940    invalid 'time'
    #
    #
    #
    # Happy path tests
    def test300_010NominalInputValuesReturnValuesWithLongAndLat(self):
        self.setParm('body', 'Aldebaran')
        self.setParm('date', '2016-01-17')
        self.setParm('time', '03:15:42')
        resultDict = nav.predict(self.inputDictionary)
        expectedResultDict = {'op':'predict', 
                              'body': 'Aldebaran', 
                              'date': '2016-01-17', 
                              'time': '03:15:42', 
                              'long':'95d41.6', 
                              'lat':'16d32.3'}    
        self.assertDictEqual(resultDict, expectedResultDict)
    
    def test300_020OptionalElementDateMissingSetToDefault(self):
        self.setParm('body', 'Betelgeuse')
        self.setParm('time', '03:15:42')
        resultDict = nav.predict(self.inputDictionary)
        expectedResultDict = {'op':'predict', 
                              'body': 'Betelgeuse', 
                              'time': '03:15:42', 
                              'long':'60d45.2', 
                              'lat':'7d24.3'}  
        self.assertDictEqual(resultDict, expectedResultDict)        
#     
#     def test300_030OptionalElementTimeMissingSetToDefault(self):
#         pass
#     
#     def test300_040IgnoreExtraInputElements(self):
#         pass
#     
#     def test300_050LongAlreadyExistReturnValuesOverride(self):
#         pass
    
    
    
    
    
    
    # Sad path tests
    def test300_910MissingMandatoryInfoReturnValuesWithErrorKey(self):
        resultDict = nav.predict(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'mandatory information is missing')
    
    def test300_920InvalidBodyReturnValuesWithErrorKey(self): 
        self.setParm('body', 'unknown')
        self.setParm('date', '2016-01-17')
        self.setParm('time', '03:15:42')
        resultDict = nav.predict(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'star not in catalog')
    
    def test300_930InvalidDateReturnValuesWithErrorKey(self): 
        self.setParm('body', 'Betelgeuse')
        self.setParm('date', '2016-99-17')
        self.setParm('time', '03:15:42')
        resultDict = nav.predict(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'invalid date')
    
    def test300_940InvalidTimeReturnValuesWithErrorKey(self): 
        self.setParm('body', 'Betelgeuse')
        self.setParm('date', '2016-01-17')
        self.setParm('time', '03:15:99')
        resultDict = nav.predict(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'invalid time')    
    
    
    
    
    
# ----------------------------------------------------------------
# unit tests for supporting functions of 'predict' operation    
# ---------> DELETE after unit tests done -------------------
    def test300_310convertAngleStrToDegreesTest(self):
        angle = '0d14.31667'
        degrees = nav.convertAngleStrToDegrees(angle)
        
        expectedDegrees = 0.2386
        
        self.assertAlmostEqual(degrees, expectedDegrees, places = 3)
        
        
    
    def test300_320convertDegreesToAngleStrTest(self):
        degrees = 290.785
        angle = nav.convertDegreesToAngleStr(degrees)
        
        expectedAngle = '290d47.1'
    
        self.assertAlmostEqual(angle, expectedAngle, places = 3)
    
    
    
    
        


