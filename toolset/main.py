#!/usr/bin/env python3

import argparse
import xml.etree.ElementTree as ET

class Node:
    def __init__(self):
        self.id = 0
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.value = (0, 0, 0)

class Cell:
    def __init__(self, id, nodes_ids = []):
        self.id = id
        self.nodes_ids = nodes_ids
        self.value = (0, 0, 0)

class Mesh:
    def __init__(self):
        self.cells = []
        self.nodes = {}

def convert_mesh_file(file_name):
    mesh = Mesh()
    tree = ET.parse(file_name)
    root = tree.getroot()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Mesh data interpolation script", description='Reads mesh and control file. Interpolates control defined in cells to mesh nodes.')
    parser.add_argument('mesh', type=str, help='path to the mesh file')
    parser.add_argument('control', type=str, help='path to the control file')

    args = parser.parse_args()

    try:
        convert_mesh_file(args.mesh)
    except Exception as e:
        print(e)
        exit()
