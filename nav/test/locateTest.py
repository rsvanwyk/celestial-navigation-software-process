'''
    Assignment 10 - tests for operation 'locate'
    
    Created on Apr 26, 2019

    @author: Rong Song
'''

import unittest
import nav.locate as nav
from nav.locate import calcPresentPosition, estimatePrecision, estimateAccuracy
from nav.adjust import convertAngleStrToDegrees


class Test(unittest.TestCase):


    def setUp(self):
        self.inputDictionary = {'op':'locate'}
        self.errorKey = "error"
        self.errorValue = "diagnostic msg"
        self.solutionKey1 = "presentLat"
        self.solutionKey2 = "presentLong"
        self.solutionKey3 = "precision"
        self.solutionKey4 = "accuracy"        


    def tearDown(self):
        self.inputDictionary = {}


    def setParm(self, key, value):
        self.inputDictionary[key] = value
        
        
        
    # ---------------------------------------------------------------------------------
    # Acceptance Tests -----> add correspondent tests to dispatchTest.py and modify
    # ---------------------------------------------------------------------------------
    # 500 locate operation
    #
    #     input dictionary elements:
    #         'op':'locate',    validated
    #         'assumedLat':     unvalidated, mandatory
    #         'assumedLong':    unvalidated, mandatory
    #         'corrections':    unvalidated, mandatory
    #
    #
    # Happy path analysis:
    #    500_010 nominal input values
    #    500_020 input values contain extra element, ignore
    #    500_030 'assumedLat' degree portion x has leading zero
    #
    #
    #
    # Sad path analysis:
    #    500_910 empty 'corrections'
    #    500_911 missing mandatory 'corrections'
    #    500_912 invalid 'corrections'
    #    500_913 invalid 'corrections'
    #    500_920 missing mandatory 'assumedLat'
    #    500_930 invalid 'assumedLat' (x not int)
    #    500_935 invalid 'assumedLat' (y.y out of range)
    #    500_940 invalid 'assumedLong' (not in the form 'xdy.y')
    #    
    
    
    
    # Happy path tests
    def test500_010NominalInputValues(self):
        self.inputDictionary = {'op':'locate',  
                                'assumedLat':'-53d38.4', 
                                'assumedLong':'350d35.3',
                                'corrections':'[[100,1d0.0]]'}
        resultDict = nav.locate(self.inputDictionary)
        expectedResultDict = {'op':'locate', 
                              'lat':'16d32.3',  
                              'assumedLat':'-53d38.4', 
                              'assumedLong':'350d35.3', 
                              'corrections':'[[100,1d0.0]]', 
                              'presentLat':'-51d58.4',
                              'presentLong':'350d37.0',
                              'precision':'0',
                              'accuracy':'NA'}
        self.assertDictEqual(resultDict, expectedResultDict)
        




  
    
    
    
#     # Sad path tests (all passed)
#     def test500_910EmptyCorrectionsReturnValueWithErrorKey(self):
#         self.setParm('assumedLat', '-53d38.4')
#         self.setParm('assumedLong', '350d35.3')
#         self.setParm('corrections', '[]')
#         resultDict = nav.locate(self.inputDictionary)
#         self.assertTrue(resultDict.has_key('error'), True)
#         self.assertEqual(resultDict['error'], 'corrections can not be empty')   
#         
#     def test500_911MissingMandatoryCorrectionsReturnValueWithErrorKey(self):
#         self.setParm('assumedLat', '-53d38.4')
#         self.setParm('assumedLong', '350d35.3')
#         resultDict = nav.locate(self.inputDictionary)
#         self.assertTrue(resultDict.has_key('error'), True)
#         self.assertEqual(resultDict['error'], 'corrections is missing')   
#     
#     def test500_912InvalidCorrectionsDistanceNotIntReturnValueWithErrorKey(self):
#         self.setParm('assumedLat', '-53d38.4')
#         self.setParm('assumedLong', '350d35.3')
#         self.setParm('corrections', '[[100.3,1d0.1]]')
#         resultDict = nav.locate(self.inputDictionary)
#         self.assertTrue(resultDict.has_key('error'), True)
#         self.assertEqual(resultDict['error'], 'invalid corrections')   
#         
#     def test500_913InvalidCorrectionsAzimuthWrongFormatReturnValueWithErrorKey(self):
#         self.setParm('assumedLat', '-53d38.4')
#         self.setParm('assumedLong', '350d35.3')
#         self.setParm('corrections', '[[100,1.0.1]]')
#         resultDict = nav.locate(self.inputDictionary)
#         self.assertTrue(resultDict.has_key('error'), True)
#         self.assertEqual(resultDict['error'], 'invalid corrections') 
#         
#     
#     def test500_920MissingMandatoryAssumedLatReturnValueWithErrorKey(self):
#         self.setParm('assumedLong', '350d35.3')
#         self.setParm('corrections', '[]')
#         resultDict = nav.locate(self.inputDictionary)
#         self.assertTrue(resultDict.has_key('error'), True)
#         self.assertEqual(resultDict['error'], 'assumedLat is missing')   
#    
#     def test500_930InvalidAssumedLatXnotIntReturnValueWithErrorKey(self):
#         self.setParm('assumedLat', '4.5d38.4')
#         self.setParm('assumedLong', '350d35.3')
#         self.setParm('corrections', '[[100,1d0.0]]')
#         resultDict = nav.locate(self.inputDictionary)
#         self.assertTrue(resultDict.has_key('error'), True)
#         self.assertEqual(resultDict['error'], 'invalid assumedLat')   
# 
#     def test500_935InvalidAssumedLatYdotYoutOfRangeReturnValueWithErrorKey(self):
#         self.setParm('assumedLat', '-53d68.4')
#         self.setParm('assumedLong', '350d35.3')
#         self.setParm('corrections', '[[100,1d0.0]]')
#         resultDict = nav.locate(self.inputDictionary)
#         self.assertTrue(resultDict.has_key('error'), True)
#         self.assertEqual(resultDict['error'], 'invalid assumedLat')   
# 
#     def test500_940InvalidAssumedLongWrongFormatReturnValueWithErrorKey(self):
#         self.setParm('assumedLat', '-53d38.4')
#         self.setParm('assumedLong', '350.35.3')
#         self.setParm('corrections', '[[100,1d0.0]]')
#         resultDict = nav.locate(self.inputDictionary)
#         self.assertTrue(resultDict.has_key('error'), True)
#         self.assertEqual(resultDict['error'], 'invalid assumedLong') 




##############################################
# unit tests for support functions
##############################################

# tests for step A (all passed)
#     def test500_310calcPresentPositionTest(self):
#         
#         correctionsList = [['100','1d0.0']]
#         
#         assumedLatStr = '-53d38.4'
#         assumedLatDegrees = convertAngleStrToDegrees(assumedLatStr)
#         
#         assumedLongStr = '350d35.3'
#         assumedLongDegrees = convertAngleStrToDegrees(assumedLongStr)
#         
#         presentPositionList = calcPresentPosition(correctionsList, assumedLatDegrees, assumedLongDegrees)
#         presentLatStr = presentPositionList[0]
#         presentLongStr = presentPositionList[1]
#         
#         expectedPresentLat = '-51d58.4'
#         expectedPresentLong = '350d37.0'
#         
#         self.assertEqual(presentLatStr, expectedPresentLat)
#         self.assertEqual(presentLongStr, expectedPresentLong)
#     
#     def test500_311calcPresentPositionTest(self):
#         
#         correctionsList = [['50','45d0.0'],
#                            ['75','60d42.0'],
#                            ['100','300d11.2'],
#                            ['42','42d12.3'],
#                            ['70','60d45.0'],
#                            ['10','280d0.0']]
#         
#         assumedLatStr = '32d36.5'
#         assumedLatDegrees = convertAngleStrToDegrees(assumedLatStr)
#         
#         assumedLongStr = '274d31.1'
#         assumedLongDegrees = convertAngleStrToDegrees(assumedLongStr)
#         
#         presentPositionList = calcPresentPosition(correctionsList, assumedLatDegrees, assumedLongDegrees)
#         presentLatStr = presentPositionList[0]
#         presentLongStr = presentPositionList[1]
#         
#         expectedPresentLat = '33d8.1'
#         expectedPresentLong = '274d46.7'
#         
#         self.assertEqual(presentLatStr, expectedPresentLat)
#         self.assertEqual(presentLongStr, expectedPresentLong)        

        
# tests for step B (all passed)       
#     def test500_320estimatePrecisionTest(self):
#         correctionsList = [['100','1d0.0']]
#         precisionStr = estimatePrecision(correctionsList)
#         expectedPrecision = '0'
#         self.assertEqual(precisionStr, expectedPrecision)    
#      
#     def test500_321estimatePrecisionTest(self):
#         correctionsList = [['50','45d0.0'],
#                            ['75','60d42.0'],
#                            ['100','300d11.2'],
#                            ['42','42d12.3'],
#                            ['70','60d45.0'],
#                            ['10','280d0.0']]
#         precisionStr = estimatePrecision(correctionsList)
#         expectedPrecision = '45'
#         self.assertEqual(precisionStr, expectedPrecision)    
    
    
# tests for step C    
#     def test500_330estimateAccuracyTest(self):
#         correctionsList = [['100','1d0.0']]
#         accuracyStr = estimateAccuracy(correctionsList)
#         expectedAccuracy = 'NA'
#         self.assertEqual(accuracyStr, expectedAccuracy)    
# 
#     def test500_331estimateAccuracyTest(self):
#         correctionsList = [['50','45d0.0'],
#                            ['75','60d42.0'],
#                            ['100','300d11.2'],
#                            ['42','42d12.3'],
#                            ['70','60d45.0'],
#                            ['10','280d0.0']]
#         accuracyStr = estimateAccuracy(correctionsList)
#         expectedAccuracy = '2878'
#         self.assertEqual(accuracyStr, expectedAccuracy)    












