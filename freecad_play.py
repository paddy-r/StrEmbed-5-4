# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:38:00 2020

@author: prehr
"""

import sys

# Path to FreeCAD
FREECADPATH = "C:/Users/prehr/AppData/Local/FreeCAD 0.18/bin"

def import_freecad(path_freecad):
    """Try to import FreeCAD on path_freecad"""
    sys.path.append(path_freecad)
    try:
        import FreeCAD
    except Exception as e:
        print(e)
        print("Could not import FreeCAD")

import_freecad(FREECADPATH)