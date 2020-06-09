# Schema lock error with feature classes that participate in relationship classes

When I attempt to run `arcpy.management.RepairGeometry` on `data.gdb\FACITLITYUST` it throws this error:

```
Traceback (most recent call last):
  File "repro.py", line 11, in <module>
    arcpy.management.RepairGeometry(str(CURRENT_FOLDER / 'data.gdb' / 'FACILITYUST'))
  File "C:\Program Files\ArcGIS\Pro\Resources\ArcPy\arcpy\management.py", line 3706, in RepairGeometry
    raise e
  File "C:\Program Files\ArcGIS\Pro\Resources\ArcPy\arcpy\management.py", line 3703, in RepairGeometry
    retval = convertArcObjectToPythonObject(gp.RepairGeometry_management(*gp_fixargs((in_features, delete_null, validation_method), True)))
  File "C:\Program Files\ArcGIS\Pro\Resources\ArcPy\arcpy\geoprocessing\_base.py", line 511, in <lambda>
    return lambda *args: val(*gp_fixargs(args, True))
arcgisscripting.ExecuteError: ERROR 000464: Cannot get exclusive schema lock.  Either being edited or in
use by another application or service.
Failed to execute (RepairGeometry).
```

I'm certain that I don't have any other processes hitting this data. When I delete the relationship classes (see `data_1.gdb`) the tool executes successfully.

1. clone repo
1. `propy repro.py`
