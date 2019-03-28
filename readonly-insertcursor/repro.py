import arcpy
import os

sde = os.path.join(os.path.dirname(__file__), '..', 'pro-project', 'uicar.sde')

table_name = 'test_fc'
table = os.path.join(sde, table_name)

arcade = 'return Guid();'
print('creating the feature class')
arcpy.management.CreateFeatureclass(sde, table_name, 'POLYGON', spatial_reference=arcpy.SpatialReference(26912))
arcpy.management.AddField(table, 'readonly', 'TEXT')
arcpy.management.AddGlobalIDs(table)
print('done')

print('giving the table some data')
with arcpy.da.InsertCursor(table, ['readonly']) as cursor:
    print(cursor.insertRow(['i am not read only yet']))
print('done')

print('adding noneditable rule')
try:
    arcpy.management.AddAttributeRule(
        in_table=table,
        name='test_rule',
        type='CALCULATION',
        script_expression=arcade,
        is_editable='NONEDITABLE',
        triggering_events='INSERT',
        error_number=1,
        error_message='i am read only',
        description='always a guid string',
        subtype='',
        field='readonly',
        exclude_from_client_evaluation='',
        batch=False,
        severity='',
        tags='bug'
    )
except Exception as e:
    print(e)

print('done')

print('disabling the rule, but it will still be a read only field now')

arcpy.management.DisableAttributeRules(table, 'test_rule')

print('done')

print('writing records that will appear to function but will be empty rows')
with arcpy.da.InsertCursor(table, ['readonly']) as cursor:
    print(cursor.insertRow(['i am not written to the table, but appear to be']))
    print(cursor.insertRow(['i am not written to the table, but appear to be']))
    print(cursor.insertRow(['i am not written to the table, but appear to be']))
    print(cursor.insertRow(['i am not written to the table, but appear to be']))
    print(cursor.insertRow(['i am not written to the table, but appear to be']))
    print(cursor.insertRow(['i am not written to the table, but appear to be']))
    print(cursor.insertRow(['i am not written to the table, but appear to be']))
    print(cursor.insertRow(['i am not written to the table, but appear to be']))
print('done')

print('printing rows as they are stored')
with arcpy.da.SearchCursor(table, ['OID@', 'readonly']) as cursor:
    for row in cursor:
        print(row)
