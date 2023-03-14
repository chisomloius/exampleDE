-- use the master location in the MSSQL
USE [master]
GO
--create a login with password and use the Default DB
CREATE LOGIN [etl] WITH PASSWORD=N'etltesting', DEFAULT_DATABASE=[AdventureWorksDW2019], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
-- Reference the Default DB
USE[AdventureWorksDW2019]
GO
--
CREATE USER[etl] FOR LOGIN [etl]
GO
--
USE[AdventureWorksDW2019]
GO
--
ALTER ROLE [db_datareader] ADD MEMBER [etl]
GO
--
USE [master]
GO
-- 
GRANT CONNECT SQL TO [etl]
GO


--STEPS ON HOW TO USE THE DEFAULT DB CAN BE FOUND HERE
- https://www.youtube.com/watch?v=oA-D2P5NssE