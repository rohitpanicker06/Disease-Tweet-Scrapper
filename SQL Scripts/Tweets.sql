CREATE DATABASE DIS; #to create my database

SHOW DATABASES; #to show a list of available databases

USE DIS; #to use my created database

/*
Creating a DB table for tweets
*/

CREATE TABLE Tweets (
    Tweet_ID BIGINT UNIQUE,
    Twitter_Handle VARCHAR(500) UNIQUE NOT NULL,
    Tweet_Text TEXT,
    Tweet_Created_Date DATETIME,
    Tweet_URL TEXT,
    PRIMARY KEY (Tweet_ID),
    FOREIGN KEY (Twitter_Handle) REFERENCES Users (Twitter_Handle)); 

/*
Viewing the table created
*/

SELECT * FROM Tweets;