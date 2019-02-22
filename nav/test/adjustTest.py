import unittest
import nav.adjust as nav
import math

class adjustTest(unittest.TestCase):

    def setUp(self):
        self.inputDictionary = {'op':'adjust'}
        self.errorKey = "error"
        self.errorValue = "error msg" 
        self.solutionKey = "altitude"

    def tearDown(self):
        self.inputDictionary = {}


    def setParm(self, key, value):
        self.inputDictionary[key] = value


#     def testName(self):
#         pass  #<--  unit tests for adjust go here

    
    
    # -----------------------------------------------------------
    # Acceptance Tests -----> move to dispatchTest.py and modify
    # -----------------------------------------------------------
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
    def test200_010NominalInputValuesReturnValuesWithAltitudeAdjusted(self):
        self.setParm('observation', '30d1.5')
        self.setParm('height', '19.0')
        self.setParm('pressure', '1000')
        self.setParm('horizon', 'artificial')
        self.setParm('temperature', '85')
        resultDict = nav.adjust(self.inputDictionary)
        expectedResultDict = {'altitude':'29d59.9', 
                              'observation': '30d1.5', 
                              'height': '19.0', 
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

    def test200_920AltitudeAlreadyExistReturnValuesWithErrorKey(self):
        self.setParm('altitude', '13d42.3')
        self.setParm('observation', '30d1.5')        
        resultDict = nav.adjust(self.inputDictionary)
        self.assertTrue(resultDict.has_key('error'), True)
        self.assertEqual(resultDict['error'], 'altitude already exists in the input')
     
    def test200_930InvalidObservationReturnValuesWithErrorKey(self):    
        self.setParm('observation', '101d15.2')
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
    
    
    




#<--  unit tests for supporting functions of 'adjust' operation    
# ---------DELETE after unit tests done----------------
    def test200_310CalculateDip(self):        
        values = {'observation':'13d51.6',
                  'height':'33',
                  'temperature':'72',
                  'pressure':'1010',
                  'horizon':'natural'}
          
        if (values['horizon'].lower() == 'natural'):  
            heightValue = float(values['height'])          
            dip = ( -0.97 * math.sqrt( heightValue ) ) / 60
        else:
            dip = 0
  
        expectedDip = -0.092870429    
        self.assertAlmostEqual(dip, expectedDip, places=3)
         
    def test200_320CalculateRefraction(self):
        values = {'observation':'13d51.6',
                  'height':'33',
                  'temperature':'72',
                  'pressure':'1010',
                  'horizon':'natural'}
         
        degreeX = int(values['observation'].split('d')[0])
        minuteY = float(values['observation'].split('d')[1])
        observationDegrees = degreeX + ( minuteY / 60.0)
        observationRadians = math.radians(observationDegrees)
        observationTan = math.tan(observationRadians)
        temperatureF = int( values['temperature'] )
        temperatureC = (temperatureF - 32) * 5.0 / 9.0
        pressureValue = int( values['pressure'] )
        refraction = (-0.00452*pressureValue) / (273+temperatureC) / observationTan           
 
        expectedRefraction = -0.062673129    
        self.assertAlmostEqual(refraction, expectedRefraction, places=3)


        




    
    