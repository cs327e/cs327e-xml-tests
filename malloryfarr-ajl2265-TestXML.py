#!/usr/bin/env python

#----------------------
# cs327e-xml/TestXML.py
# Copyright (C) 2013
# Alex Leonard
# Mallory Farr
#----------------------

# unit tests for XML project

# -------
# imports
# -------

import StringIO
import unittest

from XML import xml_solve

class TestXML (unittest.TestCase):

    # -----
    # solve
    # -----
    
    def test_solve_1 (self) :
        r = StringIO.StringIO("<THU><Team><ACRush>\n</ACRush><Jelly>\n</Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly></Team>\n</JiaJia></THU><Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() ==  "2\n2\n7")

    def test_solve_2 (self) :
        r = StringIO.StringIO("<a><b><c></c></b></a>\n<b><c></c></b>")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "1\n2")

    def test_solve_3 (self) :
        r = StringIO.StringIO("<1>\n<2>\n<3></3>\n</2>\n</1>\n<1></1>")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "1\n1")

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
