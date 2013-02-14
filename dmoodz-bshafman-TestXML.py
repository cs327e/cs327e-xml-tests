#!/usr/bin/env python

# -------------------------------
# 1/29/12
# cs327e
# Blake Schafman
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.py.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.py.out
"""

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
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("<team>\n <jacob></jacob> \n </team>\n <team><jacob></jacob></team>")
        a, b = xml_read(r)
        self.assert_(a == {1:["<team>", "<jacob>"], 2:["<jacob>"]})
        self.assert_(b == ["<team>", "<jacob>", "</jacob>", "</team>"])

    def test_read_2 (self) :
        r = StringIO.StringIO("<team><jacob><blake></blake></jacob></team><team><jacob></jacob></team>")
        a, b = xml_read(r)
        print a
        print b
        self.assert_(a == {1:["<team>", "<jacob>"], 2:["<jacob>", "<blake>"], 3:["<blake>"]})
        self.assert_(b == ["<team>", "<jacob>", "</jacob>", "</team>"])

    def test_read_3 (self) :
        r = StringIO.StringIO("<team>\n <jacob><blake></blake>\n </jacob></team>\n <team><jacob></jacob></team>\n")
        a, b = xml_read(r)
        self.assert_(a == {1:["<team>", "<jacob>"], 2:["<jacob>", "<blake>"], 3:["<blake>"]})
        self.assert_(b == ["<team>", "<jacob>", "</jacob>", "</team>"])

    def test_read_4 (self) :
        r = StringIO.StringIO("<team><jacob>\n <blake></blake></jacob>\n </team>\n <team> <jacob> </jacob> </team>\n")
        a, b = xml_read(r)
        self.assert_(a == {1:["<team>", "<jacob>"], 2:["<jacob>", "<blake>"], 3:["<blake>"]})
        self.assert_(b == ["<team>", "<jacob>", "</jacob>", "</team>"])

    # ----
    # parse
    # ----

    def test_parse_1 (self) :
        v = xml_parse(['<Team>', '<ACRush>', '</ACRush>', '<Jelly>', '</Jelly>', '<Cooly>', '</Cooly>','</Team>'])
        self.assert_(v == {1: ['<Team>', '<ACRush>', '<Jelly>', '<Cooly>'], 2: ['<ACRush>'], 3: ['<Jelly>'], 4: ['<Cooly>']})

    def test_parse_2 (self) :
        v = xml_parse(['<Jelly>', '</Jelly>', '<Cooly>', '</Cooly>'])
        self.assert_(v == {1: ['<Jelly>'], 2: ['<Cooly>']})

    def test_parse_3 (self) :
        v = xml_parse(['<Jelly>', '<Cooly>', '</Cooly>','</Jelly>'])
        self.assert_(v == {1: ['<Jelly>', '<Cooly>'], 2: ['<Cooly>']})

    def test_parse_4 (self) :
        v = xml_parse(['<Team>', '<ACRush>', '<Jelly>', '</Jelly>', '</ACRush>','</Team>'])
        self.assert_(v == {1: ['<Team>', '<ACRush>'], 2: ['<ACRush>', '<Jelly>'], 3: ['<Jelly>']})

	# ----
	# eval
	# ----
	def test_eval_1(self):
		d = {1: ['<Bookstore>', '<Book>', '<Book>'], 2: ['<Book>', '<Title>', '<Authors>'], 3: ['<Title>'], 4: ['<Authors>', '<Author>', '<Author>'], 5: ['<Author>', '<First_Name>', '<Last_Name>'], 6: ['<First_Name>'], 7: ['<Last_Name>'], 8: ['<Author>', '<First_Name>', '<Last_Name>'], 9: ['<First_Name>'], 10: ['<Last_Name>'], 11: ['<Book>', '<Title>', '<Remark>', '<Authors>'], 12: ['<Title>'], 13: ['<Remark>'], 14: ['<Authors>', '<Author>', '<Author>', '<Author>'], 15: ['<Author>', '<First_Name>', '<Last_Name>'], 16: ['<First_Name>'], 17: ['<Last_Name>'], 18: ['<Author>', '<First_Name>', '<Last_Name>'], 19: ['<First_Name>'], 20: ['<Last_Name>'], 21: ['<Author>', '<First_Name>', '<Last_Name>'], 22: ['<First_Name>'], 23: ['<Last_Name>']}
		q = ["<Book>", "<Title>", "</Title>", "<Authors>", "<Author>", "</Author>", "</Authors>", "</Book>"]
		v = xml_eval(d, q)
		self.assert_(v == "2\n2\n11")

	def test_eval_2(self):
		d = {1: ['<THU>', '<Team>', '<JiaJia>'], 2: ['<Team>', '<ACRush>', '<Jelly>', '<Cooly>'], 3: ['<ACRush>'], 4: ['<Jelly>'], 5: ['<Cooly>'], 6: ['<JiaJia>', '<Team>'], 7: ['<Team>', '<Ahyangyi>', '<Dragon>', '<Cooly>'], 8: ['<Ahyangyi>'], 9: ['<Dragon>'], 10: ['<Cooly>', '<Amber>'], 11: ['<Amber>']}
		q = ["<Team>", "<Cooly>", "</Cooly>", "</Team>"]
		v = xml_eval(d, q)
		self.assert_(v == "2\n2\n7")

	def test_eval_3(self):
		d = {1: ['<A>', '<a>', '<b>', '<c>', '<d>'], 2: ['<a>', '<1>', '<2>'], 3: ['<1>'], 4: ['<2>'], 5: ['<b>', '<1>', '<2>'], 6: ['<1>'], 7: ['<2>'], 8: ['<c>'], 9: ['<d>', '<1>'], 10: ['<1>', '<i>', '<ii>', '<iii>'], 11: ['<i>'], 12: ['<ii>'], 13: ['<iii>']}
		q = ["<d>", "<1>", "<i>", "</i>", "</1>", "</d>"]
		v = xml_eval(d, q)
		self.assert_(v == "1\n9")

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        xml_print(w, "Anything")
        self.assert_(w.getvalue() == "Anything")
    
    def test_print_2 (self) :
        w = StringIO.StringIO()
        xml_print(w, "2\n2\n7")
        self.assert_(w.getvalue() == "2\n2\n7")
    
    def test_print_3 (self) :
        w = StringIO.StringIO()
        xml_print(w, {"Test Key": "Test Value", "And": "Again"})
        self.assert_(w.getvalue() == "{'And': 'Again', 'Test Key': 'Test Value'}")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n<Cooly><Amber></Amber></Cooly>\n</Team>\n</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "2\n2\n7\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("<Bookstore>\n<Book>\n<Title></Title>\n<Authors>\n<Author>\n<First_Name></First_Name>\n<Last_Name></Last_Name>\n</Author>\n<Author>\n<First_Name></First_Name>\n<Last_Name></Last_Name>\n</Author>\n</Authors>\n</Book>\n<Book>\n<Title></Title>\n<Remark></Remark>\n<Authors>\n<Author>\n<First_Name></First_Name>\n<Last_Name></Last_Name>\n</Author>\n<Author>\n<First_Name></First_Name>\n<Last_Name></Last_Name>\n</Author>\n<Author>\n<First_Name></First_Name>\n<Last_Name></Last_Name>\n</Author>\n</Authors>\n</Book>\n</Bookstore>\n<Book><Title></Title><Authors><Author></Author></Authors></Book>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "2\n2\n11\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("<A><a><1></1><2></2></a><b><1></1><2></2></b><c></c><d><1><i></i><ii></ii><iii></iii></1></d></A><d><1><i></i></1></d>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == "1\n9\n")

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
