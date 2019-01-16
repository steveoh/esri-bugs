#!/usr/bin/env python
# * coding: utf8 *
"""
repro.py
A module that makes a query layer
"""


import arcpy
from os import path


SDE_DIR = path.abspath(path.dirname(__file__))
SDE_FILENAME = "multipointless.sde"

print("here we go...")

if not path.isfile(path.join(SDE_DIR, SDE_FILENAME)):
    print("creating sde file...")

    arcpy.CreateDatabaseConnection_management(
        out_folder_path=SDE_DIR,
        out_name=SDE_FILENAME,
        database_platform="SQL_SERVER",
        instance="(local)",
        account_authentication="OPERATING_SYSTEM_AUTH",
        username="#",
        password="#",
        database="Multipointless",
    )

print("creating query layer...")

sr = arcpy.SpatialReference(3857)

result = arcpy.management.MakeQueryLayer(
    input_database=path.join(SDE_DIR, SDE_FILENAME),
    out_layer_name="Multipoint_QL",
    query="SELECT id, shape FROM [dbo].[Multipoint]",
    oid_fields="id",
    shape_type="MULTIPOINT",
    srid="3857",
    spatial_reference=sr,
)

layer = result.getOutput(0)

describe = arcpy.da.Describe(layer)
shape_type = describe["shapeType"]

print("Multipoint == {} : {}".format(shape_type, shape_type == "Multipoint"))
