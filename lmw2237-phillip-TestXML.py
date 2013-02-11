#!/usr/bin/env python

# -------------------------------
# TestXML.py
# Copyright (C) 2013
# Lindsey Wohlfort & Phillip Lin
# -------------------------------


# -------
# imports
# -------

import StringIO
import unittest

from XML import xml_read, xml_eval, xml_print, xml_solve


# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("")
        d = {}
        ind = [0]
        firstTag = [""]
        extra = {}
        flag = xml_read(r,d,int,firstTag,extra)
        self.assert_(flag == False)

    def test_read_2 (self) :
        r = StringIO.StringIO("<Test><a></a></Test>\n<Test></Test>")
        d = {}
        ind = [0]
        firstTag = [""]
        extra = {}
        flag, nextflag = xml_read(r,d,ind,firstTag,extra)
        self.assert_(flag == False, nextflag == True)

    def test_read_3 (self) :
        r = StringIO.StringIO("<Test><a></a></Test><Test></Test>")
        d = {}
        ind = [0]
        firstTag = [""]
        extra = {}
        flag, nextflag = xml_read(r,d,ind,firstTag,extra)
        self.assert_(flag == False, nextflag == True)
        
##    def test_read_3 (self) :

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        d = {0: 'a', 1: 'c', 2: 'b', 3: '/b', 4: '/c', 5: '/a'}
        dp = {0: 'b', 1: '/b'}
        i = 2
        flag = xml_eval(d,dp,i)
        self.assert_(flag == True)

    def test_eval_2 (self) :
        d = {0: 'a', 1: 'c', 2: 'b', 3: '/b', 4: '/c', 5: '/a'}
        dp = {0: 'b', 1: '/b'}
        i = 1
        flag = xml_eval(d,dp,i)
        self.assert_(flag == True)

    def test_eval_3 (self) :
        d = {0: 'a', 1: 'b', 2: '/b', 3: 'c', 4: '/c', 5: '/a'}
        dp = {0: 'b', 1: '/b', 2: 'c', 3: '/c'}
        i = 1
        flag = xml_eval(d,dp,i)
        self.assert_(flag == True)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        xml_print(w,0,[])
        self.assert_(w.getvalue() == "0\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        xml_print(w,3,[1,2,3])
        self.assert_(w.getvalue() == "3\n1\n2\n3\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        xml_print(w,"",[])
        self.assert_(w.getvalue() == "\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("<a><b></b></a><b></b>")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "1\n2\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("<a><b></b><c></c></a>\n<b></b><c></c>")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "1\n2\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("<a><b></b></a><c></c>")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "0\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("<a><b>\n</b></a><b>\n</b>")
        w = StringIO.StringIO()
        xml_solve(r,w)
        self.assert_(w.getvalue() == "1\n2\n")
        

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
