# 02373754

## UI not updating when attributes are valid

![ar](https://user-images.githubusercontent.com/325813/62173830-b631eb80-b2f4-11e9-8b7f-9f063994c503.gif)

1. Two attribute rules on well class and well subclass that do not allow both the fields to be null
1. When user selects one, the ar rules return an error
1. User selects the second, the ar rule error goes away
1. apply button is disabled until user selects another field

This is confusing to my users and they expect the apply button to be enabled after they select a valid value. 
