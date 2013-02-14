
"""
To test the program:
    % python TestXML.py >& TestXML.py.out
    % chmod ugo+x TestXML.py
    % python TestXML.py >& TestXML.py.out
"""

# -------
# imports
# -------

import io
import unittest
import time

from XML import xml_read , xml_eval , xml_print , xml_solve

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = io.StringIO("<Lion>\n<Pens>\n<6th></6th>\n</Pens>\n</Lion>\n<Pens><6th></6th></Pens>")
        a = []
        b = []
        d = {}
        xml_read(r, a, b, d)
        self.assertTrue( a == ["<Lion>", "<Pens>" , "<6th>" , "</6th>" , "</Pens>" , "</Lion>"] )
        self.assertTrue( b == ["<Pens>" , "<6th>" , "</6th>" , "</Pens>" ] )
        self.assertTrue( d == { "<Lion>" : [1] , "<Pens>" : [2] , "<6th>" : [3]} )
        

    def test_read_2 (self) :
        r = io.StringIO("<A>\n<B>\n<C>\n<D></D>\n<E></E>\n</C>\n</B>\n<C>\n<D></D>\n</C>\n</A>\n<C><D></D></C>")
        a = []
        b = []
        d = {}
        xml_read(r, a, b, d)
        self.assertTrue( a == ['<A>', '<B>', '<C>', '<D>', '</D>', '<E>', '</E>', '</C>', '</B>', '<C>', '<D>', '</D>', '</C>', '</A>'] )
        self.assertTrue( b == ['<C>', '<D>', '</D>', '</C>'])
        self.assertTrue( d == {'<C>': [3, 6], '<A>': [1], '<D>': [4, 7], '<E>': [5], '<B>': [2]} )
        

    def test_read_3 (self) :
        r = io.StringIO("<1>\n<2>\n<4></4>\n</2>\n<3>\n<2>\n<4></4>\n<5></5>\n</2>\n</3>\n</1>\n<2><3></3></2>")
        a = []
        b = []
        d = {}
        xml_read(r, a, b, d)
        self.assertTrue( a == ['<1>', '<2>', '<4>', '</4>', '</2>', '<3>', '<2>', '<4>', '</4>', '<5>', '</5>', '</2>', '</3>', '</1>'] )
        self.assertTrue( b == ['<2>', '<3>', '</3>', '</2>'] )
        self.assertTrue( d == {'<3>': [4], '<1>': [1], '<4>': [3, 6], '<5>': [7], '<2>': [2, 5]} )




    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        a = ['<Lion>', '<Pens>', '<6th>', '</6th>', '</Pens>', '</Lion>']
        b = ['<Pens>', '<6th>', '</6th>', '</Pens>']
        d = {'<6th>': [3], '<Pens>': [2], '<Lion>': [1]}
        v = xml_eval(a ,b, d)
        self.assertTrue( v == [2, 1] )

    def test_eval_2 (self) :
        a = ['<A>', '<B>', '<C>', '<D>', '</D>', '<E>', '</E>', '</C>', '</B>', '<C>', '<D>', '</D>', '</C>', '</A>']
        b = ['<C>', '<D>', '</D>', '</C>']
        d = {'<C>': [3, 6], '<A>': [1], '<D>': [4, 7], '<E>': [5], '<B>': [2]}
        v = xml_eval(a, b, d)
        self.assertTrue(v == [3, 6, 2])

    def test_eval_3 (self) :
        a = ['<1>', '<2>', '<4>', '</4>', '</2>', '<3>', '<2>', '<4>', '</4>', '<5>', '</5>', '</2>', '</3>', '</1>']
        b = ['<2>', '<3>', '</3>', '</2>']
        d = {'<3>': [4], '<1>': [1], '<4>': [3, 6], '<5>': [7], '<2>': [2, 5]}
        v = xml_eval(a, b, d)
        self.assertTrue(v == [0] )




    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = io.StringIO()
        found = [2, 1]
        xml_print(w, found)
        self.assertTrue(w.getvalue() == "1\n2\n")

    def test_print_2 (self) :
        w = io.StringIO()
        found = [3, 6, 2]
        xml_print(w, found)
        self.assertTrue(w.getvalue() == "2\n3\n6\n")

    def test_print_3 (self) :
        w = io.StringIO()
        found = [0]
        xml_print(w, found)
        self.assertTrue(w.getvalue() == "0\n")




    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = io.StringIO("<Lion>\n<Pens>\n<6th></6th>\n</Pens>\n</Lion>\n<Pens><6th></6th></Pens>")
        w = io.StringIO()
        xml_solve(r, w)
        self.assertTrue(w.getvalue() == "1\n2\n")

    def test_solve_2 (self) :
        r = io.StringIO("<A>\n<B>\n<C>\n<D></D>\n<E></E>\n</C>\n</B>\n<C>\n<D></D>\n</C>\n</A>\n<C><D></D></C>")
        w = io.StringIO()
        xml_solve(r, w)
        self.assertTrue(w.getvalue() == "2\n3\n6\n")

    def test_solve_3 (self) :
        r = io.StringIO("<1>\n<2>\n<4></4>\n</2>\n<3>\n<2>\n<4></4>\n<5></5>\n</2>\n</3>\n</1>\n<2><3></3></2>")
        w = io.StringIO()
        xml_solve(r, w)
        self.assertTrue(w.getvalue() == "0\n")


# ----
# main
# ----

print("TestXML.py", end = "\n")
unittest.main()
print("Done." , end = "\n")
time.sleep(50)
