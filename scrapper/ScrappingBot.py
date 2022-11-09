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
    count = count+1
    print(diseaseName)
    os.system(
        f"snscrape --jsonl --max-results 1 --since 2020-06-01 twitter-search \"{diseaseName} until:2020-07-31\" > "
        "text-query-tweets.json")
    count = count + 1;
    tweets_df = pd.read_json('text-query-tweets.json', lines=True)
    print(tweets_df.to_string())
    columnHeaders = list(tweets_df.columns.values)
    resultTweet = tweetParsers.parseTweet(tweets_df, columnHeaders)
    os.remove("text-query-tweets.json")

    for tweets in resultTweet:

        sqlOperator = sql.SqlOperator.SqlOperator(tweets)
        sqlOperator.insert_users()
        #sqlOperator.insert_tweets()
        #sqlOperator.insert_tweettags()
        #sqlOperator.insert_tweetmentions()

    if count == 1:
        break















