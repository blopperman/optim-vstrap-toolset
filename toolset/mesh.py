import xml.etree.ElementTree as ET
import numpy.matlib
import numpy as np
import math

class Node:
    def __init__(self, id = 0, coord = (0.0, 0.0, 0.0)):
        self.id = id
        self.x_coord = coord[0]
        self.y_coord = coord[1]
        self.z_coord = coord[2]
        self.value = (0, 0, 0)

    def get_position(self):
        return np.asarray([self.x_coord, self.y_coord, self.z_coord])

class Cell:
    def __init__(self):
        self.id = 0
        self.nodes_ids = []
        self.value = (0, 0, 0)
        self.volume = 0.0
        self.type = 0

    def set_nodes(self, nodes):
        for node in nodes:
            self.nodes_ids.append(node.id)

        self.volume = self.calc_volume(nodes)

    def calc_volume(self, nodes):
        if self.type == 2:
            # surface triangle
            pass
        elif self.type == 4:
            return self._calc_volume_tetrahedron(nodes)
        else:
            raise Exception(__name__, self.calc_volume.__name__, "Undefined volume calculation for type {}.".format(self.type))

    def _calc_volume_tetrahedron(self, nodes):
        point1 = nodes[0].get_position()
        point2 = nodes[1].get_position()
        point3 = nodes[2].get_position()
        point4 = nodes[3].get_position()

        diff1 = point1 - point4
        diff2 = point2 - point4
        diff3 = point3 - point4

        return abs(diff1.dot(np.cross(diff2, diff3)))/6.0

class Mesh:
    def __init__(self):
        self.cells = {}
        self.nodes = {}
        self.volume = 0.0

    def __str__(self):
        str = ""
        str += "CELLS:\n"
        str += "NODES:"

        return str

    def clear(self):
        self.cells = {}
        self.nodes = {}
        self.volume = 0.0

    def read_from_xml(self, file_name):
        tree = ET.parse(file_name)
        root = tree.getroot()

        self.clear()
        self.__check_mesh_file(root)
        self.__create_nodes(root)
        self.__create_cells(root)
        self.__calc_volume()

    def __check_mesh_file(self, root):
        mesh_node = root.find('mesh')
        mesh_type = mesh_node.get('mesh_type')

        if mesh_type != "volume_mesh":
            raise Exception(__name__, self.__check_mesh_file.__name__, 'volume_mesh not defined in file')

    def __create_nodes(self, root):
        for element in root.find('nodes').findall('node'):
            node = Node()

            node.id = int(element.get('node_number'))
            node.x_coord = float(element.get('x_coord'))
            node.y_coord = float(element.get('y_coord'))
            node.z_coord = float(element.get('z_coord'))

            if node.id not in self.nodes:
                self.nodes[node.id] = node
            else:
                raise Exception(__name__, self.__create_nodes.__name__, 'Node with id {} allready in list.'.format(node.id))

    def __create_cells(self, root):
        for element in root.find('elements').findall('element'):
            cell = Cell()
            node_ids = self.__get_node_ids(element.find('nodes').text)
            nodes = []

            for id in node_ids:
                nodes.append(self.nodes[id])

            cell.id = int(element.get('elem_number'))
            cell.type = int(element.get('elm_type'))
            cell.set_nodes(nodes)

            if cell.id not in self.cells:
                self.cells[cell.id] = cell
            else:
                raise Exception(__name__, self.__create_nodes.__name__, 'Cell with id {} allready in list.'.format(cell.id))

    def __get_node_ids(self, text):
        node_ids = []

        for str in text.split(','):
            node_ids.append(int(str))

        return node_ids

    def __calc_volume(self):
        self.volume = 0.0

        for id, cell in self.cells.items():
            if cell.volume != None:
                self.volume += cell.volume