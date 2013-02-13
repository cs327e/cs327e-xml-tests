#!/usr/bin/env python

# -------------------------------
# projects/xml/TestXML.py
# Copyright (C) 2013
# Wilson Bui and Geovanni Monge
# -------------------------------


# -------
# imports
# -------

import StringIO
import unittest

from XML import xml_read, xml_print, xml_search, xml

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :

    # ----
    # read
    # ----
    
    def test_read_1 (self) :
        r = StringIO.StringIO("<THU>\n")
        l = []
        b = xml_read(r, l)
        self.assert_(b == True)
        self.assert_(l == ["<THU>"])

    def test_read_2 (self) :
        r = StringIO.StringIO("")
        l = []
        b = xml_read(r, l)
        self.assert_(b == False)


    def test_read_3 (self) :
        r = StringIO.StringIO("\t\t<Cooly><Amber></Amber></Cooly>\n")
        l = []
        b = xml_read(r, l)
        self.assert_(b == True)
        self.assert_(l == ["<Cooly><Amber></Amber></Cooly>"])

        
    # ------
    # search
    # ------

    def test_search_1 (self) :
        s = "<THU>\n"\
            "<Team>\n"\
            "<ACRush></ACRush>\n"\
            "<Jelly></Jelly>\n"\
            "<Cooly></Cooly>\n"\
            "</Team>\n"\
            "<JiaJia>\n"\
            "<Team>\n"\
            "<Ahyangyi></Ahyangyi>\n"\
            "<Dragon></Dragon>\n"\
            "<Cooly><Amber></Amber></Cooly>\n"\
            "</Team>\n"\
            "</JiaJia>\n"\
            "</THU>\n"
        l = "<Team><Cooly></Cooly></Team>"
        v = xml_search(s, l)
        self.assert_(v == [2, 2, 7])

    def test_search_2 (self) :

        s = "<Sports>\n"\
            "<Basketball>\n"\
            "<athletes>\n"\
            "<Kobe></Kobe>\n"\
            "<Lebron></Lebron>\n"\
            "<Durant></Durant>\n"\
            "<Carmelo></Carmelo>\n"\
            "</athletes>\n"\
            "</Basketball>\n"\
            "<Soccer>\n"\
            "<athletes>\n"\
            "<Messi></Messi>\n"\
            "<CRonaldo></CRonaldo>\n"\
            "<Iniesta></Iniesta>\n"\
            "<Xavi></Xavi>\n"\
            "<Kobe></Kobe>\n"\
            "</athletes>\n"\
            "</Soccer>\n"\
            "<Legends>\n"\
            "<Ronaldo></Ronaldo>\n"\
            "<Zidane></Zidane>\n"\
            "<Kobe></Kobe>\n"\
            "<Figo></Figo>\n"\
            "</Legends>\n"\
            "<CareerPoints>\n"\
            "<Kobe></Kobe>\n"\
            "</CareerPoints>\n"\
            "</Sports>\n"

        l = "<athletes><Kobe></Kobe></athletes>"
        v = xml_search(s, l)
        self.assert_(v == [2, 3, 9])

    def test_search_3 (self) :

        s = "<year>\n"\
           "<month>\n"\
           "<octb></octb>\n"\
           "<jan></jan>\n"\
           "<mar></mar>\n"\
           "</month>\n"\
           "<holiday>\n"\
           "<octb></octb>\n"\
           "<feb></feb>\n"\
           "</holiday>\n"\
           "<halloween>\n"\
           "<octb></octb>\n"\
           "<jan></jan>\n"\
           "</halloween>\n"\
           "</year>"

        l = "<month><octb></octb></month>"
        v = xml_search(s, l)
        self.assert_(v == [1, 2])

    def test_search_4 (self) :

        s = "<ANIMALS>\n"\
            "<Dogs>\n"\
            "<Rabbits></Rabbits>\n"\
            "<Frogs></Frogs>\n"\
            "</Dogs>\n"\
            "<Cheetahs></Cheetahs>\n"\
            "</ANIMALS>\n"

        l = "<Dogs><Cheetahs></Cheetahs></Dogs>"
        v = xml_search(s, l)
        self.assert_(v == [0])


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        v = 2
        xml_print(w, v)
        self.assert_(w.getvalue() == "2\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        v = 10
        xml_print(w, v)
        self.assert_(w.getvalue() == "10\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        v = 5
        xml_print(w, v)
        self.assert_(w.getvalue() == "5\n")


    # ---
    # xml
    # ---

    def test_xml_1 (self) :
        r = StringIO.StringIO("<THU>\n"\
                              "<Team>\n"\
                              "<ACRush></ACRush>\n"\
                              "<Jelly></Jelly>\n"\
                              "<Cooly></Cooly>\n"\
                              "</Team>\n"\
                              "<JiaJia>\n"\
                              "<Team>\n"\
                              "<Ahyangyi></Ahyangyi>\n"\
                              "<Dragon></Dragon>\n"\
                              "<Cooly><Amber></Amber></Cooly>\n"\
                              "</Team>\n"\
                              "</JiaJia>\n"\
                              "</THU>\n"\
                              "<Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml(r, w)
        self.assert_(w.getvalue() == "2\n2\n7\n")

    def test_xml_2 (self) :
        r = StringIO.StringIO("<Sports>\n"\
                              "<Basketball>\n"\
                              "<athletes>\n"\
                              "<Kobe></Kobe>\n"\
                              "<Lebron></Lebron>\n"\
                              "<Durant></Durant>\n"\
                              "<Carmelo></Carmelo>\n"\
                              "</athletes>\n"\
                              "</Basketball>\n"\
                              "<Soccer>\n"\
                              "<athletes>\n"\
                              "<Messi></Messi>\n"\
                              "<CRonaldo></CRonaldo>\n"\
                              "<Iniesta></Iniesta>\n"\
                              "<Xavi></Xavi>\n"\
                              "<Kobe></Kobe>\n"\
                              "</athletes>\n"\
                              "</Soccer>\n"\
                              "<Legends>\n"\
                              "<Ronaldo></Ronaldo>\n"\
                              "<Zidane></Zidane>\n"\
                              "<Kobe></Kobe>\n"\
                              "<Figo></Figo>\n"\
                              "</Legends>\n"\
                              "<CareerPoints>\n"\
                              "<Kobe></Kobe>\n"\
                              "</CareerPoints>\n"\
                              "</Sports>\n"\
                              "<athletes><Kobe></Kobe></athletes>")
        w = StringIO.StringIO()
        xml(r, w)
        self.assert_(w.getvalue() == "2\n3\n9\n")

    def test_xml_3 (self) :
        r = StringIO.StringIO("<ANIMALS>\n"\
                              "<Dogs>\n"\
                              "<Rabbits></Rabbits>\n"\
                              "<Frogs></Frogs>\n"\
                              "</Dogs>\n"\
                              "<Cheetahs></Cheetahs>\n"\
                              "</ANIMALS>\n"\
                              "<Dogs><Cheetahs></Cheetahs></Dogs>")
        w = StringIO.StringIO()
        xml(r, w)
        self.assert_(w.getvalue() == "0\n")

        
# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."

