# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 09:03:10 2020

@author: prehr
"""


from step_parse_5_4 import StepParse
from StrEmbed_5_4 import ShapeRenderer
a = StepParse()

file = '5 parts_{3,1},1.STEP'
# file = 'Torch Assembly.STEP'
# file = 'PARKING_TROLLEY.STEP'

a.load_step(file)
a.create_tree()
a.OCC_read_file(file)
a.OCC_link()

