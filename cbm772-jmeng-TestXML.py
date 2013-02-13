#!/usr/bin/env python

"""
To test the program:
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
  # -------
  # print 
  # -------

  def test_print_1(self):
    w = StringIO.StringIO()
    res = [1]
    xml_print(w, res)
    self.assert_(w.getvalue() == "1\n1\n")

  def test_print_2(self):
    w = StringIO.StringIO()
    res = []
    xml_print(w, res)
    self.assert_(w.getvalue() == "0\n")

  def test_print_3(self):
    w = StringIO.StringIO()
    res = [1, 2, 3]
    xml_print(w, res)
    self.assert_(w.getvalue() == "3\n1\n2\n3\n")

  def test_print_4(self):
    w = StringIO.StringIO()
    res = [1, 2, 3, 6, 8, 19, 24]
    xml_print(w, res)
    self.assert_(w.getvalue() == "7\n1\n2\n3\n6\n8\n19\n24\n")

  # -----------
  # parseTree 
  # -----------

  def test_parseTree_1(self):
    xmlstr = """<a></a>"""
    root = ET.fromstring(xmlstr)
    taglst = []
    nodes = []
    parseTree(root, taglst, nodes)

    self.assert_(len(taglst) == 1)
    self.assert_(taglst[0] == 'a')
    self.assert_(len(nodes) == 1)
    self.assert_(nodes[0].tag == 'a')

  def test_parseTree_2(self):
    xmlstr = """<a><b></b></a>"""
    root = ET.fromstring(xmlstr)
    taglst = []
    nodes = []
    parseTree(root, taglst, nodes)

    self.assert_(len(taglst) == 2)
    self.assert_(taglst[0] == 'a')
    self.assert_(taglst[1] == 'b')
    self.assert_(len(nodes) == 2)
    self.assert_(nodes[0].tag == 'a')
    self.assert_(nodes[0][0].tag == 'b')
    self.assert_(nodes[1].tag == 'b')

  def test_parseTree_3(self):
    xmlstr = """<a></a>"""
    root = ET.fromstring(xmlstr)
    taglst = []
    nodes = []
    parseTree(root, taglst, nodes)

    self.assert_(len(taglst) == 1)
    self.assert_(taglst[0] == 'a')
    self.assert_(len(nodes) == 1)
    self.assert_(nodes[0].tag == 'a')

  def test_parseTree_4(self):
    xmlstr = """<a><b><c></c><d></d><e><f></f></e></b></a>"""
    root = ET.fromstring(xmlstr)
    taglst = []
    nodes = []
    parseTree(root, taglst, nodes)

    self.assert_(len(taglst) == 6)
    self.assert_(taglst[0] == 'a')
    self.assert_(taglst[1] == 'b')
    self.assert_(taglst[2] == 'c')
    self.assert_(taglst[3] == 'd')
    self.assert_(taglst[4] == 'e')
    self.assert_(taglst[5] == 'f')
    self.assert_(len(nodes) == 6)
    self.assert_(nodes[0].tag == 'a')
    self.assert_(nodes[1].tag == 'b')
    self.assert_(nodes[2].tag == 'c')
    self.assert_(nodes[3].tag == 'd')
    self.assert_(nodes[4].tag == 'e')
    self.assert_(nodes[5].tag == 'f')

  # --------
  # dfs_new 
  # --------

  def test_dfs_new_1(self):
    xmlstr1 = """<a></a>"""
    root1 = ET.fromstring(xmlstr1)
    xmlstr2 = """<a></a>"""
    root2 = ET.fromstring(xmlstr2)
    self.assert_(dfs_new(root1, root2))

  def test_dfs_new_2(self):
    xmlstr1 = """<a><b></b></a>"""
    root1 = ET.fromstring(xmlstr1)
    xmlstr2 = """<a><c></c></a>"""
    root2 = ET.fromstring(xmlstr2)
    self.assert_(not dfs_new(root1, root2))

  def test_dfs_new_3(self):
    xmlstr1 = """<a><b><d></d></b><c></c></a>"""
    root1 = ET.fromstring(xmlstr1)
    xmlstr2 = """<a><b></b><c></c></a>"""
    root2 = ET.fromstring(xmlstr2)
    self.assert_(dfs_new(root1, root2))

  def test_dfs_new_4(self):
    xmlstr1 = """<a><b><d></d></b><c></c></a>"""
    root1 = ET.fromstring(xmlstr1)
    xmlstr2 = """<a><b></b><c></c></a>"""
    root2 = ET.fromstring(xmlstr2)
    self.assert_(not dfs_new(root2, root1))

  

  # -----
  # solve
  # -----

  def test_solve_1(self):
    r = StringIO.StringIO("<t></t>\n<t></t>\n")
    w = StringIO.StringIO()
    xml_solve(r, w)
    self.assert_(w.getvalue() == "1\n1\n")

  def test_solve_2(self):
    r = StringIO.StringIO("<t></t>\n<s></s>\n")
    w = StringIO.StringIO()
    xml_solve(r, w)
    self.assert_(w.getvalue() == "0\n")

  def test_solve_3(self):
    r = StringIO.StringIO("""
      <t1>
        <t2>
          <t3></t3>
          <t4></t4>
        </t2>
        <t5>
          <t2>
            <t4><t6></t6></t4>
            <t3></t3>
          </t2>
        </t5>
      </t1>

      <t2>
        <t4><t6></t6></t4>
        <t3></t3>
      </t2>
      """)
    w = StringIO.StringIO()
    xml_solve(r, w)
    self.assert_(w.getvalue() == "1\n6\n")

  def test_solve_4(self):
    r = StringIO.StringIO("<t><s></s></t>\n<s><u></u></s>\n")
    w = StringIO.StringIO()
    xml_solve(r, w)
    self.assert_(w.getvalue() == "0\n")

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
