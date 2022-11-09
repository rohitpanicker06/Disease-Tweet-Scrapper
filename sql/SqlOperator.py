import mysql.connector
# from diseases import Tweet
import sql.SqlConnectorGenerator


class SqlOperator:
    mydbConnectorInstance = sql.SqlConnectorGenerator.SqlConnectorGenerator("localhost", "root", "Welcometopune18@",
                                                                            "DMDD")
    mydbConnectorInstance = mydbConnectorInstance.createConnector()
    mycursor = mydbConnectorInstance.cursor()

    def __init__(self, tweet):
        self.id = tweet.id
        #self.handle = tweet.handle get handle from users json
        self.content = tweet.content
        self.date = tweet.date
        self.url = tweet.url
        self.tweet_id = tweet.id
        self.source = tweet.source
        #self.user = tweet.user  get user fromm users json
        self.hashtags = tweet.hashtags

    def insert_tweets(self):
        mydb = self.connect_db()
        mycursor = mydb.cursor()
        sqlformula = "INSERT INTO tweets(Tweet_ID,Twitter_Handle,Tweet_Text,Tweet_Created_Date,Tweet_url) VALUES(%s,%s,%s,%s,%s)"
        tweets = (self.id, self.handle, self.content, self.date, self.url)
        #mycursor.execute(sqlformula, tweets)
        #mydb.commit()

    def insert_tweetmentions(self):
        mydb = self.connect_db()
        mycursor = mydb.cursor()
        sqlformula = "INSERT INTO tweetmentions(Tweet_ID,Source_User,Target_User) VALUES(%s,%s,%s)"
        tweetmentions = (self.tweet_id, self.source, self.user)
        #mycursor.execute(sqlformula, tweetmentions)
        #mydb.commit()

    def insert_tweettags(self):
        mydb = self.connect_db()
        mycursor = mydb.cursor()
        sqlformula = "INSERT INTO tweettags(Tweet_ID,Hashtags) VALUES(%s,%s)"
        tweettags = (self.tweettag_id, self.hashtags)
        #mycursor.execute(sqlformula, tweettags)
        #mydb.commit()

    def insert_users(self):
        mydb = self.connect_db()
        mycursor = mydb.cursor()
        sqlformula = "INSERT INTO tweettags(User_ID,Twitter_Handle,Display_Name,User_Description,verified,Profile_Created_At,Follower_Count,Friends_Count,User_Location,Profile_Image_URL) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"
        users = (self.tweettag_id, self.hashtags)
       # mycursor.execute(sqlformula, users)
       # mydb.commit()
