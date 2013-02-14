#!/usr/bin/env python

# -------------------------------
# TestXML.py
# Copyright (C) 2013
# Carlos Balderas and William Generous
# -------------------------------

"""
To test the program:
    % python TestXML.py >& TestXML.out
    % chmod ugo+x TestXML.py
    % TestXML.py >& TestXML.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from XML import xml_read, xml_eval, xml_dictionary, xml_print, xml_solve

# -----------
# TestXML
# -----------




class TestXML (unittest.TestCase):


##################
##xml_dictionary##
##################


  def test_dictionary_1(self):
    a = ['<Cooly><Amber></Cooly></Amber>']
    b = [12]
    master={}
    xml_dictionary(a, b, master)
    self.assert_(master == {12 :'<Cooly><Amber></Cooly></Amber>'})

  def test_dictionary_2(self):
    a = ['<PillBox><OmegaFi></OmegaFi><PhiDelt></PhiDelt></PillBox>']
    b = [3]
    master={}
    xml_dictionary(a, b, master)
    self.assert_(master == {3 :'<PillBox><OmegaFi></OmegaFi><PhiDelt></PhiDelt></PillBox>'})

  def test_dictionary_3(self):
    a = ['<a><b><c><d><e></e></d></c></b></a>']
    b = [5]
    master={}
    xml_dictionary(a, b, master)
    self.assert_(master == {5:'<a><b><c><d><e></e></d></c></b></a>'})

  def test_dictionary_4(self):
    a = ['<Yuchen>']
    b = [1]
    master={}
    xml_dictionary(a, b, master)
    self.assert_(master == {1:'<Yuchen>'})


############
##xml_eval##
############


  def test_eval_1(self):
    master = {1:'<AIDS>',2:'<Team>',3:'<Death></Death>',4:'</Team>',5:'</AIDS>',6:'<Team><Death></Death></Team>'}
    line_num = 6
    iter, line_num_array = xml_eval(master, line_num)
    self.assert_(iter != 1)
    self.assert_(line_num_array != [2])

    
  def test_eval_2(self):
    master = {1:'<AIDS>',2:'<Team></Team',3:'</AIDS>',4:'<Team></Team>',5:'<Team></Team>'}
    line_num = 5
    iter, line_num_array = xml_eval(master, line_num)
    self.assert_(iter != 1)
    self.assert_(line_num_array != [2])


  def test_eval_3(self):
    master = {1:'<Banana>',2:'<Hi>',3:'<Death></Death>',4:'<Team></Team>',5:'</HI>',6:'<Hi>',7:'<Death></Death',8:'</Hi>',9:'</Banana>',10:'<Hi><Death></Death></Hi>'}
    line_num = 10
    iter, line_num_array = xml_eval(master, line_num)
    self.assert_(iter != 2)
    self.assert_(line_num_array != [2,6])  


#############
##xml_print##
#############


  def test_print_1(self):
    w = StringIO.StringIO()
    xml_print(w, 3, [2,7,11])
    self.assert_(w.getvalue() == "3\n2\n7\n11\n")

  def test_print_2(self):
    w = StringIO.StringIO()
    xml_print(w, 2, [1,8])
    self.assert_(w.getvalue() == "2\n1\n8\n")

  def test_print_3(self):
    w = StringIO.StringIO()
    xml_print(w, 5, [1,5,8,11,15])
    self.assert_(w.getvalue() == "5\n1\n5\n8\n11\n15\n")

  def test_print_4(self):
    w = StringIO.StringIO()
    xml_print(w, 1, [5])
    self.assert_(w.getvalue() == "1\n5\n")


#############
##xml_solve##
#############


  def test_solve_1(self):
    r = StringIO.StringIO("<Team><Cooly></Cooly><Amber></Amber></Team>\n<Team><Cooly></Cooly></Team>\n")
    w = StringIO.StringIO()
    xml_solve(r,w)
    self.assert_(r != None)

  def test_solve_2(self):
    r = StringIO.StringIO("<StarWars>/n<Wookiee></Wookiee>/n<Jedi></Jedi>/n</StarWars>")
    w = StringIO.StringIO()
    xml_solve(r,w)
    self.assert_(r != None)

  def test_solve_3(self):
    r = StringIO.StringIO("<THU>/n</THU>")
    w = StringIO.StringIO()
    xml_solve(r,w)
    self.assert_(r != None)

  def test_solve_4(self):
    r = StringIO.StringIO("<THU>/n</THU>")
    w = StringIO.StringIO()
    xml_solve(r,w)
    self.assert_(r != None)


##############
## xml_read ##
##############


  def test_read_1(self):
    r = StringIO.StringIO("<Cooly><Amber></Cooly></Amber>")
    a = [0]
    xml_read(r,a)
    self.assert_(r != None)

  def test_read_2(self):
    r = StringIO.StringIO("<steams><sd></sd></steams")
    a = [0]
    xml_read(r,a)
    self.assert_( r != None)

  def test_read_3(self):
    r = StringIO.StringIO("<Banana></Banana><Glasses><Speaker></Glasses></Speaker>")
    a = [0]
    xml_read(r,a)
    self.assert_(r != None)

  def test_read_3(self):
    r = StringIO.StringIO("<team></team")
    a = [0]
    xml_read(r,a)
    self.assert_(r != None)

  

# ---
# main
# ---

print "TestXML.py"
unittest.main()
print "Done."