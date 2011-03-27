from infix2Postfix import *
import unittest

class testInfix2Postfix(unittest.TestCase):

    def testOneOperand(self):
        self.assertEquals( i2p("5"), "5")
        
    def testOneOperation(self):
        self.assertEquals( i2p("1 + 1"), "1 1 +")
        
    def testTwoOperations(self):
        self.assertEquals( i2p("1 + ( 2 + 3 )"), "1 2 3 + +")
    
    def testExample(self):
        self.assertEquals( i2p("( 2 + 3 ) * 5"), "2 3 + 5 *" )
    
    def testScrewCase(self):
        self.assertEquals( i2p("( 1 * 3 ) / ( ( 1 + 2 ) - 2 )"), "1 3 * 1 2 + 2 - /" ) 
    
    def testMatchPar(self):
        self.assertEquals( substrMatchPar("1 + ( 2 + 3 )".split()), ("2 + 3".split(), []) )
        
    
    def testFoo(self):
        self.assertEquals( i2p(""), "")
    
unittest.main()
