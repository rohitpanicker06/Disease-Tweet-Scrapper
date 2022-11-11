import json
import math
import mysql.connector


# from diseases import Tweet
import sql.SqlConnectorGenerator

from tweetParser import TweetParser


def parseMentionedUsers(mentionedUsers):

    for newMentionedUsers in mentionedUsers:
        print(newMentionedUsers)






class SqlOperator:
    mydbConnectorInstance = sql.SqlConnectorGenerator.SqlConnectorGenerator("localhost", "root", "Welcometopune18@",
                                                                            "DMDD")
    mydbConnectorInstance = mydbConnectorInstance.createConnector()
    mycursor = mydbConnectorInstance.cursor()
    tweetParsers = TweetParser.TweetParser()

    def __init__(self, tweet):
        self.id = tweet.id
        tweetParsers = TweetParser.TweetParser()
        #self.handle = tweet.handle get handle from users json
        self.content = tweet.content
        self.date = tweet.date
        self.url = tweet.url
        self.tweet_id = tweet.id
        self.source = tweet.source
        self.user = tweetParsers.parseUsers(tweet.user)
        self.hashtags = tweet.hashtags
        self.mentionedUsers = tweet.mentionedUsers

    def insert_tweets(self):

        sqlformula = "INSERT INTO Tweets (Tweet_ID, Twitter_Handle, Tweet_Text, Tweet_Created_Date, Tweet_url) VALUES(%s," \
                     "%s,%s,%s,%s) "
        jsonObj = json.loads(self.user)
        handle = jsonObj["username"]
        tweets = (self.id, handle, self.content, self.date, self.url)
        self.mycursor.execute(sqlformula, tweets)
        self.mydbConnectorInstance.commit()

    def insert_tweetmentions(self):

        sqlformula = "INSERT INTO TweetMentions (Tweet_ID,Source_User,Target_User) VALUES(%s,%s,%s)"
        for newMentionedUsers in self.mentionedUsers:
            userId = newMentionedUsers["id"]
            handle = newMentionedUsers["username"]
            displayname = newMentionedUsers["displayname"]
            userDesc = newMentionedUsers["description"]
            verified = newMentionedUsers["verified"]
            created = newMentionedUsers["created"]
            followerCount = newMentionedUsers["followersCount"]
            friendsCount = newMentionedUsers["friendsCount"]
            location = newMentionedUsers["location"]
            profileImageUrl = newMentionedUsers["profileImageUrl"]
            sqlformulaUsers = "INSERT INTO Users (User_ID,Twitter_Handle,Display_Name,User_Description,verified," \
                         "Profile_Created_At,Follower_Count,Friends_Count,User_Location,Profile_Image_URL) VALUES(%s,%s," \
                         "%s,%s,%s,%s,%s,%s,%s,%s) "
            users = (userId, handle, displayname, userDesc, verified, created, followerCount, friendsCount, location,
                     profileImageUrl)
            self.mycursor.execute(sqlformulaUsers, users)
            self.mydbConnectorInstance.commit()

            jsonObj = json.loads(self.user)
            userIdSource = jsonObj["id"]
            tweetmentions = (self.tweet_id, userIdSource, userId)
            self.mycursor.execute(sqlformula, tweetmentions)
            self.mydbConnectorInstance.commit()







    def insert_tweettags(self):
        #Done

        sqlformula = "INSERT INTO TweetTags (Tweet_ID,Hashtags) VALUES(%s,%s)"
        if self.hashtags is None:
            self.hashtags = None
        else:
            if math.isnan(self.hashtags):
                self.hashtags = None

        tweettags = (self.id, self.hashtags)
        self.mycursor.execute(sqlformula, tweettags)
        self.mydbConnectorInstance.commit()

    def insert_users(self):

        sqlformula = "INSERT INTO Users (User_ID,Twitter_Handle,Display_Name,User_Description,Verified,Profile_Created_At,Follower_Count,Friends_Count,User_Location,Profile_Image_URL) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        jsonObj = json.loads(self.user)
        userId = jsonObj["id"]
        handle = jsonObj["username"]
        displayname = jsonObj["displayname"]
        userDesc = jsonObj["description"]
        verified = jsonObj["verified"]
        created = jsonObj["created"]
        followerCount = jsonObj["followersCount"]
        friendsCount = jsonObj["friendsCount"]
        location = jsonObj["location"]
        profileImageUrl = jsonObj["profileImageUrl"]

        users = (userId, handle, displayname, userDesc, verified, created, followerCount, friendsCount, location, profileImageUrl)
        self.mycursor.execute(sqlformula, users)
        self.mydbConnectorInstance.commit()
