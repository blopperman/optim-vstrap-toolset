import unittest
import sys

sys.path.append('../.')

from toolset.mesh import Mesh
from toolset.mesh import Cell
from toolset.mesh import Node

class MeshTest(unittest.TestCase):
    def test_read_from_xml(self):
        mesh = Mesh()
        execption = False

        try:
            mesh.read_from_xml('test_data/cube.xml')
        except Exception as e:
            print(e)
            execption = True

        self.assertTrue(not execption)
        self.assertTrue(1.0 - mesh.volume < 0.001)

class CellTest(unittest.TestCase):
    def test_calc_volume(self):
        cell = Cell()
        node1 = Node(1, (0.0, 0.0, 0.0))
        node2 = Node(2, (1.0, 0.0, 0.0))
        node3 = Node(3, (0.0, 1.0, 0.0))
        node4 = Node(4, (0.0, 0.0, 1.0))
        nodes = (node1, node2, node3, node4)

        cell.type = 4
        volume = cell.calc_volume(nodes)

        self.assertEqual(1.0/6.0, volume)