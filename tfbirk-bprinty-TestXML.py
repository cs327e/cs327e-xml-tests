#!/usr/bin/env python

# ---------------------------
# cs327e-xml/TestXML.py
# Copyright (C) 2013
# Blake Printy
# Taylor Birk
# --------------------------

"""
Unit tests for Project2 XML
"""

# -------
# imports
# -------

import StringIO
import unittest

from XML import xml_parse, xml_eval, xml_solve, xml_print

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # -----
    # parse
    # -----

    def test_read_1 (self) :
        r = StringIO.StringIO("<tag1>\n</tag1>\n<tag1></tag1>\n")
        inp = ["",""]
        b = xml_parse(r, inp)
        self.assert_(b == True)
        self.assert_(inp[0] ==  "<tag1></tag1>")
        self.assert_(inp[1] == "<tag1>.*?</tag1>")

    def test_read_2 (self) :
        r = StringIO.StringIO("<tag1></tag1>\n<tag1></tag1>\n")  # 2 lines only
        inp = ["",""]
        b = xml_parse(r, inp)
        self.assert_(b == True)
        self.assert_(inp[0] ==  "<tag1></tag1>")
        self.assert_(inp[1] == "<tag1>.*?</tag1>")

    def test_read_3 (self) :
        r = StringIO.StringIO("<tag1><tag2></tag2><tag3></tag3></tag1>\n<tag1></tag1>\n")
        inp = ["",""]
        b = xml_parse(r, inp)
        self.assert_(b == True)
        self.assert_(inp[0] ==  "<tag1><tag2></tag2><tag3></tag3></tag1>")
        self.assert_(inp[1] == "<tag1>.*?</tag1>")

    def test_read_4 (self) :
        r = StringIO.StringIO("<tag1><tag2></tag2><tag3>\n</tag3></tag1><tag1></tag1>\n")
        inp = ["",""]
        b = xml_parse(r, inp)
        self.assert_(b == True)
        self.assert_(inp[0] ==  "<tag1><tag2></tag2><tag3></tag3></tag1>")
        self.assert_(inp[1] == "<tag1>.*?</tag1>")

    # --------
    # xml_eval
    # --------
    
    def test_eval_1(self) :
        inp = ["<tag1></tag1>","<tag1>.*?</tag1>"]
        xml_out = []
        xml_eval(inp,xml_out)
        self.assert_(xml_out == ["1"])

    def test_eval_2(self) :
        inp = ["<tag1><tag2></tag2><tag3></tag3></tag1>","<tag1>.*?</tag1>"]
        xml_out = []
        xml_eval(inp,xml_out)
        self.assert_(xml_out == ["1"])

    def test_eval_3(self) :
       inp = ["<THU><Team><tag><Cooly></Cooly></tag></Team></THU>","<Team>.*?<Cooly>.*?</Cooly>.*?</Team>"]
       xml_out = []
       xml_eval(inp,xml_out)
       self.assert_(xml_out == ["2"])

    def test_eval_4(self) :
       inp = ["<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU>","<Team>.*?<Cooly>.*?</Cooly>.*?</Team>"]
       xml_out =[]
       xml_eval(inp,xml_out)
       self.assert_(xml_out == ["2","7"])

    # -------------
    # xml_print
    # -------------

    def test_print_1(self) :
        w = StringIO.StringIO()
        xml_out = ["1","3"]
        xml_print(w,xml_out)
        self.assert_(w.getvalue() == "2\n1\n3")

    def test_print_2(self) :
        w = StringIO.StringIO()
        xml_out = ["1","3","5","9"]
        xml_print(w,xml_out)
        self.assert_(w.getvalue() == "4\n1\n3\n5\n9")

    def test_print_3(self) :
        w = StringIO.StringIO()
        xml_out = ["1"]
        xml_print(w,xml_out)
        self.assert_(w.getvalue() == "1\n1")

    def test_print_4(self) :
        w = StringIO.StringIO()
        xml_out = ["4","3","5","6","65"]
        xml_print(w,xml_out)
        self.assert_(w.getvalue() == "5\n4\n3\n5\n6\n65")
		
    # -------------
    # xml_solve
    # -------------

    def test_solve_1 (self) :
        r = StringIO.StringIO("<tag1>\n<tag2></tag2></tag1>\n<tag1></tag1>\n")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() ==  "1\n1")

    def test_solve_2 (self) :
        r = StringIO.StringIO("<tag1></tag1>\n<tag1></tag1>\n")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "1\n1")

    def test_solve_3 (self) :
        r = StringIO.StringIO("<tag1><tag2><tag3></tag3></tag2><tag3></tag3><tag2></tag2></tag1>\n<tag2></tag2>\n")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "2\n2\n5")

    def test_solve_4 (self) :
        r = StringIO.StringIO("<THU><Team><ACRush>\n</ACRush><Jelly>\n</Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly></Team>\n</JiaJia></THU><Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() ==  "2\n2\n7")	

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
