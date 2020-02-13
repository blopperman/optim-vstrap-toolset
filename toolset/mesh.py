import xml.etree.ElementTree as ET

class Node:
    def __init__(self):
        self.id = 0
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.value = (0, 0, 0)

class Cell:
    def __init__(self, id, nodes = []):
        self.id = id
        self.nodes_ids = []
        self.value = (0, 0, 0)
        self.volume = 0.0

    def set_nodes(self, nodes):
        for node in nodes:
            self.nodes_ids.append(node.id)

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
        self.clear()
        tree = ET.parse(file_name)
        root = tree.getroot()
