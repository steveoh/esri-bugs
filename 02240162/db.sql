CREATE DATABASE [Multipointless]
GO

USE [Multipointless]
GO

CREATE TABLE [dbo].[Multipoint]
(
  [id] [int] NOT NULL,
  [shape] [geometry] NOT NULL
)
GO

INSERT INTO [dbo].[Multipoint]
  ([id],[shape])
VALUES
  (1, geometry::STGeomFromText('POINT (-12410700 5020300)', 3857)),
  (2, geometry::STGeomFromText('MULTIPOINT((-12410650 5020250),(-12410255 5020448))', 3857))
GO
