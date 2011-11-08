from looknsay import *
import unittest

class LookAndSayTest(unittest.TestCase):
    def test_look1(self):
        self.assertEquals(lookandsay(1),11)

    def test_look2(self):
        self.assertEquals(lookandsay(2),12)

    def test_look11(self):
        self.assertEquals(lookandsay(11),21)

    def test_look112(self):
        self.assertEquals(lookandsay(112),2112)

    def test_look21122(self):
        self.assertEquals(lookandsay(21122),122122)

    def test_iterator1(self):
        self.assertEquals(iterator(1,3), 1211)
        self.assertEquals(iterator(1,5), 312211)
        self.assertEquals(iterator(1,7), 1113213211)
        self.assertEquals(iterator(1,9), 13211311123113112211)
        self.assertEquals(iterator(1,2), 21)

    def test_iterator11(self):
        self.assertEquals(iterator(11,3), 111221)

    def test_iterator4(self):
        self.assertEquals(iterator(4,5), 1113122114)

    def test_iterator7(self):
        self.assertEquals(iterator(7,43), 1)
unittest.main()
