#!/usr/bin/env python

import StringIO
import unittest
from XML import *

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----------
    # parse_tree
    # ----------

    def test_parse_tree_1 (self):
        r = StringIO.StringIO("<root><a></a><b></b></root><extra></extra>")
        tree = xml_parse_tree(r)
        expected = [('root', 1, [('a', 2, []), ('b', 3, [])])]
        self.assertEqual(tree, expected)
        self.assertEqual(r.read(), "<extra></extra>")

    def test_parse_tree_2 (self):
        r = StringIO.StringIO("<root></root><extra></extra>")
        tree = xml_parse_tree(r)
        expected = [('root', 1, [])]
        self.assertEqual(tree, expected)
        self.assertEqual(r.read(), "<extra></extra>")

    def test_parse_tree_3 (self):
        r = StringIO.StringIO("<root><a><b><c><d><e><f></f></e></d></c></b></a></root><extra></extra>")
        tree = xml_parse_tree(r)
        expected = [('root', 1, [('a', 2, [('b', 3, [('c', 4, [('d', 5, [('e', 6, [('f', 7, [])])])])])])])]
        self.assertEqual(tree, expected)
        self.assertEqual(r.read(), "<extra></extra>")

    # ----------
    # search
    # ----------

    def test_search_1 (self) :
        tree = [('root', 1, [])]
        pattern = [('root', None, [])]
        match = xml_search(tree, pattern)
        self.assertEqual(match, [1])

    def test_search_2 (self) :
        tree = [('root', 1, [])]
        pattern = [('a', None, [])]
        match = xml_search(tree, pattern)
        self.assertEqual(match, [])

    def test_search_3 (self) :
        tree = [('root', 1, [('a', 2, [('b', 3, [('c', 4, [('d', 5, [('a', 6, [('f', 7, [])])])])])])])]
        pattern = [('a', None, [])]
        match = xml_search(tree, pattern)
        self.assertEqual(match, [2, 6])

    def test_search_4 (self) :
        tree = [('root', 1, [('a', 2, [('b', 3, [('c', 4, [('d', 5, [('e', 6, [('f', 7, [])])])]), ('d', None, [])])])])]
        pattern = [('b', None, [('c', None, []), ('d', None, [])])]
        match = xml_search(tree, pattern)
        self.assertEqual(match, [3])

    def test_search_5 (self) :
        tree = [('root', 1, [('a', 2, [('b', 3, [('c', 4, [('d', 5, [('e', 6, [('f', 7, [])])])])]), ('d', None, [])])])]
        pattern = [('b', None, [('c', None, []), ('e', None, [])])]
        match = xml_search(tree, pattern)
        self.assertEqual(match, [])


    # ----------
    # solve
    # ----------

    def test_solve_1 (self) :
        r = StringIO.StringIO("<a></a><a></a>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertEquals(w.getvalue(), "1\n1\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("<a></a><b></b>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertEquals(w.getvalue(), "0\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertEquals(w.getvalue(), "2\n2\n7\n")

    def test_solve_4 (self) :
        r = StringIO.StringIO("<THU><Team><ACRush><Team><Cooly></Cooly></Team></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assertEquals(w.getvalue(), "3\n2\n4\n9\n")



# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
