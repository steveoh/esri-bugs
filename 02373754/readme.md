# 02373754

## UI not updating when attributes are valid

![apply-disabled](https://user-images.githubusercontent.com/325813/62174044-99e27e80-b2f5-11e9-9142-2e709471b394.gif)

### Actual

1. Two attribute rules on well class and well subclass that do not allow both the fields to be null

   - well class
   
```js
if (!haskey($feature, 'wellclass') || isempty($feature.wellclass)) {
    return true;
}

return iif (isempty(domainname($feature, 'wellclass', $feature.wellclass)), {
    'errorMessage': 'Acceptable well classes are 1, 3, 4, 5, or 6. Input: ' + $feature.wellclass
}, true)
```

   - well sub class

```js
if (!haskey($feature, 'wellsubclass') || !haskey($feature, 'wellclass')) {
    return true;
}

if (isempty($feature.wellclass)) {
    return true;
}

if (isempty($feature.wellsubclass)) {
    return {
        'errorMessage': 'Well subclass is required'
    }
}

return iif (left($feature.wellsubclass, 1) == text($feature.wellclass), true, {
    'errorMessage': 'Well sub class (' + text($feature.wellsubclass) + ') is not associated with the well class (' + text($feature.wellclass) + ')'
})
```
1. They are also contingent values 
1. When user selects one, the ar rules return an error
1. User selects the second, the ar rule error goes away
1. apply button is disabled until user selects another field

### Expected

the apply button to be enabled after they select a valid value. Not after clicking somewhere else to blur the input.

### Problem 

This is confusing to my users as they do not think the record is valid

### Software Versions

```
1. Operating system for your Client:                              Windows Server 2016 64-bit
2. Version and Service Pack level of ArcGIS:                      ArcGIS 10.7, Pro 2.4
3. Version and Service Pack level of Enterprise Geodatabase:      Enterprise Geodatabase 10.7
4. Complete version of Oracle\MS SQL Server:                      MS SQL Server 12.0.6108.1
5. Operating system for the database:                             Windows Server 2016 64-Bit)
```
