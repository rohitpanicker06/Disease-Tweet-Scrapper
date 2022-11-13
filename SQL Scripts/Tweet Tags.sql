SHOW DATABASES;

USE DIS;

/*
Creating a DB table for tweet tags
*/

CREATE TABLE TweetTags (
    Tweet_ID BIGINT UNIQUE,
    Hashtags VARCHAR(750),
    PRIMARY KEY (Hashtags),
    FOREIGN KEY (Tweet_ID) REFERENCES Tweets (Tweet_ID)
);

/*
Viewing the table created
*/

SELECT * FROM TweetTags;