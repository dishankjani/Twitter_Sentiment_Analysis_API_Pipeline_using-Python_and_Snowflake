-- create database

CREATE DATABASE SNOWFLAKE_DATAPIPELINE_DB;
use schema snowflake_datapipeline_db.public;


-- create table
create or replace TABLE Twitter_Sentiment (
    ABOUT VARCHAR(16777216),
    ASSSOCIATED_LOC VARCHAR(16777216),
    ASSOCIATED_ORG VARCHAR(16777216),
    CATEGORY VARCHAR(16777216),
    DOB VARCHAR(16777216),
    tweet VARCHAR(16777216),
    user_tweets VARCHAR(16777216),
    TITLE VARCHAR(16777216),
    URL VARCHAR(16777216)
);

-- check history for failed or successful copy operations in pipe
select * from table(information_schema.copy_history(TABLE_NAME=>'twitter_sentiments', START_TIME=> DATEADD(hours, -1, CURRENT_TIMESTAMP())));


