# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:38:00 2020

@author: prehr
"""

import sys, threading

# Path to FreeCAD
FREECADPATH = "C:/Users/prehr/Anaconda3/envs/p36/Library/bin"
def import_freecad(path_freecad):
    """Try to import FreeCAD on path_freecad"""
    sys.path.append(path_freecad)
    try:
        import FreeCAD, FreeCADGui
        print("FreeCAD and FreeCADGui imported")
    except Exception as e:
        print(e)
        print("Could not import FreeCAD")

import_freecad(FREECADPATH)

# import freecad
# import FreeCADGui

FreeCADGui.showMainWindow()
FreeCADGui.updateGui()
print('hi')
# t1 = threading.Thread(target = FreeCADGui.updateGui)
# t1.start()

