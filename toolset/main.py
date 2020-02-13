#!/usr/bin/env python3

import argparse
import xml.etree.ElementTree as ET

from mesh import*

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
