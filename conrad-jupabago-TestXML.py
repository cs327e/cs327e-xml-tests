# -------
# imports
# -------

import StringIO
import io
import unittest

from XML import *

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase):
  #              1   2    3            4            5                   6        7     8                            
  seed_data = "<thu><team><abby></abby><john></john><paul></paul></team><taketwo><team><abby></abby></team></taketwo><team></team></thu>"
  seed_query = "<team><abby></abby></team>"

  def test_findChild_1(self):
    data = ET.fromstring(self.seed_data)
    query = ET.fromstring(self.seed_query)

    array = []
    for c in findChild(data, query):
      array.append(c)
    self.assertTrue(array.__len__() == 3)
  
  def test_findChild_2(self):
    data = ET.fromstring(self.seed_data)
    query = ET.fromstring("<abby></abby>")

    expected_result = [3,8] 
    array = []
    for c in findChild(data, query):
      array.append(c)
    for i in range(array.__len__()):
      self.assertTrue(array[i][0]==expected_result[i])
  
  def test_findChild_3(self):
    data = ET.fromstring(self.seed_data)
    query = ET.fromstring("<notfound></notfound>")

    array = []
    for c in findChild(data, query):
      array.append(c)
    self.assertTrue(array.__len__() == 0)
  
  def test_findRecursive_1(self):
    data = ET.fromstring(self.seed_data)
    query = ET.fromstring("<notfound><pretend></pretend></notfound>")
    r = findRecursive(data,query)
    self.assertTrue(r is False)
  
  def test_findRecursive_2(self):
    data = ET.fromstring(self.seed_data)
    query = ET.fromstring(self.seed_query)
    r = findRecursive(data,query)
    self.assertTrue(r)

  def test_findRecursive_3(self):
    data = ET.fromstring("<empty></empty>")
    query = ET.fromstring("<empty></empty>")
    r = findRecursive(data,query)
    self.assertTrue(r)

  def test_findAll_1(self):
    expected_result = [2,7] 
    array = findAll(self.seed_data, self.seed_query)

    self.assertTrue(len(array)==len(expected_result))
    for i in range(array.__len__()):
      self.assertTrue(array[i]==expected_result[i])   

  def test_findAll_2(self):
    array = findAll("<nothing></nothing>","<blah></blah>")
    expected_result = []

    self.assertTrue(len(array)==len(expected_result))
    for i in range(array.__len__()):
      self.assertTrue(array[i]==expected_result[i])

  def test_findAll_3(self):
    array = findAll("<one-result><a><insideof><a></a></insideof></a></one-result>","<a></a>")
    expected_result = [2,4]

    self.assertTrue(len(array)==len(expected_result))
    for i in range(array.__len__()):
      self.assertTrue(array[i]==expected_result[i])

  def test_print1 (self) :
    w = StringIO.StringIO()
    results = [2,7]
    xml_print(w,results)
    self.assert_(w.getvalue() == "2\n2\n7\n\n")

  def test_print2 (self) :
    w = StringIO.StringIO()
    results = []
    xml_print(w,results)
    self.assert_(w.getvalue() == "0\n\n")

  def test_print3 (self) :
    w = StringIO.StringIO()
    results = [2,7,3,5,6,7,7,8]
    xml_print(w,results)
    self.assert_(w.getvalue() == "8\n2\n7\n3\n5\n6\n7\n7\n8\n\n")

  def test_xml_read1(self):
    r = StringIO.StringIO("")
    b = xml_read(r)
    self.assert_(b=="")
  
  def test_xml_read2(self):
    r = StringIO.StringIO("1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n\n")
    b = xml_read(r)
    self.assert_(b=="111111111111")
  
  def test_xml_read3(self):
    r = StringIO.StringIO("<a><b><c><d></d></c></b></a>\n<b><d></d></b>")
    b = xml_read(r)
    self.assert_(b=="<a><b><c><d></d></c></b></a><b><d></d></b>")
 
  def test_xml_solve1(self):
    r = StringIO.StringIO("<a><b><c><d></d></c></b></a>\n<b><d></d></b>")          
    w = StringIO.StringIO()
    xml_solve(r, w)
    self.assert_(w.getvalue()=="1\n2\n\n")

  def test_xml_solve2(self):
    r = StringIO.StringIO("<a></a><a></a>")          
    w = StringIO.StringIO()
    xml_solve(r, w)
    self.assert_(w.getvalue()=="1\n1\n\n")

  def test_xml_solve3(self):
    r = StringIO.StringIO("<a></a><b></b>")          
    w = StringIO.StringIO()
    xml_solve(r, w)
    self.assert_(w.getvalue()=="0\n\n")


# ----
# main
# ----

print ("TestXML.py")
unittest.main()
print ("Done.")
