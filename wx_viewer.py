# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from OCCT.Graphic3d import Graphic3d_NOM_ALUMINIUM
from OCCT.STEPControl import STEPControl_Reader
from OCCT.IFSelect import IFSelect_RetDone, IFSelect_GeneralInfo, IFSelect_EntitiesByItem, IFSelect_ItemsByEntity, IFSelect_CountByItem, IFSelect_ListByItem
from OCCT.TopAbs import TopAbs_FACE
from OCCT.TopExp import TopExp_Explorer

from OCCT.Visualization.WxViewer import ViewerWx
print('imported')

reader = STEPControl_Reader()
tr = reader.WS().TransferReader()
reader.ReadFile('Torch Assembly.STEP')
# failsonly = False
# items_list = reader.PrintCount(failsonly, IFSelect_GeneralInfo)
# print(items_list)
print('Loaded file')
reader.TransferRoots()

no_shapes = reader.NbShapes()
no_roots = reader.NbRootsForTransfer()
# items = reader.IFSelect_PrintCount()
print('Number of shapes = ', no_shapes)
print('Number of roots  = ', no_roots)
shape = reader.OneShape()

v = ViewerWx()
# v.display_shape(shape, rgb=(0.5, 0.5, 0.5), material=Graphic3d_NOM_ALUMINIUM)

exp = TopExp_Explorer(shape, TopAbs_FACE)
while exp.More():
    rgb = None
    s = exp.Current()
    exp.Next()
    item = tr.EntityFromShapeResult(s, 1)
    name = item
    if name:
        print('Found entity: {}'.format(name))
        rgb = (1, 0, 0)
    v.add(s, rgb)
    
v.start()