from cheque import *
import unittest

class testCheque(unittest.TestCase):
    def testUmReal(self):
        self.assertEquals(cheque(1),'Um real')

    def testDoisReais(self):
        self.assertEquals(cheque(2), 'Dois reais')    
    
    def testQuatroReais(self):
        self.assertEquals(cheque(4), 'Quatro reais')

    def test17Reais(self):
        self.assertEquals(cheque(17), 'Dezessete reais')
    
    def test50Reais(self):
        self.assertEquals(cheque(50), 'Cinquenta reais')

    def testTrintaEDois(self):
        self.assertEquals(cheque(32), 'Trinta e dois reais')

    def testUmRealECinquentaCentavos(self):
        self.assertEquals(cheque(1.50), 'Um real e cinquenta centavos')
    def testUmRealECinquentaE4Centavos(self):
        self.assertEquals(cheque(1.54), 'Um real e cinquenta e quatro centavos')
    def test20Centavos(self):
        self.assertEquals(cheque(0.20),'Vinte centavos')
    def testZeroReaisEZeroCentavos(self):
        self.assertEquals(cheque(0.0),'')
    def test99ReaisE98Centavos(self):
        self.assertEquals(cheque(99.98),'Noventa e nove reais e noventa e oito centavos')
    def test99ReaisE99Centavos(self):
        self.assertEquals(cheque(99.99),'Noventa e nove reais e noventa e nove centavos')

unittest.main()

