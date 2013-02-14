#-----------------
# XML Project #2
#-----------------
# Annie Wu
# Cathy Egboh
#-----------------

import StringIO
import unittest

from XML import xml_read, xml_find, xml_print, xml_search


class TestXML(unittest.TestCase):

  
  #---------
  # xml_read
  #---------
  def test_read_1(self):
    r = StringIO.StringIO(" <THU>")
    tagList = []
    levelList = []
    searchList = []
    x = xml_read(r, tagList, levelList, searchList)
    self.assert_(tagList == ["<THU>"])
    self.assert_(levelList == [1])
    self.assert_(searchList == [])

  def test_read_2(self):
    r = StringIO.StringIO("<THU>")
    tagList = []
    levelList = []
    searchList = []
    x = xml_read(r, tagList, levelList, searchList)
    self.assert_(tagList == ['<THU>'])
    self.assert_(levelList == [0])
    self.assert_(searchList == [])

  def test_read_3(self):
    r = StringIO.StringIO("   <THU><Team></Team></THU>\n<THU></THU>")
    tagList = []
    levelList = []
    searchList = []
    x = xml_read(r, tagList, levelList, searchList)
    self.assert_(tagList == ['<THU>', '<Team>'])
    self.assert_(levelList == [4, 4])
    self.assert_(searchList == ["<THU>"]) 


  # --------
  # xml_find
  # --------
  def test_xml_find1(self):
    tagList = ["<THU>", "<Team>", "<Cooly>"]
    levelList = [1, 2, 3]
    searchList = ["<Team>", "<Cooly>"]
    x = xml_find(tagList, levelList, searchList)
    self.assert_(x == [2])

  def test_xml_find2(self):
    tagList = ["<THU>", "<Team>", "<Cooly>", "<JiaJia>", "<Team>", "<Cooly>", "<Amber>"]
    levelList = [1, 2, 3, 2, 3, 4, 4]
    searchList = ["<Team>", "<Cooly>"]
    x = xml_find(tagList, levelList, searchList)
    self.assert_(x == [2, 5])

  def test_xml_find3(self):
    tagList = ["<THU>", "<Team>", "<Bob>", "<John>", "<JiaJia>", "<Team>", "<Tim>", "<7>"]
    levelList = [1,2,3,3,2,3,4,4]
    searchList = ["<Team>", "<7>"]
    x = xml_find(tagList, levelList, searchList)
  #  print x
    self.assert_(x == [6])

  # ---------
  # xml_print
  # ---------
  def test_xml_print1(self):
    w = StringIO.StringIO()
    lis = [3,6,11]
    xml_print(w, lis)
    self.assert_(w.getvalue() == "3\n3\n6\n11\n")

  def test_xml_print2(self):
    w = StringIO.StringIO()
    lis = [7,8,9,10]
    xml_print(w, lis)
    self.assert_(w.getvalue() == "4\n7\n8\n9\n10\n")

  def test_xml_print3(self):
    w = StringIO.StringIO()
    lis = []
    xml_print(w, lis)
    self.assert_(w.getvalue() == "0\n")
    
  # ----------
  # xml_search
  # ----------
  def test_xml_search1(self):
    r = StringIO.StringIO("<THU><Team></Team></THU>\n<Team></Team>")
    w = StringIO.StringIO()
    xml_search(r, w)
    self.assert_(w.getvalue() == "1\n2\n")

  def test_xml_search2(self):
    r = StringIO.StringIO("<THU><Team></Team></THU>\n<THU><Team></Team></THU>")
    w = StringIO.StringIO()
    xml_search(r, w)
    self.assert_(w.getvalue() == "1\n1\n")

  def test_xml_search3(self):
    r = StringIO.StringIO("<THU><Team></Team></THU>\n<Hello></Hello>\n<THU></THU>")
    w = StringIO.StringIO()
    xml_search(r, w)
    self.assert_(w.getvalue() == "1\n1\n")

print "TestXML.py"
unittest.main()
print "Done."
