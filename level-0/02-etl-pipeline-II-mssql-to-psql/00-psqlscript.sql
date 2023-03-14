--create a database
CREATE DATABASE playDB

--create etl user
CREATE USER etl WITH PASSWORD 'etltesting';

--grant connect
GRANT CONNECT ON DATABASE "playDB" TO etl;

--grant table permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO etl;