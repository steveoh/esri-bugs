import arcpy
from pathlib import Path


CURRENT_FOLDER = Path(__file__).resolve().parent

print('this should work')
arcpy.management.RepairGeometry(str(CURRENT_FOLDER / 'data_1.gdb' / 'FACILITYUST'))

print('this throws an error')
arcpy.management.RepairGeometry(str(CURRENT_FOLDER / 'data.gdb' / 'FACILITYUST'))
