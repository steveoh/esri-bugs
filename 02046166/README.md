# 02046166

1. Build SOE
1. Add SOE to ArcGIS Server Extensions
1. Enable SOE capability on any `MapServer`
1. See error

# Visual

![value](./image (1).png)
- The field I request is `VALUE` and is shown in the `attributeName` variable
- The `findIndex` is `1`
- The `item.GetPropAndValue` uses the `findIndex` of `1` and `property` is set to `OBJECTID` :bug:

![objectid](./image (2).png)
- The field I request is `OBJECTID` and is shown in the `attributeName` variable -
- The `findIndex` is `0`
- The `item.GetPropAndValue` uses the `findIndex` of `0` and `property` is set to `Pixel value` :bug:

![objectid](./image.png)
- The field I request is `FEET` and is shown in the `attributeName` variable - -
- The `findIndex` is `3`
- The `item.GetPropAndValue` uses the `findIndex` of `3` and `property` is set to `FEET` :white_check_mark:
