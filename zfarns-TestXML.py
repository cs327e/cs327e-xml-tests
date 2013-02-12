#!/usr/bin/env python

# -------------------------------
# Zachary Farnsworth
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""

import StringIO
import unittest

from XML import xml_solve, printer, travI, trav, reader, Tree

class TestXML(unittest.TestCase):

    #The setUp function also tests the __init__ of class Tree
    def setUp(self):
        self.tree1 = Tree("base", 1)
        self.tree1.kids.append(Tree("sub", 2))
        self.tree1.kids[0].kids.append(Tree("deep", 3))
        self.tree1.kids[0].kids[0].kids.append(Tree("far", 4))
        self.tree1.kids[0].kids.append(Tree("cool", 5))
        self.tree2 = Tree("base", 1)
        self.tree2.kids.append(Tree("sub", 2))
        self.tree2.kids[0].kids.append(Tree("deep", 3))
        self.tree2.kids[0].kids[0].kids.append(Tree("far", 4))
        self.tags = "<THU><Team><ACRush></ACRush><Jelly></Jelly><Kelly></Kelly><Cooly></Cooly> \
                    </Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Philly> \
                    </Philly><Amber></Amber></Cooly></Team></JiaJia></THU>"

    def test_print_1(self) :
        w = StringIO.StringIO()
        printer(w, [4, 56, 78])
        self.assert_(w.getvalue() == "3\n4\n56\n78\n")

    def test_print_2(self) :
        w = StringIO.StringIO()
        printer(w, [2, 6])
        self.assert_(w.getvalue() == "2\n2\n6\n")

    def test_print_3(self) :
        w = StringIO.StringIO()
        printer(w, [4, 56, 78, 509687, 1234567890])
        self.assert_(w.getvalue() == "5\n4\n56\n78\n509687\n1234567890\n")

    def test_reader_1(self):
        r = StringIO.StringIO("<THU><FRI></FRI></THU>\n<THU><FRI></FRI></THU>")
        a = reader(r)
        self.assert_(a[0].kids[0].root == "THU")

    def test_reader_2(self):
        r = StringIO.StringIO("<THU><FRI></FRI></THU>\n<THU><FRI></FRI></THU>")
        a = reader(r)
        self.assert_(a[0].kids[0].kids[0].root == "FRI")

    def test_reader_3(self):
        r = StringIO.StringIO("<THU><FRI></FRI></THU>\n<THU><FRI></FRI></THU>")
        a = reader(r)
        self.assert_(a[1].kids[0].root == "THU")

    def test_travI_1(self):
        t = travI(self.tree1, self.tree2, [])
        self.assert_(t == [1])

    def test_travI_2(self):
        t = travI(self.tree1.kids[0], self.tree2.kids[0], [])
        self.assert_(t == [2])

    def test_travI_3(self):
        t = travI(self.tree1.kids[0].kids[0], self.tree2.kids[0].kids[0], [])
        self.assert_(t == [3])

    def test_trav_1(self):
        self.assert_(trav(self.tree1.kids, self.tree2.kids))

    def test_trav_2(self):
        self.assert_(trav(self.tree1.kids[0].kids, self.tree2.kids[0].kids))

    def test_trav_3(self):
        self.assert_(trav(self.tree1.kids[0].kids[0].kids, self.tree2.kids[0].kids[0].kids))

    def test_xml_solve_1(self):
        r = StringIO.StringIO(self.tags + "\n<Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "2\n2\n8\n")

    def test_xml_solve_2(self):
        r = StringIO.StringIO(self.tags + "\n<Team><Ahyangyi></Ahyangyi><Cooly> \
                                          <Amber></Amber></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n8\n")

    def test_xml_solve_3(self):
        r = StringIO.StringIO(self.tags + "\n<JiaJia><Team><Dragon></Dragon></Team></JiaJia>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n7\n")

print "TestXML.py"
unittest.main()
print "Done."
