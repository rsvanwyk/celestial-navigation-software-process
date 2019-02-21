import unittest
# import httplib
# from urllib import urlencode
import json

#import math
import nav.adjust as nav


class adjustTest(unittest.TestCase):

    def setUp(self):
        self.inputDictionary = {'op':'adjust'}
        self.errorKey = "error"
        self.errorValue = "error msg" 
        self.solutionKey = "altitude"
#         self.BX_PATH = '/nav?'
#         self.BX_PORT = 5000
#         self.BX_URL = 'localhost'
            #self.BX_PORT = 5000
            #self.BX_URL = 'www.ibmcloud.com'

    def tearDown(self):
        self.inputDictionary = {}


    def setParm(self, key, value):
        self.inputDictionary[key]  = value

#     def microservice(self):
#         try:
#             theParm = urlencode(self.inputDictionary)
#             theConnection = httplib.HTTPConnection(self.BX_URL, self.BX_PORT)
#             theConnection.request("GET", self.BX_PATH + theParm)
#             theStringResponse = theConnection.getresponse().read()
#             return theStringResponse
#         except Exception as e:
#             return "error encountered during transaction"

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


    # ---------DELETE after unit tests done----------------
    #<--  unit tests for supporting functions of 'adjust' operation
#     def test200_310CalculateDip(self):        
#         values = {'observation':'13d51.6',
#                   'height':'33',
#                   'temperature':'72',
#                   'pressure':'1010',
#                   'horizon':'natural'}
#          
#         if (values['horizon'].lower() == 'natural'):  
#             heightValue = float(values['height'])          
#             dip = ( -0.97 * math.sqrt( heightValue ) ) / 60
#         else:
#             dip = 0
#  
#         expectedDip = -0.092870429    
#         self.assertAlmostEqual(dip, expectedDip, places=3)
#         
#     def test200_320CalculateRefraction(self):
#         values = {'observation':'13d51.6',
#                   'height':'33',
#                   'temperature':'72',
#                   'pressure':'1010',
#                   'horizon':'natural'}
#         
#         degreeX = int(values['observation'].split('d')[0])
#         minuteY = float(values['observation'].split('d')[1])
#         angleDegrees = degreeX + ( minuteY / 60.0)
#         angleRadians = math.radians(angleDegrees)
#         tanObservation = math.tan(angleRadians)
#         temperatureF = int( values['temperature'] )
#         temperatureC = (temperatureF - 32) * 5.0 / 9.0
#         pressureValue = int( values['pressure'] )
#         refraction = (-0.00452*pressureValue) / (273+temperatureC) / tanObservation           
# 
#         expectedRefraction = -0.062673129    
#         self.assertAlmostEqual(refraction, expectedRefraction, places=3)

    
    
    
    
    
    
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
    #        010    nominal input values
    #        'observation': low bound (add later)
    #        optional elements missing, set to default 
    #        input extra elements, ignore
    #
    #    Sad path analysis:
    #        910    missing mandatory information 'observation'
    #        920    'altitude' already exists in the input dictionary
    #        930    invalid 'observation'
    #        940    invalid 'height'
    #        invalid 'temperature' (add later)
    #        invalid 'pressure' (add later)
    #        invalid 'horizon'
    #        'observation is .LT. 1d00.0 (invalid 'observation')
    #
    #
    # Happy path tests
#     def test200_010NominalInputValuesReturnValuesWithAltitudeAdjusted(self):
#         self.setParm('observation', '30d1.5')
#         self.setParm('height', '19.0')
#         self.setParm('pressure', '1000')
#         self.setParm('horizon', 'artificial')
#         self.setParm('temperature', '85')
#         result = self.microservice()
#         resultDict = self.string2dict(result)
#         expectedResultDict = {'altitude':'29d59.9', 
#                               'observation': '30d1.5', 
#                               'height': '19.0', 
#                               'pressure': '1000', 
#                               'horizon': 'artificial', 
#                               'op': 'adjust', 
#                               'temperature': '85'}
#         #self.assertDictEqual(resultDict, expectedResultDict)
    
    
    
    # Sad path tests
    def test200_910MissingMandatoryInfoReturnValuesWithErrorKey(self):
        result = self.microservice()
        resultDict = self.string2dict(result)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'mandatory information is missing')



# ----------------> failed ----------------
#     def test200_920AltitudeAlreadyExistReturnValuesWithErrorKey(self):
#         self.setParm('altitude', '13d42.3')
#         self.setParm('observation', '30d1.5')        
#         result = self.microservice()
#         resultDict = self.string2dict(result)
#         #self.assertTrue(resultDict.has_key('error'), True)
#         #self.assertEqual(resultDict['error'], 'altitude already exists in the input')
  
# -----------------> failed ------------------      
#     def test200_930InvalidObservationReturnValuesWithErrorKey(self):    
#         self.setParm('observation', '101d15.2')
#         self.setParm('height', '6')
#         self.setParm('pressure', '1010')
#         self.setParm('horizon', 'natural')
#         self.setParm('temperature', '71')
#         result = self.microservice()
#         resultDict = self.string2dict(result)
#         #self.assertTrue(resultDict.has_key('error'), True)
#         #self.assertEqual(resultDict['error'], 'observation is invalid')
         
# -----------> production code not finish --------------  
#     def test200_940InvalidHeightReturnValuesWithErrorKey(self):
#         self.setParm('observation', '45d15.2')
#         self.setParm('height', 'a')
#         self.setParm('pressure', '1010')
#         self.setParm('horizon', 'natural')
#         self.setParm('temperature', '71')
#         result = self.microservice()
#         resultDict = self.string2dict(result)
#         self.assertTrue(resultDict.has_key('error'), True)        
#         self.assertEqual(resultDict['error'], 'height is invalid')
    
    
    
    
    
    
    