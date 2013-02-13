# -------------------------------
# Cameron Ebrahimian
# Lauren Salsini
# Copyright (C) 2013
# -------------------------------

"""
To test the program:
    % python TestXML.py >& TestXML.out
    % chmod ugo+x TestXMLpy
    % TestXML.py >& TestXML.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from XML import *
import xml.dom.minidom

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("<THU><Team></Team></THU>\n<Team></Team>\n")
        a = []
        b = xml_read(r, a)
        self.assert_(b.documentElement != None)
        self.assert_(len(a) == 2)


    def test_read2 (self) :
        r = StringIO.StringIO("<THU><Team></Team></THU>\n<Team></Team>")
        a = []
        b = xml_read(r, a)
        self.assert_(b.documentElement.tagName.find('THU') != -1)
        self.assert_(a == ["Team", "/Team"])

    def test_read3(self):
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>"+\
                              "<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n"+\
                              "<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n"+\
                              "<Cooly><Amber></Amber></Cooly>\n</Team>\n"+\
                              "</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>")
        a = []
        b = xml_read(r, a)
        self.assert_(b.documentElement.firstChild.firstChild.nodeName == "ACRush")
        self.assert_(a == ["Team", "Cooly", "/Cooly", "/Team"])

    # ----
    # eval
    # ----

    def test_eval (self) :
        r = StringIO.StringIO("<THU><Team></Team></THU>\n<Team></Team>\n")
        a = []
        b = xml_read(r, a)
        self.assert_(xml_eval(b, a) == [2])

    def test_eval2 (self):
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>"+\
                              "<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n"+\
                              "<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n"+\
                              "<Cooly><Amber></Amber></Cooly>\n</Team>\n"+\
                              "</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>")
        a = []
        b = xml_read(r, a)
        self.assert_(xml_eval(b, a) == [2, 7])

    def test_eval3 (self):
        r = StringIO.StringIO("")
        a = []
        b = xml_read(r, a)
        self.assert_(xml_eval(b, a) == [])

    # ----
    # find_index
    # ---

    def test_findIndex (self):
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>"+\
                              "<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n"+\
                              "<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n"+\
                              "<Cooly><Amber></Amber></Cooly>\n</Team>\n"+\
                              "</JiaJia>\n</THU>\n<Team><Cooly></Cooly></Team>")
        a = []
        b = xml_read(r, a)
        queryList = b.getElementsByTagName(a[0])
        self.assert_(find_index(b.documentElement, [queryList[0], 0, 0]) == 2)

    def test_findIndex2 (self):
        r = StringIO.StringIO("<THU></THU><THU></THU>")
        a = []
        b = xml_read(r, a)
        queryList = b.getElementsByTagName(a[0])
        self.assert_(find_index(b.documentElement, [queryList[0], 0, 0]) == 1)

    def test_findIndex3 (self):
        r = StringIO.StringIO("<THU>\n<Team>\n<ACRush></ACRush>\n<Jelly></Jelly>"+\
                              "<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n"+\
                              "<Ahyangyi></Ahyangyi>\n<Dragon></Dragon>\n"+\
                              "<Cooly><Amber></Amber></Cooly>\n</Team>\n"+\
                              "</JiaJia>\n</THU>\n<Team><Cooly><Amber></Amber>"+\
                              "<ACRush></ACRush></Cooly></Team>")
        a = []
        b = xml_read(r, a)
        queryList = b.getElementsByTagName(a[0])
        self.assert_(find_index(b.documentElement, [queryList[0], 0, 0]) == 2)

            

    # ----
    # xml_print
    # ----

    def test_print (self):
        resultList = []
        w = StringIO.StringIO()
        xml_print(resultList, w)
        self.assert_(w.getvalue() == "0\n")

    def test_print2 (self):
        resultList = [1, 2, 3]
        w = StringIO.StringIO()
        xml_print(resultList, w)
        self.assert_(w.getvalue() == "3\n1\n2\n3\n")

    def test_print3 (self):
        resultList = [2, -5, "hello", 9]
        w = StringIO.StringIO()
        xml_print(resultList, w)
        self.assert_(w.getvalue() == "4\n2\n-5\nhello\n9\n")

        
        
        
        
print "TestXML.py"
unittest.main()
print "Done."
