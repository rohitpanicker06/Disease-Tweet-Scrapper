SHOW DATABASES;

USE DIS;

/*
Creating a DB table for users
*/

CREATE TABLE Users (
    User_ID BIGINT UNIQUE,
    Twitter_Handle VARCHAR(500),
    Display_Name TEXT,
    User_Description TEXT,
    Verified BOOLEAN,
    Profile_Created_At DATETIME,
    Follower_Count INT,
    Friends_Count INT,
    User_Location TEXT,
    Profile_Image_URL TEXT,
    PRIMARY KEY (Twitter_Handle) 
);

/*
Viewing the table created
*/

SELECT * FROM Users;

