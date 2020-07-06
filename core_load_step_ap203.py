##Copyright 2010-2017 Thomas Paviot (tpaviot@gmail.com)
##
##This file is part of pythonOCC.
##
##pythonOCC is free software: you can redistribute it and/or modify
##it under the terms of the GNU Lesser General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##pythonOCC is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Lesser General Public License for more details.
##
##You should have received a copy of the GNU Lesser General Public License
##along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

import random
import os
import os.path
import sys
import threading

from OCC.Core.Quantity import Quantity_Color, Quantity_TOC_RGB
from OCC.Display.SimpleGui import init_display

from OCC.Extend.TopologyUtils import TopologyExplorer
from OCC.Extend.DataExchange import read_step_file as readstep

def import_as_one_shape(event = None):
    # shp = read_step_file(os.path.join('..', 'assets', 'models', 'as1_pe_203.stp'))
    shp = readstep(os.path.join('Torch Assembly.STEP'))
    display.EraseAll()
    display.DisplayShape(shp, update = True)

def import_as_multiple_shapes(event = None):
    # compound = read_step_file(os.path.join('..', 'assets', 'models', 'as1_pe_203.stp'))
    compound = readstep(os.path.join('Torch Assembly.STEP'))
    t = TopologyExplorer(compound)
    display.EraseAll()
    for solid in t.solids():
        color = Quantity_Color(random.random(),
                               random.random(),
                               random.random(),
                               Quantity_TOC_RGB)
        display.DisplayColoredShape(solid, color)

    display.FitAll()

def save_to_image(event = None):
    print('Saving image to file')
    display.ExportToImage('image.png')


def exit(event = None):
    sys.exit()


if __name__ == '__main__':
    display, start_display, add_menu, add_function_to_menu = init_display('wx')
    add_menu('STEP import')
    add_function_to_menu('STEP import', import_as_one_shape)
    add_function_to_menu('STEP import', import_as_multiple_shapes)
    add_function_to_menu('STEP import', save_to_image)
    # add_function_to_menu('STEP import', exit)
    
    display.View_Iso()
    start_display()
    
    # t1 = threading.Thread(target = start_display)
    # t1.start()
