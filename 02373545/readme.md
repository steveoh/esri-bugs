# 02373545

## create related record fails with attribute constraint rule

![add-relationship](https://user-images.githubusercontent.com/325813/62175491-31969b80-b2fb-11e9-97c4-b39c65cb427e.gif)

this rule checks that a record has a value in field a or b but not both.

```js
return iif (isempty($feature.facility_fk) && isempty($feature.well_fk) || (!isempty($feature.facility_fk) && !isempty($feature.well_fk)), {
    'errorMessage': 'an inspection record must have either, but not both, a Facility_FK or a Well_FK'
}, true);
```

### Actual

It appears when using a relationship class to create a related record the `$feature` that is sent to an attribute rule with an `insert` trigger is empty and all `insert` trigger rules will fail. This makes me think that the process behind the context menu is:

1. Insert empty row with object id and or global id
1. Update row with FK from parent record

### Expected / Resolution

I expect the foreign key will be present on the `$feature` that is sent to the `insert` triggers.

A resolution would be to insert the row with the FK value as one command.

### Problem

This is problematic because we do not want to allow users to insert records without a PK. We cannot rely on them to update it later.


```
1. Operating system for your Client:                              Windows Server 2016 64-bit
2. Version and Service Pack level of ArcGIS:                      ArcGIS 10.7, Pro 2.4
3. Version and Service Pack level of Enterprise Geodatabase:      Enterprise Geodatabase 10.7
4. Complete version of Oracle\MS SQL Server:                      MS SQL Server 12.0.6108.1
5. Operating system for the database:                             Windows Server 2016 64-Bit)
```
