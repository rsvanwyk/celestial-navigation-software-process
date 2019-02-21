import unittest
import httplib
from urllib import urlencode
import json

import nav.adjust as nav

class adjustTest(unittest.TestCase):

    def setUp(self):
        self.inputDictionary = {'op':'adjust'}
        self.errorKey = "error"
        self.errorValue = "error msg" 
        self.solutionKey = "altitude"
        self.BX_PATH = '/nav?'
        self.BX_PORT = 5000
        self.BX_URL = 'localhost'
        # self.BX_PORT = 5000
        # self.BX_URL = 'www.ibmcloud.com'

    def tearDown(self):
        self.inputDictionary = {}


    def setParm(self, key, value):
        self.inputDictionary[key]  = value

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



    #def testName(self):
    #    pass  #<--  unit tests for adjust go here
    
    
    
    # --------------------------------------------
    # Acceptance Tests
    # --------------------------------------------
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
    #        nominal input values
    #        'observation' x: low bound
    #        'observation' y.y: low bound
    #        optional elements missing, set to default 
    #        input extra elements, ignore
    #
    #    Sad path analysis:
    #        missing mandatory information 'observation'
    #        invalid 'observation'
    #        invalid 'height'
    #        invalid 'temperature'
    #        invalid 'pressure'
    #        invalid 'horizon'
    #
    #
    # Happy path tests
    #def test200_010NominalInputValues(self):
        
    
    
    
    # Sad path tests
    def test200_910MissingMandatoryInfoReturnError(self):
        #self.setParm('op', 'adjust')
        result = self.microservice()
        resultDict = self.string2dict(result)
        self.assertTrue(resultDict.has_key('error'), True)
        
#     def test200_920InvalidObservationReturnError(self):    
#         self.setParm(key, value)
#   
    
     
    
    
    
    
    
    
    
    
    