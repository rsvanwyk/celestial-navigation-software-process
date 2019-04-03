import unittest
import httplib
from urllib import urlencode
import json



class DispatchTest(unittest.TestCase):
    
    def setUp(self):
        self.inputDictionary = {}
        self.errorKey = "error"
        self.solutionKey = "probability"
        self.BX_PATH = '/nav?'
        self.BX_PORT = 5000
        self.BX_URL = 'localhost'
#         self.BX_PORT = 5000
#         self.BX_URL = 'www.ibmcloud.com'

    def tearDown(self):
        self.inputDictionary = {}

    def setParm(self, key, value):
        self.inputDictionary[key] = value
        
    def microservice(self):
        try:
            theParm = urlencode(self.inputDictionary)
            theConnection = httplib.HTTPConnection(self.BX_URL, self.BX_PORT)
            theConnection.request("GET", self.BX_PATH + theParm)
            theStringResponse = theConnection.getresponse().read()
            return theStringResponse
        except Exception as e:
            return "error encountered during transaction"
        
    def string2dict(self, httpResponse):
        '''Convert JSON string to dictionary'''
        result = {}
        try:
            jsonString = httpResponse.replace("'", "\"")
            unicodeDictionary = json.loads(jsonString)
            for element in unicodeDictionary:
                if(isinstance(unicodeDictionary[element],unicode)):
                    result[str(element)] = str(unicodeDictionary[element])
                else:
                    result[str(element)] = unicodeDictionary[element]
        except Exception as e:
            result['diagnostic'] = str(e)
        return result



    # -----------------------------------------------------------------------
    # ---- Acceptance Tests
    # 100 dispatch operation
    #   Happy path analysis:
    #        values:      mandatory
    #                     dictionary
    #                     Operations:   {'op':'adjust'}
    #                                   {'op':'predict'}
    #                                   {'op':'correct'}
    #                                   {'op':'locate'}
    #   Sad path analysis:
    #        values:
    #                     no op specified             values={}
    #                        -- return {'error':'no op  is specified'}
    #                     contain 'error' as a key      values={5d04.9', 'height': '6.0', 'pressure': '1010',
    #                                                           'horizon': 'artificial', 'temperature': '72'
    #                                                           'error':'no op is specified'}'
    #                        -- return values without error as a key and without its values
    #                     not-dictionary                values=42
    #                        -- return {'error':'parameter is not a dictionary'}
    #                     not legal operation           values={'op': 'unknown'}
    #                        -- return {'error':'op is not a legal operation'}
    #                     missing dictionary            dispatch()
    #                        -- return {'error':'dictionary is missing'}
    
    
    
    # Happy path
#     def test100_010ShouldReturnUnchangedValuesWithOperationAdjust(self):
#         self.setParm('op','adjust')
#         result = self.microservice()
#         resultDictionary = self.string2dict(result)
#         self.assertDictEqual(self.inputDictionary, resultDictionary)
 
#     def test100_020ShouldReturnUnchangedValuesWithOperationPredict(self):
#         self.setParm('op','predict')
#         result = self.microservice()
#         resultDictionary = self.string2dict(result)
#         self.assertDictEqual(self.inputDictionary, resultDictionary)
  
#     def test100_030ShouldReturnUnchangedValuesWithOperationCorrect(self):
#         self.setParm('op','correct')
#         result = self.microservice()
#         resultDictionary = self.string2dict(result)
#         self.assertDictEqual(self.inputDictionary, resultDictionary)
         
    def test100_040ShouldReturnUnchangedValuesWithOperationLocate(self):
        self.setParm('op','locate')
        result = self.microservice()
        resultDictionary = self.string2dict(result)
        self.assertDictEqual(self.inputDictionary, resultDictionary)
  
       
    # Sad path
    def test100_910_ShouldReturnValuesWithErrorKeyWhenNoOpSpecified(self):
        result = self.microservice()
        resultDictionary = self.string2dict(result)
        self.assertTrue(resultDictionary.has_key("error"), True)
  
    def test100_920ShouldReturnValuesWithErrorWhenParameterIsNotALegalOperation(self):
        self.setParm('op','unknown')        
        result = self.microservice()
        resultDictionary = self.string2dict(result)
        self.assertTrue(resultDictionary.has_key("error"), True)
  
    def test100_930ShouldReturnValuesWithErrorWhenOpIsBlank(self):
        self.setParm('op','')        
        result = self.microservice()
        resultDictionary = self.string2dict(result)
        self.assertTrue(resultDictionary.has_key("error"), True)

   

    ####################################################################################
    # Acceptance tests related to operation 'adjust' ---> adapted from adjustTest.py  
    ####################################################################################
    
    # Happy path
    def test200_010NominalInputValuesReturnValuesWithAltitudeAdjusted(self):
        self.setParm('op', 'adjust')
        self.setParm('observation', '30d1.5')
        self.setParm('height', '19')
        self.setParm('pressure', '1000')
        self.setParm('horizon', 'artificial')
        self.setParm('temperature', '85')
        result = self.microservice()
        resultDict = self.string2dict(result)
        expectedResultDict = {'op': 'adjust',
                              'observation': '30d1.5', 
                              'height': '19', 
                              'pressure': '1000', 
                              'horizon': 'artificial',  
                              'temperature': '85',
                              'altitude':'29d59.9',}
        self.assertDictEqual(expectedResultDict, resultDict)                
    
    
    # Sad path
    def test200_910MissingMandatoryInfoReturnValuesWithErrorKey(self):
        self.setParm('op', 'adjust')    
        result = self.microservice()
        resultDict = self.string2dict(result)
        self.assertTrue(resultDict.has_key('error'), True)
        
 
 
    #####################################################################################
    # Acceptance tests related to operation 'predict' ---> adapted from predictTest.py
    #####################################################################################
    
    # Happy path
    def test300_010NominalInputValuesReturnValuesWithLongAndLat(self):
        self.setParm('op', 'predict')
        self.setParm('body', 'Aldebaran')
        self.setParm('date', '2016-01-17')
        self.setParm('time', '03:15:42')
        result = self.microservice()
        resultDict = self.string2dict(result)
        expectedResultDict = {'op':'predict', 
                              'body': 'Aldebaran', 
                              'date': '2016-01-17', 
                              'time': '03:15:42', 
                              'long':'95d41.6', 
                              'lat':'16d32.3'}    
        self.assertDictEqual(resultDict, expectedResultDict)
 
    # Sad path
    def test300_910MissingMandatoryInfoReturnValuesWithErrorKey(self):
        self.setParm('op', 'predict')
        result = self.microservice()
        resultDict = self.string2dict(result)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'mandatory information is missing')

 
 
    #####################################################################################
    # Acceptance tests related to operation 'correct' ---> adapted from correctTest.py
    #####################################################################################
 
    # Happy path
    
    
    
    # Sad path
 
 
 
 
        
        

