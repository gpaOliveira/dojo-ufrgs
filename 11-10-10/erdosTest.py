from erdos import *
import unittest

class AuthorTest(unittest.TestCase):

    def test_name(self):
        a = Author("Suya")
        self.assertEquals(a.name, "Suya")

    def test_relation(self):
        s = Author("Suya")
        l = Author("Lucas")
        s.addRelation(l)

        self.assertEquals(s.isRelated(l), True)
        self.assertEquals(l.isRelated(s), True)

    def test_equal(self):
        s = Author("Suya")
        s2 = Author("Suya")
        l = Author("Lucas")
        self.assertNotEquals(s, s2)
        self.assertNotEquals(s, l)
        self.assertEquals(s, s)

class ErdosTest(unittest.TestCase):

    def test_relations(self):
        s = Author("Suya")
        e = Author("Erdos")
        s.addRelation(e)
        self.assertEquals(erdos(s), 1)
        self.assertEquals(erdos(e), 0)

    def test_relationsComplex(self):
        s = Author("Suya")
        e = Author("Erdos")
        s.addRelation(e)
        l = Author("Lucas")
        l.addRelation(s)
        self.assertEquals(erdos(l), 2)

    def test_really_complex(self):
        m = Author("Manuel")
        d = Author("Diego")
        s = Author("Suya")
        l = Author("Lucas")
        a = Author("Augusto")
        f = Author("Fernando")
        e = Author("Erdos")
        
        m.addRelation(f)
        f.addRelation(l)
        l.addRelation(s)
        l.addRelation(e)
        l.addRelation(d)
        a.addRelation(e)
        f.addRelation(s)
        self.assertEquals(erdos(e), 0)
        self.assertEquals(erdos(l), 1)
        self.assertEquals(erdos(a), 1)
        self.assertEquals(erdos(f), 2)
        self.assertEquals(erdos(s), 2)
        self.assertEquals(erdos(d), 2)
        self.assertEquals(erdos(m), 3)

    def test_noErdos(self):
        m = Author("Manuel")
        d = Author("Diego")
        m.addRelation(d)
        d.addRelation(m)
        self.assertEquals(erdos(d), INFINITY)
        self.assertEquals(erdos(m), INFINITY)

unittest.main()
