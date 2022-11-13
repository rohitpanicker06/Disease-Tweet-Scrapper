SHOW DATABASES;

USE DIS;

/*
Creating a DB table for tweet mentions
*/

CREATE TABLE TweetMentions (
    Tweet_ID BIGINT UNIQUE,
    Source_User VARCHAR(250),
    Target_User TEXT,
    PRIMARY KEY (Source_User),
    FOREIGN KEY (Tweet_ID) REFERENCES Tweets (Tweet_ID)
);


/*
Viewing the table created
*/

SELECT * FROM TweetMentions;