#!/usr/bin/env python

# -------------------------------
# projects/xml/TestXML.py
# Copyright (C) 2013
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

from XML import xml_tokenizer, xml_driver, xml_match, xml_print

# -----------
# TestCollatz
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # xml_tokenizer
    # ----

    def test_tokenizer1 (self) :
        print("TEST_TOKENIZER #1")
        s = StringIO.StringIO("<THU><Team></Team><JiaJia><Team></Team></JiaJia></THU><JiaJia></JiaJia>")
        tree, sep, search = xml_tokenizer(s)
        self.assert_( tree == "<THU><Team></Team><JiaJia><Team></Team></JiaJia>" ) 
        self.assert_( sep == "</THU>" )
        self.assert_( search == "<JiaJia></JiaJia>" )

    def test_tokenizer2 (self) :
        s = SringIO.StringIO("<Taylor><Holly></Holly></Taylor><Holly></Holly>")
        tree, sep, search = xml_tokenizer(s)
        self.assert_( tree == "<Taylor><Holly></Holly>" ) 
        self.assert_( sep == "</Taylor>" )
        self.assert_( search == "<Holly></Holly>" )

    def test_tokenizer3 (self) :
        s = SringIO.StringIO("<THU><Team><thu></thr></Team></THU><JiaJia></JiaJia>")
        tree, sep, search = xml_tokenizer(s)
        self.assert_( tree == "<THU><Team><thu></thr></Team>" ) 
        self.assert_( sep == "</THU>" )
        self.assert_( search == "<JiaJia></JiaJia>" )


    # ----
    # xml_match
    # ----


    #SETUP INPUT FOR TEST
    
    s = StringIO.StringIO("<THU><Team></Team><JiaJia><Team></Team></JiaJia></THU><JiaJia></JiaJia>")
    tree, sep, search = xml_tokenizer(s)
    #fix tree
    tree = ET.fromstring(tree+sep)
    t_iter = tree.iter()
    #ET.dump(tree)
    
    #creates a list, field, of elements to be searched for
    s_iter = ET.fromstring(search).iter()
    field = []
    for child in s_iter:
        field.append(child.tag)
    #print(sep)
    
    #creates a list, lst, of memory addresses for the nodes of the tree    
    lst = []
    for child in t_iter:
        lst.append(child)
    #print(lst)


    def test_match1 (self) :
         test = xml_match(1, match_parent[0], field)
         assert_(test == True)
        

    # ----
    # xml_driver
    # ----

    def test_driver1 (self) :
        v = xml_driver("<Taylor><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></Taylor><Taylor><Team></Team></Taylor>", w)
        self.assert_(v == "1\n1")

    def test_driver2 (self) :
        v = xml_driver(100, 200)
        self.assert_(v == 125)

    def test_driver3 (self) :
        v = xml_driver(201, 210)
        self.assert_(v == 89)

    def test_driver4 (self) :
        v = xml_driver(900, 1000)
        self.assert_(v == 174)



    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")

    def test_print_3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assert_(w.getvalue() == "201 210 89\n")

    def test_print_4 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")

               
    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1660 5068\n1362 5153\n6636 3965\n3226 5611\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1660 5068 238\n1362 5153 238\n6636 3965 262\n3226 5611 238\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("3842 1200\n3168 2892\n3419 6158\n87 6318\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "3842 1200 238\n3168 2892 217\n3419 6158 238\n87 6318 262\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("5881 2389\n9169 9347\n193 2702\n8515 190\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "5881 2389 238\n9169 9347 260\n193 2702 209\n8515 190 262\n")
       

# ----
# main
# ----

print ("TestXML.py")
unittest.main()
print ("Done.")
