#!/usr/bin/env python
# * coding: utf8 *
'''
repro.py
A module that contains code to show that desktop arcpy can print the WKT but propy cannot
'''

import arcpy
from os import path

cwd = path.join(path.dirname(path.realpath(__file__)), 'data.gdb')

with arcpy.da.SearchCursor(path.join(cwd, 'ErrorOnWKT'), ['OID@', 'SHAPE@WKT']) as cursor:
    for oid, wkt in cursor:
        print(oid)
