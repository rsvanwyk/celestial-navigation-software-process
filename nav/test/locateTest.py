'''
    Assignment 10 - tests for operation 'locate'
    
    Created on Apr 26, 2019

    @author: Rong Song
'''

import unittest
import nav.locate as nav


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
    
    
    
    
    
    # Sad path tests
    def test500_910EmptyCorrectionsReturnValueWithErrorKey(self):
        self.setParm('assumedLat', '-53d38.4')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('corrections', '[]')
        resultDict = nav.locate(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'corrections can not be empty')   
        
    def test500_911MissingMandatoryCorrectionsReturnValueWithErrorKey(self):
        self.setParm('assumedLat', '-53d38.4')
        self.setParm('assumedLong', '350d35.3')
        resultDict = nav.locate(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'corrections is missing')   
    
    def test500_912InvalidCorrectionsDistanceNotIntReturnValueWithErrorKey(self):
        self.setParm('assumedLat', '-53d38.4')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('corrections', '[[100.3,1d0.1]]')
        resultDict = nav.locate(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'invalid corrections')   
        
    def test500_913InvalidCorrectionsAzimuthWrongFormatReturnValueWithErrorKey(self):
        self.setParm('assumedLat', '-53d38.4')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('corrections', '[[100,1.0.1]]')
        resultDict = nav.locate(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'invalid corrections') 
        
        
        
        
        
                    
        
        
    
    def test500_920MissingMandatoryAssumedLatReturnValueWithErrorKey(self):
        self.setParm('assumedLong', '350d35.3')
        self.setParm('corrections', '[]')
        resultDict = nav.locate(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'assumedLat is missing')   
   
    def test500_930InvalidAssumedLatXnotIntReturnValueWithErrorKey(self):
        self.setParm('assumedLat', '4.5d38.4')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('corrections', '[[100,1d0.0]]')
        resultDict = nav.locate(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'invalid assumedLat')   

    def test500_935InvalidAssumedLatYdotYoutOfRangeReturnValueWithErrorKey(self):
        self.setParm('assumedLat', '-53d68.4')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('corrections', '[[100,1d0.0]]')
        resultDict = nav.locate(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'invalid assumedLat')   

    def test500_940InvalidAssumedLongWrongFormatReturnValueWithErrorKey(self):
        self.setParm('assumedLat', '-53d38.4')
        self.setParm('assumedLong', '350.35.3')
        self.setParm('corrections', '[[100,1d0.0]]')
        resultDict = nav.locate(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'invalid assumedLong') 

















