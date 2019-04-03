'''
    assignment 6 - tests for operation 'adjust'

    Created on Feb 16, 2019

    @author: Rong Song
'''


import unittest
import nav.adjust as nav
import math


class adjustTest(unittest.TestCase):

    def setUp(self):
        self.inputDictionary = {'op':'adjust'}
        self.errorKey = "error"
        self.errorValue = "diagnostic msg" 
        self.solutionKey = "altitude"

    def tearDown(self):
        self.inputDictionary = {}


    def setParm(self, key, value):
        self.inputDictionary[key] = value

    
    # -------------------------------------------------------------
    # Acceptance Tests --->  modify and add to dispatchTest.py 
    # -------------------------------------------------------------
    # 200 adjust operation
    #    Desired level of confidence: boundary value analysis
    #    Input Analysis
    #        values: mandatory
    #                dictionary
    #                elements: 
    #                    'op':'adjust', validated
    #                    'observation': mandatory, string, form xdy.y, unvalidated
    #                        x: positive int .GE.1 and .LT.90
    #                        d: char 'd', separate x and y.y
    #                        y.y: positive float .GE.0.0 and .LT.60.0
    #                    'height': optional, string of numeric value .GE.0, 
    #                        default='0' if missing, unvalidated
    #                    'temperature': optional, string of int .GE.-20 and .LE.120, 
    #                        default='72' if missing, unvalidated
    #                    'pressure': optional, string of int .GE.100 and .LE.1100, 
    #                        default='1010' if missing, unvalidated
    #                    'horizon': optional, string, case-insensitive, one of the following:
    #                        'artificial' or 'natural', default='natural' if missing, unvalidated
    #
    #    Happy path analysis:
    #        200_010    nominal input values
    #        200_020    optional elements missing, set to default 
    #        200_030    input extra elements, ignore
    #        200_040    'observation': low bound
    #
    #    Sad path analysis:
    #        200_910    missing mandatory information 'observation'
    #        200_920    'altitude' already exists in the input dictionary
    #        200_930    invalid 'observation'
    #        200_931    invalid 'observation' not in form xdy.y
    #        200_935    invalid 'observation' .LT. 1d00.0
    #        200_940    invalid 'height'
    #        200_950    invalid 'horizon'
    #        200_960    invalid 'temperature'
    #        200_970    invalid 'pressure'


    # Happy path tests
    def test200_010NominalInputValuesReturnValuesWithAltitudeAdjusted(self):
        self.setParm('observation', '30d1.5')
        self.setParm('height', '19')
        self.setParm('pressure', '1000')
        self.setParm('horizon', 'artificial')
        self.setParm('temperature', '85')
        resultDict = nav.adjust(self.inputDictionary)
        expectedResultDict = {'op': 'adjust',
                              'observation': '30d1.5', 
                              'height': '19', 
                              'pressure': '1000', 
                              'horizon': 'artificial',  
                              'temperature': '85',
                              'altitude':'29d59.9',}
        self.assertDictEqual(resultDict, expectedResultDict)
    
    def test200_020OptionalElementsMissingSetToDefaul(self):
        self.setParm('observation', '42d0.0')
        resultDict = nav.adjust(self.inputDictionary)
        expectedResultDict = {'altitude': '41d59.0', 
                              'observation': '42d0.0',  
                              'op': 'adjust'}
        self.assertDictEqual(resultDict, expectedResultDict)
    
    def test200_030IgnoreExtraInputElements(self):
        self.setParm('observation', '42d0.0')
        self.setParm('extraKey', 'ignore')
        resultDict = nav.adjust(self.inputDictionary)
        expectedResultDict = {'altitude':'41d59.0', 
                              'observation': '42d0.0',  
                              'op': 'adjust', 
                              'extraKey':'ignore'}
        self.assertDictEqual(resultDict, expectedResultDict)
    
    def test200_040ObservationLowBound(self):
        self.setParm('observation', '1d0.0')
        self.setParm('height', '19')
        self.setParm('pressure', '1000')
        self.setParm('horizon', 'artificial')
        self.setParm('temperature', '85')
        resultDict = nav.adjust(self.inputDictionary)
        expectedResultDict =  {'altitude': '0d8.6', 
                               'observation': '1d0.0', 
                               'height': '19', 
                               'pressure': '1000', 
                               'horizon': 'artificial', 
                               'op': 'adjust', 
                               'temperature': '85'}
        self.assertDictEqual(resultDict, expectedResultDict)
        
        
    
    # Sad path tests
    def test200_910MissingMandatoryInfoReturnValuesWithErrorKey(self):
        resultDict = nav.adjust(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'mandatory information is missing')

# ---------> change of requirement: if 'altitude' already exist then override its value
#     def test200_920AltitudeAlreadyExistReturnValuesWithErrorKey(self):
#         self.setParm('altitude', '13d42.3')
#         self.setParm('observation', '30d1.5')        
#         resultDict = nav.adjust(self.inputDictionary)
#         self.assertTrue(resultDict.has_key('error'), True)
#         self.assertEqual(resultDict['error'], 'altitude already exists in the input')
     
    def test200_930InvalidObservationXoutOfRangeReturnValuesWithErrorKey(self):    
        self.setParm('observation', '101d15.2')
        self.setParm('height', '6')
        self.setParm('pressure', '1010')
        self.setParm('horizon', 'natural')
        self.setParm('temperature', '71')
        resultDict = nav.adjust(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'observation is invalid')

    def test200_931InvalidObservationWrongFormatReturnValuesWithErrorKey(self):    
        self.setParm('observation', '101')
        self.setParm('height', '6')
        self.setParm('pressure', '1010')
        self.setParm('horizon', 'natural')
        self.setParm('temperature', '71')
        resultDict = nav.adjust(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'observation is invalid')

    def test200_933InvalidObservationEmptyStrReturnValuesWithErrorKey(self):    
        self.setParm('observation', '')
        self.setParm('height', '6')
        self.setParm('pressure', '1010')
        self.setParm('horizon', 'natural')
        self.setParm('temperature', '71')
        resultDict = nav.adjust(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'observation is invalid')

    #935 ---> change of requirement: invalid 'observation' .LT. 1d00.0
    def test200_935InvalidObservationOutOfRangeReturnValueWithErrorKey2(self):
        self.setParm('observation', '0d15.2')
        self.setParm('height', '6')
        self.setParm('pressure', '1010')
        self.setParm('horizon', 'natural')
        self.setParm('temperature', '71')
        resultDict = nav.adjust(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'observation is invalid')

    def test200_940InvalidHeightReturnValuesWithErrorKey(self):
        self.setParm('observation', '45d15.2')
        self.setParm('height', 'a')
        self.setParm('pressure', '1010')
        self.setParm('horizon', 'natural')
        self.setParm('temperature', '71')
        resultDict = nav.adjust(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)        
        self.assertEqual(resultDict['error'], 'height is invalid')
    
    def test200_950InvalidHorizonReturnValuesWithErrorKey(self):
        self.setParm('observation', '45d15.2')
        self.setParm('height', '6')
        self.setParm('horizon', ' ')
        self.setParm('pressure', '1010')
        self.setParm('temperature', '71')
        resultDict = nav.adjust(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)        
        self.assertEqual(resultDict['error'], 'horizon is invalid')
        
    def test200_960InvalidTemperatureReturnValuesWithErrorKey(self):
        self.setParm('observation', '45d15.2')
        self.setParm('height', '6')
        self.setParm('horizon', 'natural')
        self.setParm('pressure', '1010')
        self.setParm('temperature', '150')
        resultDict = nav.adjust(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)        
        self.assertEqual(resultDict['error'], 'temperature is invalid')
    
    def test200_970InvalidPressureReturnValuesWithErrorKey(self):
        self.setParm('observation', '45d15.2')
        self.setParm('height', '6')
        self.setParm('horizon', 'natural')
        self.setParm('pressure', '50')
        self.setParm('temperature', '71')
        resultDict = nav.adjust(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)        
        self.assertEqual(resultDict['error'], 'pressure is invalid')
    
    



        




    
    