# 02240162

[Make Query Layer](https://pro.arcgis.com/en/pro-app/tool-reference/data-management/make-query-layer.htm) will **always** create a `POINT` feature class no matter the `shape_type` option when the first record it reads from a MSSQL query layer is a point.

## Repro

1. Bootstrap the sql database with `db.sql`
1. Run `repro.py`
