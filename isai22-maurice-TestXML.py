# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 01:47:08 2013

@author: Maurice & Isaiah
"""
"""
To test the program:
    % python TestXML.py >& TestXML.py.out
    % chmod ugo+x TestXML.py
    % TestCollatz.py >& TestXML.py.out
"""


import StringIO
import unittest

from XML import XML_read_2, XML_print, XML_solve

class TestXML (unittest.TestCase):
    # ----
    # read
    # ----
    
    def test_read_1 (self):
        r = StringIO.StringIO('<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team>\
<JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team>\
</JiaJia></THU><Team><Cooly></Cooly></Team>')
        p= XML_read_2(r)
        self.assert_(p[0] == 2)
        self.assert_(p[1] == 2)
        self.assert_(p[2] == 7)

    def test_read_2 (self):
        r = StringIO.StringIO('<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly><Bob></Bob>\
</Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber>\
</Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>')
        p= XML_read_2(r)
        self.assert_(p[0] == 2)
        self.assert_(p[1] == 2)
        self.assert_(p[2] == 8)

    def test_read_3 (self):
        r = StringIO.StringIO('<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly><Bob></Bob></Cooly>\
</Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team>\
</JiaJia><Win><Team><Matt></Matt><Cooly></Cooly></Team></Win></THU><Team><Cooly></Cooly></Team>')
        p= XML_read_2(r)
        self.assert_(p[0] == 3)
        self.assert_(p[1] == 2)
        self.assert_(p[2] == 8)
        self.assert_(p[3] == 14)

    # ----
    # print
    # ----

    def test_print_1 (self):
        w= StringIO.StringIO()
        XML_print (w, 2)
        self.assert_(w.getvalue() == '2\n')

    def test_print_2 (self):
        w= StringIO.StringIO()
        XML_print (w, 2)
        self.assert_(w.getvalue() == '2\n')

    def test_print_3 (self):
        w= StringIO.StringIO()
        XML_print (w, 7)
        self.assert_(w.getvalue() == '7\n')

    # ----
    # solve
    # ----

    def test_solve_1 (self):
        r = StringIO.StringIO('<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team>\
<JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team>\
</JiaJia></THU><Team><Cooly></Cooly></Team>')
        w= StringIO.StringIO()
        XML_solve(r,w)
        self.assert_(w.getvalue() == '2\n2\n7\n')

    def test_solve_2 (self):
        r = StringIO.StringIO('<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly><Bob></Bob>\
</Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber>\
</Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>')
        w= StringIO.StringIO()
        XML_solve(r,w)
        self.assert_(w.getvalue() == '2\n2\n8\n')

    def test_solve_1 (self):
        r = StringIO.StringIO('<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly><Bob></Bob></Cooly>\
</Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team>\
</JiaJia><Win><Team><Matt></Matt><Cooly></Cooly></Team></Win></THU><Team><Cooly></Cooly></Team>')
        w= StringIO.StringIO()
        XML_solve(r,w)
        self.assert_(w.getvalue() == '3\n2\n8\n14\n')

print 'TestXML.py'
unittest.main()
print 'Done'
    
