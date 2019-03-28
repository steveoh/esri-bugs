If you have add an attribute rule that is noneditable, disable it, and then write data to those fields the cursor appears to function but no data is actually written. I would expect an error or some sort of warning.

[AlterField](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/alter-field-properties.htm) does not give you access to the readonly property either so you cannot modify it via arcpy.
