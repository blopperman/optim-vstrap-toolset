import xml.etree.ElementTree as ET

class Node:
    def __init__(self):
        self.id = 0
        self.x_coord = 0.0
        self.y_coord = 0.0
        self.z_coord = 0.0
        self.value = (0, 0, 0)

class Cell:
    def __init__(self):
        self.id = 0
        self.nodes_ids = []
        self.value = (0, 0, 0)
        self.volume = 0.0

    def set_nodes(self, nodes):
        for node in nodes:
            self.nodes_ids.append(node.id)

        self.__calc_volume(nodes)

    def __calc_volume(self, nodes):
        pass

class Mesh:
    def __init__(self):
        self.cells = []
        self.nodes = {}

    def __str__(self):
        str = ""
        str += "CELLS:\n"
        str += "NODES:"

        return str

    def clear(self):
        self.cells = []
        self.nodes = {}

    def read_from_xml(self, file_name):
        tree = ET.parse(file_name)
        root = tree.getroot()

        self.clear()
        self.__check_mesh_file(root)
        self.__create_nodes(root)
        self.__create_cells(root)

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
            cell.set_nodes(nodes)

    def __get_node_ids(self, text):
        node_ids = []

        for str in text.split(','):
            node_ids.append(int(str))

        return node_ids
