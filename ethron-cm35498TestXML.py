"""
Test program for XML.py
"""

# -------
# imports
# -------

import StringIO
import unittest

from XML import xml_read, xml_refine, xml_pclist, xml_eval, xml_confirm, xml_search, xml_print, xml_solve

# -------
# TestXML
# -------

class TestXML(unittest.TestCase):

    # ----
    # read
    # ----

    def test_read_1(self):
        r = StringIO.StringIO("<THU><Team>\n")
        a = []
        b = xml_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == "<THU><Team>")

    def test_read_2(self):
        r = StringIO.StringIO("")
        a = []
        b = xml_read(r, a)
        self.assert_(b == False)

    def test_read_3(self):
        r = StringIO.StringIO("<THU><Team><Jelly></Jelly>\n")
        a = []
        b = xml_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == "<THU><Team><Jelly></Jelly>")

    # ------
    # refine
    # ------

    def test_refine_1(self):
        x,y = xml_refine(['<THU>', '</THU>', '<Team>'])
        self.assert_(x == ['THU', '/THU'])
        self.assert_(y == ['Team'])
    
    def test_refine_2(self):
        x,y = xml_refine(['<Cooly><Amber></Amber></Cooly>', '<Dog><Cat></Cat></Dog>'])
        self.assert_(x == ['Cooly', 'Amber', '/Amber', '/Cooly'])
        self.assert_(y == ['Dog', 'Cat', '/Cat', '/Dog'])
        
    def test_refine_3(self):
        x,y = xml_refine(['<THU>', '<Team>', '<ACRush></ACRush>', '<Jelly></Jelly>', '<Cooly></Cooly>', '</Team>', '<JiaJia>', '<Team>', '<Ahyangyi></Ahyangyi>', '<Dragon></Dragon>', '<Cooly><Amber></Amber></Cooly>', '</Team>', '</JiaJia>', '</THU><Team><Cooly></Cooly></Team>'])
        self.assert_(x == ['THU', 'Team', 'ACRush', '/ACRush', 'Jelly', '/Jelly', 'Cooly', '/Cooly', '/Team', 'JiaJia', 'Team', 'Ahyangyi', '/Ahyangyi', 'Dragon', '/Dragon', 'Cooly', 'Amber', '/Amber', '/Cooly', '/Team', '/JiaJia', '/THU'])
        self.assert_(y == ['Team', 'Cooly', '/Cooly', '/Team'])

    # ------
    # pclist
    # ------

    def test_pclist_1(self):
        refined_list = ['Cooly', 'Amber', '/Amber', '/Cooly']
        pclist = xml_pclist(refined_list)
        self.assert_(pclist == [1, 2, 1, 0])

    def test_pclist_2(self):
        refined_list = ['THU', 'Team', 'ACRush', '/ACRush', 'Jelly', '/Jelly', 'Cooly', '/Cooly', '/Team', 'JiaJia', 'Team', 'Ahyangyi', '/Ahyangyi', 'Dragon', '/Dragon', 'Cooly', 'Amber', '/Amber', '/Cooly', '/Team', '/JiaJia', '/THU']
        pclist = xml_pclist(refined_list)
        self.assert_(pclist == [1, 2, 3, 2, 3, 2, 3, 2, 1, 2, 3, 4, 3, 4, 3, 4, 5, 4, 3, 2, 1, 0])

    def test_pclist_3(self):
        refined_list = ['A', 'B', 'C', 'D', '/D', 'E', '/E', '/C', '/B', '/A']
        pclist = xml_pclist(refined_list)
        self.assert_(pclist == [1, 2, 3, 4, 3, 4, 3, 2, 1, 0])

    # ----
    # eval
    # ----

    def test_eval_1(self):
        index = [1, 5, 7, 9]
        compare_pc = [0, 1]
        test = xml_eval(index, compare_pc)
        self.assert_(test == True)

    def test_eval_2(self):
        index = [1, 10, 7, 9]
        compare_pc = [0, 1]
        test = xml_eval(index, compare_pc)
        self.assert_(test == False)

    def test_eval_3(self):
        index = [1, 5, 7, 9]
        compare_pc = [0, 2]
        test = xml_eval(index, compare_pc)
        self.assert_(test == False)

    # -------
    # confirm
    # -------

    def test_confirm_1(self):
        temp_list = ['Team', 'ACRush', 'Cooly', '/Cooly', '/ACRush', 'Jelly', '/Jelly', '/Team']
        temp_query = ['Team', 'Cooly', '/Cooly', '/Team']
        temp_pclist = [2, 3, 4, 3, 2, 3, 2, 1]
        index = []
        test = xml_confirm(temp_list, temp_query, temp_pclist, index)
        self.assert_(test == False)

    def test_confirm_2(self):
        temp_list = ['Team', 'ACRush', '/ACRush', 'Cooly', '/Cooly', 'Jelly', '/Jelly', '/Team']
        temp_query = ['Team', 'Cooly', '/Cooly', '/Team']
        temp_pclist = [2, 3, 2, 3, 2, 3, 2, 1]
        index = []
        test = xml_confirm(temp_list, temp_query, temp_pclist, index)
        self.assert_(test == True)

    def test_confirm_3(self):
        temp_list = ['Team', 'ACRush', '/ACRush', 'Jelly', '/Jelly', '/Team']
        temp_query = ['Team', 'Cooly', '/Cooly', '/Team']
        temp_pclist = [2, 3, 2, 3, 2, 1]
        index = []
        test = xml_confirm(temp_list, temp_query, temp_pclist, index)
        self.assert_(test == False)

    # ------
    # search
    # ------

    def test_search_1(self):
        refined_list = ['THU', 'Team', 'ACRush', '/ACRush', 'Cooly', '/Cooly', 'Jelly', '/Jelly', '/Team', 'JiaJia', 'Team', 'Dragon', '/Dragon', 'Cooly', '/Cooly', '/Team', '/JiaJia', '/THU']
        query_list = ['Team', 'Cooly', '/Cooly', '/Team']
        pclist = [1, 2, 3, 2, 3, 2, 3, 2, 1, 2, 3, 4, 3, 4, 3, 2, 1, 0]
        test = xml_search(refined_list, query_list, pclist)
        self.assert_(test[0] == 2)
        self.assert_(test[1] == 7)

    def test_search_2(self):
        refined_list = ['THU', 'Team', 'ACRush', '/ACRush', 'Cooly', '/Cooly', 'Jelly', '/Jelly', '/Team', 'JiaJia', 'Team', 'Dragon', '/Dragon', 'Cooly', '/Cooly', '/Team', '/JiaJia', '/THU']
        query_list = ['JiaJia', 'Team', 'Dragon', '/Dragon', '/Team', '/JiaJia']
        pclist = [1, 2, 3, 2, 3, 2, 3, 2, 1, 2, 3, 4, 3, 4, 3, 2, 1, 0]
        test = xml_search(refined_list, query_list, pclist)
        self.assert_(test[0] == 6)

    def test_search_3(self):
        refined_list = ['THU', 'Team', 'ACRush', 'Cooly', '/Cooly', '/ACRush', 'Jelly', '/Jelly', '/Team', 'JiaJia', 'Team', 'Dragon', '/Dragon', 'Cooly', '/Cooly', '/Team', '/JiaJia', '/THU']
        query_list = ['Team', 'Cooly', '/Cooly', '/Team']
        pclist = [1, 2, 3, 4, 3, 2, 3, 2, 1, 2, 3, 4, 3, 4, 3, 2, 1, 0]
        test = xml_search(refined_list, query_list, pclist)
        self.assert_(test[0] == 7)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO.StringIO()
        xml_print(w, [1,2,3])
        self.assert_(w.getvalue() == "3\n1\n2\n3")

    def test_print_2(self):
        w = StringIO.StringIO()
        xml_print(w, [1, 7])
        self.assert_(w.getvalue() == "2\n1\n7")

    def test_print_3(self):
        w = StringIO.StringIO()
        xml_print(w, [])
        self.assert_(w.getvalue() == "0")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO.StringIO('<Team>\n<Dragon></Dragon>\n<Cooly></Cooly>\n</Team>\n<Team><Dragon></Dragon></Team>')
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == '1\n1')

    def test_solve_2(self):
        r = StringIO.StringIO('<THU>\n<Team>\n<Dragon></Dragon>\n<Cooly></Cooly>\n</Team>\n<JiaJia>\n<Team>\n<ACRush><Cooly></Cooly></ACRush>\n</Team>\n</JiaJia>\n</THU><Team><Dragon></Dragon></Team>')
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == '1\n1')

    def test_solve_2(self):
        r = StringIO.StringIO('<Team><Cooly><Dragon></Dragon></Cooly></Team><Team><Dragon></Dragon></Team>')
        w = StringIO.StringIO()
        xml_solve(r, w)
        self.assert_(w.getvalue() == '0')

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
