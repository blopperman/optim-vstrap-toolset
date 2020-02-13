import unittest
import sys

sys.path.append('../.')

from toolset.mesh import Mesh

class MeshTest(unittest.TestCase):
    def test_read_from_xml(self):
        mesh = Mesh()
        execption = False

        try:
            mesh.read_from_xml('test_data/box_vol_regular_refined.xml')
        except:
            execption = True

        self.assertTrue(not execption)
