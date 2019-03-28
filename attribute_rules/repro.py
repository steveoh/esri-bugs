import arcpy
import os

sde = 'some.sde'
featureset_name = 'intersect_fc'
featureset_table = os.path.join(sde, featureset_name)

table_name = 'base_fc'
table = os.path.join(sde, table_name)

wkt = (
    'POLYGON ((419771.30999999959 4476140.9299999997, 421271.66000000015 4474303, 425713.20999999996 4477928.7599999998, 424212.86000000034 '
    '4479766.6799999997, 419771.30999999959 4476140.9299999997)), 26912)'
)

extract_fips = '''var layer = 'intersect_fc';
var field = 'FIPS';
var set = FeatureSetByName($datastore, layer);

function getAttributeFromLargestArea(feat, set, field) {
    var items = intersects(set, feat);
    var counts = count(items);

    if (counts == 0) {
        return { 'errorMessage': 'No intersection found' };
    }

    if (counts == 1) {
        var result = first(items);

        return result[field];
    }

    var largest = -1;
    var result;

    for (var item in items) {
        var size = area(intersection(item, feat));

        if (size > largest) {
            largest = size;
            result = item[field];
        }
    }

    return result;
}

var fips = getAttributeFromLargestArea($feature, set, field);

return iif(isnan(number('490' + fips)), null, number('490' + fips));
'''

print('creating the feature class to use in the featuresetbyname')
arcpy.management.CreateFeatureclass(sde, featureset_name, 'POLYGON', spatial_reference=arcpy.SpatialReference(26912))
arcpy.management.AddField(featureset_table, 'FIPS', 'LONG')
arcpy.management.AddGlobalIDs(featureset_table)
print('done')

print('giving the featureset some data')
with arcpy.da.InsertCursor(featureset_table, ['FIPS', 'shape@wkt']) as cursor:
    print(cursor.insertRow((49001, wkt)))
print('done')

print('creating table to add rule to')
arcpy.management.CreateFeatureclass(sde, table_name, 'POLYGON', spatial_reference=arcpy.SpatialReference(26912))
arcpy.management.AddField(table, 'CountyNumber', 'LONG')
arcpy.management.AddGlobalIDs(table)
print('done')

print('adding rule')
arcpy.management.AddAttributeRule(
    in_table=table,
    name='test_rule',
    type='CALCULATION',
    script_expression=extract_fips,
    is_editable='EDITABLE',
    triggering_events='INSERT',
    error_number=1,
    error_message='you broke it',
    description='work please',
    subtype='',
    field='CountyNumber',
    exclude_from_client_evaluation='',
    batch=False,
    severity='',
    tags='bug'
)
print('done')
