
# -------
# imports
# -------

import StringIO
import unittest
import xml.etree.ElementTree as ET

from XML import compareNode, getNodeNum, getXMLText, solve

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # getXMLText
    # ----

    def test_getXMLText_1 (self) :
        r = StringIO.StringIO("<THU></THU><aa></aa>")
        t = getXMLText( r )
        self.assert_(t == "<root><THU></THU><aa></aa></root>")

    def test_getXMLText_2 (self) :
        r = StringIO.StringIO("<THU><aa></aa></THU><aa></aa>  \t\n")
        t = getXMLText( r )
        self.assert_(t == "<root><THU><aa></aa></THU><aa></aa></root>")

    def test_getXMLText_3 (self) :
        r = StringIO.StringIO("   <THU>\n\t\t\t<aa>\n\t\t\t</aa>\n</THU>\n<aa>\n</aa>  \t\n")
        t = getXMLText( r )
        self.assert_(t == "<root><THU><aa></aa></THU><aa></aa></root>")


    # ----
    # compareNode
    # ----

    def test_compareNode_1 (self) :
        xml = ET.fromstring ( "<root><THU></THU><THU></THU></root>" )
        root = xml [ 0 ]
        search = xml [ 1 ]
        xml.remove ( xml [ 1 ] )
        foundNodes = xml.findall ( ".//" + search.tag )
        equal = compareNode ( foundNodes [ 0 ], search )
        self.assert_(equal == True)

    def test_compareNode_2 (self) :
        xml = ET.fromstring ( "<root><THU></THU><THU><a></a></THU></root>" )
        root = xml [ 0 ]
        search = xml [ 1 ]
        xml.remove ( xml [ 1 ] )
        foundNodes = xml.findall ( ".//" + search.tag )
        equal = compareNode ( foundNodes [ 0 ], search )
        self.assert_(equal == False)

    def test_compareNode_3 (self) :
        xml = ET.fromstring ( "<root><THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team><Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team></root>" )
        root = xml [ 0 ]
        search = xml [ 1 ]
        xml.remove ( xml [ 1 ] )
        foundNodes = xml.findall ( ".//" + search.tag )
        equal1 = compareNode ( foundNodes [ 0 ], search )
        equal2 = compareNode ( foundNodes [ 1 ], search )
        self.assert_(equal1 == True)
        self.assert_(equal2 == True)
        
        
    # -----
    # getNodeNum
    # -----

    def test_getNodeNum_1 (self) :
        global nodeCount
        xml = ET.fromstring ( "<root><THU></THU><THU></THU></root>" )
        root = xml [ 0 ]
        search = xml [ 1 ]
        xml.remove ( xml [ 1 ] )
        m = root
        id = getNodeNum ( m, root )
        self.assert_(id == 1)

    def test_getNodeNum_2 (self) :
        global nodeCount
        xml = ET.fromstring ( "<root><THU><aa></aa><b><c></c></b></THU><aa></aa></root>" )
        root = xml [ 0 ]
        search = xml [ 1 ]
        xml.remove ( xml [ 1 ] )
        m = root [ 0 ]
        id = getNodeNum ( m, root )
        self.assert_(id == 2)

    def test_getNodeNum_2 (self) :
        global nodeCount
        xml = ET.fromstring ( "<root><THU><g></g><aa></aa><b><c><e></e></c><d><f></f></d></b></THU><b><c></c><d></d></b></root>" )
        root = xml [ 0 ]
        search = xml [ 1 ]
        xml.remove ( xml [ 1 ] )
        m = root [ 2 ]
        id = getNodeNum ( m, root )
        self.assert_(id == 4)

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("<THU></THU><aa></aa>  ")
        w = StringIO.StringIO()
        solve(r, w)
        self.assert_(w.getvalue() == "0\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("<THU><g></g><aa></aa><b><c><e></e></c><d><f></f></d></b></THU><b><c></c><d></d></b>")
        w = StringIO.StringIO()
        solve(r, w)
        self.assert_(w.getvalue() == "1\n4\n")
        
    def test_solve_3 (self) :
        r = StringIO.StringIO("<THU><Team><ACRush></ACRush><Jelly></Jelly><Cooly></Cooly></Team><JiaJia><Team>" +
                              "<Ahyangyi></Ahyangyi><Dragon></Dragon><Cooly><Amber></Amber></Cooly></Team></JiaJia></THU><Team><Cooly></Cooly></Team>")
        w = StringIO.StringIO()
        solve(r, w)
        self.assert_(w.getvalue() == "2\n2\n7\n")

# ----
# main
# ----

print ("TestXML.py")
unittest.main()
print ("Done.")
