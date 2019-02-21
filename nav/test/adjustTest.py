import unittest
import nav.adjust as nav

class adjustTest(unittest.TestCase):

    def setUp(self):
        self.inputDictionary = {}
        self.errorKey = "error"
        # self.errorValue = "diagnostic string" ?
        self.BX_PATH = '/nav?'
        self.BX_PORT = 5000
        self.BX_URL = 'localhost'
        # self.BX_PORT = 5000
        # self.BX_URL = 'www.ibmcloud.com'

    def tearDown(self):
        self.inputDictionary = {}

    def setParm(self, key, value):
        self.inputDictionary[key]  = value

    # def microservice(self):
    #     pass



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
        #result = self.microservice()
        
        inputValues = {'op':'adjust'}
        expectedResult = {'error':'mandatory information is missing',
                          'op':'adjust'}
        actualResult = nav.adjust(inputValues)
        self.assertDictEqual(expectedResult, actualResult)
    
     
    
    
    
    
    
    
    
    
    