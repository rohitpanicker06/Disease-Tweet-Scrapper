import os
import pandas as pd
import mysql.connector
import sql.SqlConnectorGenerator
import sql.SqlOperator
import tweetParser
from tweetParser import TweetParser

mydbConnectorInstance = sql.SqlConnectorGenerator.SqlConnectorGenerator("localhost", "root", "Welcometopune18@", "DMDD")
mydbConnectorInstance = mydbConnectorInstance.createConnector()
tweetParsers = TweetParser.TweetParser()

mycursor = mydbConnectorInstance.cursor()
diseasesSubsetResult = "Select DiseaseName from Diseases";
mycursor.execute(diseasesSubsetResult)

myresult = mycursor.fetchall()
count = 0;
for row in myresult:
    diseaseName = row[0]
    count = count + 1
    print(diseaseName)
    os.system(
        f"snscrape --jsonl --max-results 10 --since 2020-06-01 twitter-search \"{diseaseName} until:2020-07-31\" > "
        "text-query-tweets.json")
    tweets_df = pd.read_json('text-query-tweets.json', lines=True)
    print(tweets_df.to_string())
    columnHeaders = list(tweets_df.columns.values)
    resultTweet = tweetParsers.parseTweet(tweets_df, columnHeaders)

    for tweets in resultTweet:

        sqlOperator = sql.SqlOperator.SqlOperator(tweets)
        try:
            sqlOperator.insert_users()
        except Exception as e:
            print("Exception occured while inserting user into Users= {}", e)

        try:
            sqlOperator.insert_tweets()
        except Exception as e:
            print("Exception occured while inserting tweet into Tweets Table = {}", e)

        try:
            sqlOperator.insert_tweettags()
        except Exception as e:
            print("Exception occured while inserting tweetTags into TweetsTags table = {}", e)

        try:
            sqlOperator.insert_tweetmentions()
        except Exception as e:
            print("Exception occured while inserting TweetMentions into TweetMentions table = {}", e)

    if count == 5:
        break
