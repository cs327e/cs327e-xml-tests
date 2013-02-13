#!/usr/bin/env python

# ---------------------------
# cs327e-xml/TestXML.py
# Copyright (C) 2013
# Tracy Mullen, John Dees
# --------------------------

# -------
# imports
# -------

import StringIO
import unittest

from XML import *

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    
    # -----
    # xml_read
    # -----

    def test_read_1 (self) :
        r = StringIO.StringIO("<Team><Cooly></Cooly></Team>")
        inputList = []
        inputList = xml_read(r, inputList)
        self.assert_(inputList !=  [])

    def test_read_2 (self) :
        r = StringIO.StringIO("<Team><Cooly></Cooly></Team>")
        inputList = []
        inputList = xml_read(r, inputList)
        self.assert_(inputList !=  ["<Team>","<Cooly>","</Cooly>","</Team>"])

    def test_read_3 (self) :
        r = StringIO.StringIO("<Team><Cooly></Cooly></Team>")
        inputList = []
        inputList = xml_read(r, inputList)
        self.assert_(inputList ==  ["Team","Cooly","/Cooly","/Team"])

    # --------
    # findRoot
    # --------
 
    def test_eval_1(self) :
        inputList = ["<Team><Cooly></Cooly></Team>"]
        searchRoot = findRoot(inputList)
        self.assert_(searchRoot == [])

    def test_eval_2(self) :
        inputList = ["<Team><Cooly></Cooly></Team><Team></Team>"]
        searchRoot = findRoot(inputList)
        self.assert_(searchRoot != ["<Team>","</Team>"])

    def test_eval_3(self) :
        inputList = ["Team","Cooly","/Cooly","/Team","Cooly","/Cooly"]
        searchRoot = findRoot(inputList)
        self.assert_(searchRoot == ["Cooly","/Cooly"])

    # -------------
    # xml_write
    # -------------

    def test_print_1(self) :
        w = StringIO.StringIO()
        inputList = ["1","2","3"]
        xml_write(w,inputList)
        self.assert_(w.getvalue() == "1\n2\n3\n")

    def test_print_2(self) :
        w = StringIO.StringIO()
        inputList = [""]
        xml_write(w,inputList)
        self.assert_(w.getvalue() == "\n")

    def test_print_3(self) :
        w = StringIO.StringIO()
        inputList = ["1"]
        xml_write(w,inputList)
        self.assert_(w.getvalue() == "1\n")

# ----
# main
# ----

print("TestXML.py")
unittest.main()
print("Done.")
