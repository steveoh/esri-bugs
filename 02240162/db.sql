-- create temp db
CREATE DATABASE [Multipointless]
GO

USE [Multipointless]
GO

-- create temp table
CREATE TABLE [dbo].[Multipoint](
	[id] [int] NOT NULL,
	[shape] [geometry] NOT NULL
)
GO

-- insert a point and multipoint feature making sure the point feature is first
INSERT INTO [dbo].[Multipoint]
           ([id]
           ,[shape])
     VALUES
           (1
           ,'POINT (-12410700 5020300)'
		   ),
		   (2
		   ,'MULTIPOINT((-12410650 5020250),(-12410255.541000001 5020448.7007))'
		   )
GO
