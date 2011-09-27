import unittest
from frase import *

frases = ["Oi pessoal",
          "Oi pessoas\nFialho na area",
          "Hello mundo!\nAgora e a vez do lorenzo.\nDepois vai ser o diego",
          "Oi!!!\n\n\n!!!!!!!\n\n\n!!!\n",
          "Oi pessoal eu estou muito feliz de sair daqui :)",
          "aaaa bb aa"
         ]

class testFrase(unittest.TestCase):    

    def testUmaLinha(self):
        self.assertEquals(1, numero_linhas(frases[0]))

    def testDuasLinhas(self):
        self.assertEquals(2, numero_linhas(frases[1]))

    def testTresLinhas(self):
        self.assertEquals(3, numero_linhas(frases[2]))

    def testVariasLinhas(self):
        self.assertEquals(8, numero_linhas(frases[3]))

    def test10colunas(self):
        self.assertEquals(frases[0], quebra_linha(frases[0], 10))

    def testMuitasColunas(self):
        self.assertEquals(frases[4], quebra_linha(frases[4], 48))
        self.assertEquals(frases[4], quebra_linha(frases[4], 50))

    def testQuebraTexto(self):
        self.assertEquals("Oi\npessoal", quebra_linha(frases[0], 9))
        self.assertEquals(2, numero_linhas(quebra_linha(frases[0], 9)))

    def testQuebraTexto2(self):
        self.assertEquals("aaaa\nbb aa", quebra_linha(frases[5], 4))

    def testQuebraTextoGrande(self):     
        self.assertEquals("Oi pessoal eu estou muito feliz de sair daqui :)", quebra_linha(frases[4], 10))

unittest.main()

