#!/usr/bin/env python

# -------------------------------
# TestXML.py
# Copyright (C) 2013
# Jonathan H. Anthony
# -------------------------------

"""
To test the program:
    % python TestXML.py >& TestXML.out
    % chmod ugo+x TestXML.py
    % TestXML.py >& TestXML.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from XML import XML_read, XML_eval, XML_search, XML_print, XML_solve

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("<THU>\n	<Team>\n		<ACRush></ACRush>\n		<Jelly></Jelly>\n		<Cooly></Cooly>\n	</Team>\n	<JiaJia>\n		<Team>\n			<Ahyangyi></Ahyangyi>\n			<Dragon></Dragon>\n			<Cooly><Amber></Amber></Cooly>\n		</Team>\n	</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
        doc = []
        query = []
        indices = []
        b = XML_read(r, doc, query, indices)
        self.assert_(b == True)
        self.assert_(doc == ["THU", "Team", "ACRush", "/ACRush", "Jelly", "/Jelly", "Cooly", "/Cooly", "/Team", "JiaJia", "Team", "Ahyangyi", "/Ahyangyi", "Dragon", "/Dragon", "Cooly", "Amber", "/Amber", "/Cooly", "/Team", "/JiaJia", "/THU"])
        self.assert_(query == ["Team", "Cooly", "/Cooly", "/Team"])
        self.assert_(indices == [1, 2, 3, 0, 4, 0, 5, 0, 0, 6, 7, 8, 0, 9, 0, 10, 11, 0, 0, 0, 0, 0])

    def test_read_2 (self) :
        r = StringIO.StringIO("<a> <b> <c> <d> <e> </e> </d> </c> </b> </a> <a> </a>")
        doc = []
        query = []
        indices = []
        b = XML_read(r, doc, query, indices)
        self.assert_(b == True)
        self.assert_(doc == ["a", "b", "c", "d", "e", "/e", "/d", "/c", "/b", "/a"])
        self.assert_(query == ["a", "/a"])
        self.assert_(indices == [1, 2, 3, 4, 5, 0, 0, 0, 0, 0])

    def test_read_3 (self) :
        r = StringIO.StringIO("<a ><b ></b><c></c >\n\n\n\t<d ></d></a><d> </d>")
        doc = []
        query = []
        indices = []
        b = XML_read(r, doc, query, indices)
        self.assert_(b == True)
        self.assert_(doc == ["a", "b", "/b", "c", "/c", "d", "/d", "/a"])
        self.assert_(query == ["d", "/d"])
        self.assert_(indices == [1, 2, 0, 3, 0, 4, 0, 0])

    def test_read_4 (self) :
        r = StringIO.StringIO("<a> <b> <c> <d> <e> </e> </d> </c> </b> <b> </b>")
        doc = []
        query = []
        indices = []
        b = XML_read(r, doc, query, indices)
        self.assert_(b == False)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        doc = ["THU", "Team", "ACRush", "/ACRush", "Jelly", "/Jelly", "Cooly", "/Cooly", "/Team", "JiaJia", "Team", "Ahyangyi", "/Ahyangyi", "Dragon", "/Dragon", "Cooly", "Amber", "/Amber", "/Cooly", "/Team", "/JiaJia", "/THU"]
        query = ["Team", "Cooly", "/Cooly", "/Team"]
        indices = [1, 2, 3, 0, 4, 0, 5, 0, 0, 6, 7, 8, 0, 9, 0, 10, 11, 0, 0, 0, 0, 0]
        v = XML_eval(doc, query, indices)
        self.assert_([2, 2, 7])

    def test_eval_2 (self) :
        doc = ["a", "b", "/b", "c", "/c", "d", "/d", "/a"]
        query = ["d", "/d"]
        indices = [1, 2, 0, 3, 0, 4, 0, 0]
        v = XML_eval(doc, query, indices)
        self.assert_([1, 4])

    def test_eval_3 (self) :
        doc = ["a", "b", "c", "d", "e", "/e", "/d", "/c", "/b", "/a"]
        query = ["a", "/a"]
        indices = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
        v = XML_eval(doc, query, indices)
        self.assert_([1, 1])

    # -----
    # search
    # -----

    def test_search_1 (self) :
        doc = ["THU", "Team", "ACRush", "/ACRush", "Jelly", "/Jelly", "Cooly", "/Cooly", "/Team", "JiaJia", "Team", "Ahyangyi", "/Ahyangyi", "Dragon", "/Dragon", "Cooly", "Amber", "/Amber", "/Cooly", "/Team", "/JiaJia", "/THU"]
        query = ["Team", "Cooly", "/Cooly", "/Team"]
        indices = [1, 2, 3, 0, 4, 0, 5, 0, 0, 6, 7, 8, 0, 9, 0, 10, 11, 0, 0, 0, 0, 0]
        i = 0;
        j = 21;
        k = 0;
        v = XML_search(doc, query, indices, i, j, k)
        self.assert_(v == False)

    def test_search_2 (self) :
        doc = ["THU", "Team", "ACRush", "/ACRush", "Jelly", "/Jelly", "Cooly", "/Cooly", "/Team", "JiaJia", "Team", "Ahyangyi", "/Ahyangyi", "Dragon", "/Dragon", "Cooly", "Amber", "/Amber", "/Cooly", "/Team", "/JiaJia", "/THU"]
        query = ["Team", "Cooly", "/Cooly", "/Team"]
        indices = [1, 2, 3, 0, 4, 0, 5, 0, 0, 6, 7, 8, 0, 9, 0, 10, 11, 0, 0, 0, 0, 0]
        i = 1;
        j = 9;
        k = 0;
        v = XML_search(doc, query, indices, i, j, k)
        self.assert_(v)

    def test_search_3 (self) :
        doc = ["THU", "Team", "ACRush", "/ACRush", "Jelly", "/Jelly", "Cooly", "/Cooly", "/Team", "JiaJia", "Team", "Ahyangyi", "/Ahyangyi", "Dragon", "/Dragon", "Cooly", "Amber", "/Amber", "/Cooly", "/Team", "/JiaJia", "/THU"]
        query = ["Team", "Cooly", "/Cooly", "/Team"]
        indices = [1, 2, 3, 0, 4, 0, 5, 0, 0, 6, 7, 8, 0, 9, 0, 10, 11, 0, 0, 0, 0, 0]
        i = 10;
        j = 19;
        k = 0;
        v = XML_search(doc, query, indices, i, j, k)
        self.assert_(v)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        XML_print(w, [1, 10, 11])
        self.assert_(w.getvalue() == "1\n10\n11\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        XML_print(w, [1])
        self.assert_(w.getvalue() == "1\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        XML_print(w, [])
        self.assert_(w.getvalue() == "")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("<THU>\n	<Team>\n		<ACRush></ACRush>\n		<Jelly></Jelly>\n		<Cooly></Cooly>\n	</Team>\n	<JiaJia>\n		<Team>\n			<Ahyangyi></Ahyangyi>\n			<Dragon></Dragon>\n			<Cooly><Amber></Amber></Cooly>\n		</Team>\n	</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>\n")
        w = StringIO.StringIO()
        XML_solve(r, w)
        self.assert_(w.getvalue() == "2\n2\n7\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("<a> <b> <c> <d> <e> </e> </d> </c> </b> </a> <a> </a>")
        w = StringIO.StringIO()
        XML_solve(r, w)
        self.assert_(w.getvalue() == "1\n1\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("<a ><b ></b><c></c >\n\n\n\t<d ></d></a><d> </d>")
        w = StringIO.StringIO()
        XML_solve(r, w)
        self.assert_(w.getvalue() == "1\n4\n")

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
