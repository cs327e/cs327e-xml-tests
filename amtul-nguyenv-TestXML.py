#!/usr/bin/env python

# -------------------------------
# projects/XML/TestXML.py
# Copyright (C) 2013
# Amtul Batool and Vivian Nguyen
# -------------------------------

"""
To test the program:
    % python TestXML.py >& TestXML.out
    % chmod ugo+x TestXML.py
    % TestXML.py >& TestXML.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from XML import xml_read, xml_eval, xml_print, xml_solve

# -------
# TestXML
# -------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = xml_read(r, a)
        self.assert_(b    == False)
        self.assert_(a[0] == "")
        self.assert_(a[1] == "")

    def test_read_2 (self) :
        r = StringIO.StringIO("<x>\n<f>\n<p></p>\n</f>\n<j>\n<f>\n<p></p>\n</f>\n</j>\n<i>\n<g>\n<f>\n<p></p>\n</f>\n</g>\n</i>\n</x>\n<f><p></p></f>")
        a = [0, 0]
        b = xml_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == "<x>\n<f>\n<p></p>\n</f>\n<j>\n<f>\n<p></p>\n</f>\n</j>\n<i>\n<g>\n<f>\n<p></p>\n</f>\n</g>\n</i>\n</x>\n")
        self.assert_(a[1] == "<f><p></p></f>")

    def test_read_3 (self) :
        r = StringIO.StringIO("<e>\n<q>\n<b><i><c></c></i></b>\n</q>\n<b>\n<b><i><c></c></i></b>\n</b>\n</e>\n<b><i><c></c></i></b>")
        a = [0, 0]
        b = xml_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == "<e>\n<q>\n<b><i><c></c></i></b>\n</q>\n<b>\n<b><i><c></c></i></b>\n</b>\n</e>\n")
        self.assert_(a[1] == "<b><i><c></c></i></b>")
    
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        p = xml_eval("<r>\n<o>\n<t></t>\n</o>\n</r>\n", "<r><o></o></r>")
        self.assert_(p == [1])

    def test_eval_2 (self) :
        p = xml_eval("<x>\n<f>\n<p></p>\n</f>\n<j>\n<f>\n<p></p>\n</f>\n</j>\n<i>\n<g>\n<f>\n<p></p>\n</f>\n</g>\n</i>\n</x>\n", "<f><p></p></f>")
        self.assert_(p ==[2,5,9])

    def test_eval_3 (self) : 
        p = xml_eval("<e>\n<q>\n<b><i><c></c></i></b>\n</q>\n<b>\n<b><i><c></c></i></b>\n</b>\n</e>\n", "<b><i><c></c></i></b>")
        self.assert_(p == [3,7])


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        xml_print(w, [1])
        self.assert_(w.getvalue() == "1\n1\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        xml_print(w, [2,5,9])
        self.assert_(w.getvalue() == "3\n2\n5\n9\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        xml_print(w, [3,7])
        self.assert_(w.getvalue() == "2\n3\n7\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("<r>\n<o>\n<t></t>\n</o>\n</r>\n<r><o></o></r>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n1\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("<x>\n<f>\n<p></p>\n</f>\n<j>\n<f>\n<p></p>\n</f>\n</j>\n<i>\n<g>\n<f>\n<p></p>\n</f>\n</g>\n</i>\n</x>\n<f><p></p></f>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "3\n2\n5\n9\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("<e>\n<q>\n<b><i><c></c></i></b>\n</q>\n<b>\n<b><i><c></c></i></b>\n</b>\n</e>\n<b><i><c></c></i></b>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "2\n3\n7\n")
    
# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
