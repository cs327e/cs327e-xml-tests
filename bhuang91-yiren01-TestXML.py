#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2013
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestXML.py >& TestXML.py.out
    % chmod ugo+x TestXML.py
    % TestXML.py >& TestXML.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from SphereXML2 import XML_read, XML_eval, XML_print, XML_solve

# -----------
# TestCollatz
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read1 (self) :
        r = StringIO.StringIO("<Team><Cooly></Cooly></Team>\n")
        tag = []
        first=[]
        b = XML_read(r, tag,first)
        self.assert_(b == False)
        self.assert_(tag == ['Team>','Cooly>','/Cooly>','/Team>'])

    def test_read2 (self) :
        r = StringIO.StringIO("<Team><ACRush></ACRush>"+\
                              "<Jelly></Jelly><Cooly></Cooly></Team>\n")
        tag = []
        first=[]
        b = XML_read(r, tag,first)
        self.assert_(b == False)
        self.assert_(tag == ['Team>','ACRush>','/ACRush>','Jelly>',\
                             '/Jelly>','Cooly>','/Cooly>','/Team>'])

    def test_read3 (self) :
        r = StringIO.StringIO("<Team><Ahyangyi></Ahyangyi>"+\
  		"<Dragon></Dragon><Cooly><Amber>"+\
                        "</Amber></Cooly></Team>")
        tag = []
        first=[]
        b = XML_read(r, tag,first)
        self.assert_(b == False)
        self.assert_(tag == ["Team>","Ahyangyi>","/Ahyangyi>",\
			"Dragon>","/Dragon>","Cooly>","Amber>",\
                        "/Amber>","/Cooly>","/Team>"])

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        tags=['Team>','Cooly>','/Cooly>','Amber>','/Amber>','/Team>']
        keys=['Team>','Cooly>','/Cooly>','/Team>']
        positions=[]
        XML_eval(tags,keys,positions)
        self.assert_(positions == [1])

    def test_eval_2 (self) :
        tags=["Team>","Ahyangyi>","/Ahyangyi>",\
			"Dragon>","/Dragon>","Cooly>","Amber>",\
                        "/Amber>","/Cooly>","/Team>"]
        keys=['Team>','Cooly>','/Cooly>','/Team>']
        positions=[]
        XML_eval(tags,keys,positions)
        self.assert_(positions == [1])

    def test_eval_3 (self) :
        tags=["THU>","Team>","ACRush>","/ACRush>","Jelly>",\
              "/Jelly>","Cooly>","/Cooly>","/Team>","JiaJia>",\
		"Team>","Ahyangyi>","/Ahyangyi>","Dragon>",\
              "/Dragon>","Cooly>","Amber>","/Amber>","/Cooly>","/Team>",\
            "/JiaJia>","/THU>"]
        keys=['Team>','Cooly>','/Cooly>','/Team>']
        positions=[]
        XML_eval(tags,keys,positions)
        self.assert_(positions == [2,7])

    # -----
    # print
    # -----

    def test_print1 (self) :
        w = StringIO.StringIO()
        positions=[2,7]
        XML_print(w,positions )
        self.assert_(w.getvalue() == '2\n2\n7\n')

    def test_print2 (self) :
        w = StringIO.StringIO()
        positions=[4,7,8,9]
        XML_print(w,positions )
        self.assert_(w.getvalue() == '4\n4\n7\n8\n9\n')

    def test_print3 (self) :
        w = StringIO.StringIO()
        positions=[]
        XML_print(w,positions )
        self.assert_(w.getvalue() == '0\n')


    # -----
    # solve
    # -----

    def test_solve1 (self) :
        r = StringIO.StringIO("<Team><Cooly></Cooly><Amber></Amber></Team>\n<Team><Cooly></Cooly></Team>\n")
        w = StringIO.StringIO()
        XML_solve(r, w)
        self.assert_(w.getvalue() == "1\n1\n")

    def test_solve2 (self) :
        r = StringIO.StringIO("<Team><Cooly></Cooly><Amber></Amber>"+\
                            "</Team>\n<Team><Cooly><Amber></Amber></Cooly></Team>\n")
        w = StringIO.StringIO()
        XML_solve(r, w)
        self.assert_(w.getvalue() == "0\n")

    def test_solve2 (self) :
        r = StringIO.StringIO("<Thu><Jia><Team><Cooly></Cooly><Amber></Amber>"+\
                            "</Team></Jia><Team><Jelly></Jelly><Cooly></Cooly></Team></Thu>"+\
                              "\n<Team><Cooly></Cooly></Team>\n")
        w = StringIO.StringIO()
        XML_solve(r, w)
        self.assert_(w.getvalue() == "2\n3\n6\n")

    
# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
