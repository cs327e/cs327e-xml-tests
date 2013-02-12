#!/usr/bin/env python

# ---------------------------
# XML.py
# Copyright (C) 2013
# Xiaolong Li & Shirley Li
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

from XML import *

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----------
    # xml_read
    # ----------
    
    def test_xml_read_1 (self) :
      reader = StringIO.StringIO("<html>\n\t"
            "<head> </head>\n\t<body></body>\n</html>")
      token_list = xml_read(reader)
      self.assert_(token_list == ["html", "head", "/head", 
            "body", "/body", "/html"])
    
    def test_xml_read_2 (self) :
      reader = StringIO.StringIO("<Team><Cooly></Cooly></Team>")
      token_list = xml_read(reader)
      self.assert_(token_list == ["Team", "Cooly", "/Cooly", "/Team"])
            
    def test_xml_read_3 (self) :
      reader = StringIO.StringIO("<silly>       \t\n </silly>\t\n")
      token_list = xml_read(reader)
      self.assert_(token_list == ["silly", "/silly"])
      
    # ----------
    # xml_create_dict
    # ----------
    
    def test_xml_create_dict_1 (self) :
      token_list = ["Team", "Cooly", "/Cooly", "/Team"]
      dict_list = xml_create_dict(token_list)
      self.assert_(len(dict_list) == 1)
      self.assert_(dict_list[0] ==
            {"Team": [1, {"Cooly": [2, {}]}]})
            
    def test_xml_create_dict_2 (self) :
      token_list = ["THU", "Team", "ACRush", "/ACRush", "Jelly",
            "/Jelly", "Cooly", "/Cooly", "/Team", "JiaJia", "Team",
            "Ahyangyi", "/Ahyangyi", "Dragon", "/Dragon", "Cooly",
            "Amber", "/Amber", "/Cooly", "/Team", "/JiaJia", "/THU",
            "Team", "Cooly", "/Cooly", "/Team"]
      dict_list = xml_create_dict(token_list)
      self.assert_(len(dict_list) == 2)
      self.assert_(dict_list[0] ==
            {"THU":[1, {"Team":[2, {"ACRush":[3, {}], "Jelly":[4, {}],
            "Cooly": [5, {}]}], "JiaJia":[6, {"Team":[7, {"Ahyangyi":
            [8, {}], "Dragon": [9, {}], "Cooly":[10, {"Amber": [11, {}
            ]}]}]}]}]})
      self.assert_(dict_list[1] ==
            {"Team": [1, {"Cooly": [2, {}]}]})
            
    def test_xml_create_dict_3 (self) :
      token_list = ["html", "head", "/head", "body", "/body", "/html",
            "body", "/body"]
      dict_list = xml_create_dict(token_list)
      self.assert_(len(dict_list) == 2)
      self.assert_(dict_list[0] ==
            {"html":[1, {"head":[2, {}], "body":[3, {}]}]})
      self.assert_(dict_list[1] ==
            {"body":[1, {}]})
    
    # ----------
    # xml_match
    # ----------
    
    def test_xml_match_1 (self) :
      # false case
      tree = {"Team":[1, {"Hotty":[2, {"Cooly":[3, {}]}]}]}
      pattern = {"Team": [1, {"Cooly": [2, {}]}]}
      self.assert_(xml_match(tree, pattern) == False)
    
    def test_xml_match_2 (self) :
      # false case
      tree = {"html":[1, {"head":[2, {}], "foot":[3, {}]}]}
      pattern = {"html":[1, {"head":[2, {}], "body":[3, {}]}]}
      self.assert_(xml_match(tree, pattern) == False)
      
    def test_xml_match_3 (self) :
      # true case
      tree = {"Team":[2, {"ACRush":[3, {}], "Jelly":[4, {}],
            "Cooly": [5, {}]}]}
      pattern = {"Team": [1, {"Cooly": [2, {}]}]}
      self.assert_(xml_match(tree, pattern) == True)    
      
    def test_xml_match_4 (self) :
      # true case
      tree = {"Team":[7, {"Ahyangyi":[8, {}], "Dragon": [9, {}], 
            "Cooly":[10, {"Amber": [11, {}]}]}]}
      pattern = {"Team": [1, {"Cooly": [2, {}]}]}
      self.assert_(xml_match(tree, pattern) == True)    
      
    # ----------
    # xml_match
    # ----------
    
    def test_xml_match_all_1 (self) :
      # no match case
      tree = {"THU":[1, {"Team":[2, {"ACRush":[3, {}], "Jelly":[4, {}],
            "Cooly": [5, {}]}], "JiaJia":[6, {"Team":[7, {"Ahyangyi":
            [8, {}], "Dragon": [9, {}], "Cooly":[10, {"Amber": [11, {}
            ]}]}]}]}]}
      pattern = {"Hi":[1, {}]}
      self.assert_(xml_linked2list(xml_match_all(tree, pattern)[0]) == [])      
      
    def test_xml_match_all_2 (self) :
      # no match case
      tree = {"THU":[1, {"Team":[2, {"ACRush":[3, {}], "Jelly":[4, {}],
            "Cooly": [5, {}]}], "JiaJia":[6, {"Team":[7, {"Ahyangyi":
            [8, {}], "Dragon": [9, {}], "Cooly":[10, {"Amber": [11, {}
            ]}]}]}]}]}
      pattern = {"ACRush":[1, {}]}
      self.assert_(xml_linked2list(xml_match_all(tree, pattern)[0]) == [3])

    def test_xml_match_all_3 (self) :
      # no match case
      tree = {"THU":[1, {"Team":[2, {"ACRush":[3, {}], "Jelly":[4, {}],
            "Cooly": [5, {}]}], "JiaJia":[6, {"Team":[7, {"Ahyangyi":
            [8, {}], "Dragon": [9, {}], "Cooly":[10, {"Amber": [11, {}
            ]}]}]}]}]}
      pattern = {"Team": [1, {"Cooly": [2, {}]}]}
      l = xml_linked2list(xml_match_all(tree, pattern)[0])
      l.sort()
      self.assert_(l == [2, 7])         

    # ----------
    # xml_solve
    # ----------
    
    def test_xml_solve_1 (self) :
      reader = StringIO.StringIO("<html>\n\t"
            "<head> </head>\n\t<body></body>\n</html><body></body>")
      writer = StringIO.StringIO()
      xml_solve(reader, writer)
      self.assert_(writer.getvalue() == "1\n3\n")
          
    def test_xml_solve_2 (self) :
      reader = StringIO.StringIO("""<THU>
                                      <Team>
                                        <ACRush></ACRush>
                                        <Jelly></Jelly>
                                        <Cooly></Cooly>
                                      </Team>
                                      <JiaJia>
                                        <Team>
                                          <Ahyangyi></Ahyangyi>
                                          <Dragon></Dragon>
                                          <Cooly><Amber></Amber></Cooly>
                                        </Team>
                                      </JiaJia>
                                    </THU>
                                    <Team><Cooly></Cooly></Team>""")
      writer = StringIO.StringIO()
      xml_solve(reader, writer)
      self.assert_(writer.getvalue() == "2\n2\n7\n")   
      
    def test_xml_solve_3 (self) :
      reader = StringIO.StringIO("""<THU>
                                      <Team>
                                        <ACRush></ACRush>
                                        <Jelly></Jelly>
                                        <Cooly></Cooly>
                                      </Team>
                                      <JiaJia>
                                        <Team>
                                          <Ahyangyi></Ahyangyi>
                                          <Dragon></Dragon>
                                          <Amber><Cooly></Cooly></Amber>
                                        </Team>
                                      </JiaJia>
                                    </THU>
                                    <Team><Cooly></Cooly></Team>""")
      writer = StringIO.StringIO()
      xml_solve(reader, writer)
      self.assert_(writer.getvalue() == "1\n2\n")
      
    def test_xml_solve_4 (self) :
      reader = StringIO.StringIO("""<Team><Cooly></Cooly></Team>
                                    <THU>
                                      <Team>
                                        <ACRush></ACRush>
                                        <Jelly></Jelly>
                                        <Cooly></Cooly>
                                      </Team>
                                      <JiaJia>
                                        <Team>
                                          <Ahyangyi></Ahyangyi>
                                          <Dragon></Dragon>
                                          <Amber><Cooly></Cooly></Amber>
                                        </Team>
                                      </JiaJia>
                                    </THU>""")
      writer = StringIO.StringIO()
      xml_solve(reader, writer)
      self.assert_(writer.getvalue() == "0\n")
      
    def test_xml_solve_5 (self) :
      reader = StringIO.StringIO("""<Team><Cooly></Cooly></Team>
                                    <Team><Cooly></Cooly></Team>""")
      writer = StringIO.StringIO()
      xml_solve(reader, writer)
      self.assert_(writer.getvalue() == "1\n1\n")
      
# ----
# main
# ----

print ("TestXML.py")
unittest.main()
print ("Done.")
