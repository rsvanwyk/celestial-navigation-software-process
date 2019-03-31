'''
    Assignment 8 - tests for operation 'correct'
    
    Created on Mar 27, 2019
    
    @author: Rong Song
'''

import unittest
import nav.correct as nav


class correctTest(unittest.TestCase):


    def setUp(self):
        self.inputDictionary = {'op':'correct'}
        self.errorKey = "error"
        self.errorValue = "diagnostic msg"
        self.solutionKey1 = "correctedDistance"
        self.solutionKey2 = "correctedAzimuth"


    def tearDown(self):
        self.inputDictionary = {}


    def setParm(self, key, value):
        self.inputDictionary[key] = value


    # ---------------------------------------------------------------------------------
    # Acceptance Tests -----> add correspondent tests to dispatchTest.py and modify
    # ---------------------------------------------------------------------------------
    # 400 correct operation
    #     
    #     Input Analysis
    #         values: mandatory
    #                 python dictionary
    #                 elements:  
    #                     'op':'correct', validated
    #
    #                     'lat': unvalidated, mandatory, obtained from 'predict' op, 
    #                            angle in the range .GT.-90d0.0 and .LT.90d0.0
    #                     'long': unvalidated, mandatory, obtained from 'predict' op,
    #                             angle in the range .GE.0d0.0 and .LT.360d0.0
    #                     'altitude': unvalidated, mandatory, obtained from 'adjust' op,
    #                                 angle in the range .GT.0d0.0 and .LT.90d0.0
    #                     'assumedLat': unvalidated, mandatory, estimated latitude of the navigator,
    #                                   angle in the range .GT. -90d0.0 and .LT.90d0.0 
    #                     'assumedLong': unvalidated, mandatory, estimated longitude of the navigator,
    #                                    angle in the range .GE.0d0.0 and .LT.360d0.0
    #                 Note 1: all angles are strings in format xdy.y: 
    #                     x: degree portion, int value may have leading zeros
    #                     d: char 'd' to separate degrees from minutes
    #                     y.y: minute portion, positive floating point value in the range .GE. 0.0 and .LT. 60.0,
    #                          with at least one digit on either side of the decimal point, may have leading zeros.
    #
    #
    # Happy path analysis:
    #     400_010    nominal input values
    #     400_020    input extra elements, ignore
    #     400_030    'long' degree portion x has leading zero
    #     400_040    boundary values for --->
    #
    # Sad path analysis:
    #     400_910    missing all mandatory elements
    #     400_915    missing mandatory 'lat'
    #     400_920    invalid 'lat' (degree portion x not int: '16.0d32.3') 
    #     400_925    invalid 'lat' (minute portion y.y out of range: '16d60.0')
    #     400_930    invalid 'long' (not in the form 'xdy.y': '95.41.6) 
    #     400_940    invalid 'altitude'
    #     400_950    invalid 'assumedLat' (out of range: '-153d38.4')
    #     400_960    invalid 'assumedLong'
    #
    #
    # Happy path tests





    # Sad path tests
    def test400_910MissingAllMandatoryInfoReturnValuesWithErrorKey(self):
        resultDict = nav.correct(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'mandatory information is missing')   
    
    def test400_915MissingMandatoryInfoReturnValueWithErrorKey(self):
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '-53d38.4')
        self.setParm('assumedLong', ' 74d35.3')
        resultDict = nav.correct(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'mandatory information is missing')   
        
    def test400_920InvalidLatXnotIntReturnValueWithErrorKey(self):
        self.setParm('lat', '16.0d32.3')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '-53d38.4')
        self.setParm('assumedLong', ' 74d35.3')
        resultDict = nav.correct(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'invalid lat')   

    def test400_925InvalidLatYdotYoutOfRangeReturnValueWithErrorKey(self):
        self.setParm('lat', '16d60.0')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '-53d38.4')
        self.setParm('assumedLong', ' 74d35.3')
        resultDict = nav.correct(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'invalid lat')   

    def test400_926InvalidLatOutOfRangeReturnValueWithErrorKey(self):
        self.setParm('lat', '90d0.0')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '-53d38.4')
        self.setParm('assumedLong', ' 74d35.3')
        resultDict = nav.correct(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'invalid lat')   


    
    def test400_930InvalidLongWrongFormatReturnValueWithErrorKey(self):
        self.setParm('lat', '16d32.3')
        self.setParm('long', '95.41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '-53d38.4')
        self.setParm('assumedLong', ' 74d35.3')
        resultDict = nav.correct(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'invalid long') 
    
    
    
    
    
    
    
    






