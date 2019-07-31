# 02373754

## UI not updating when attributes are valid

![apply-disabled](https://user-images.githubusercontent.com/325813/62174044-99e27e80-b2f5-11e9-9142-2e709471b394.gif)

1. Two attribute rules on well class and well subclass that do not allow both the fields to be null
1. When user selects one, the ar rules return an error
1. User selects the second, the ar rule error goes away
1. apply button is disabled until user selects another field

This is confusing to my users and they expect the apply button to be enabled after they select a valid value. 
