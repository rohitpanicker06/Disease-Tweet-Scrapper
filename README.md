# ASSIGNMENT 2 - SCRAPING TWITTER - TEAM DATA SHERPAS
# Python Twitter Bot for this assignment:
Utilizes Sncrape module for scrapping tweets from twitter.
Note: No API_TOKENS needed.
1. Code Entry Point : scrapper.ScrappingBot.py
2. The code fetches 500 tweets for each Keyword.
3.Keywords are pre populated using Diseases dataset. (You can find the diseases dataset within the "Datasets" folder.
NOTE: If one wants import the Diseases dataset provided in this repository to the Diseases table, the encoding for the dataset CSV file must be in ASCII.
For Macs: You could convert File encoding to ASCII by using cotEditor.

4. Tweets will be fetched and parsed and the following tables will be populated:


  -Users
  -Tweets
  -TweetMentions
  -TweetTags
  
 5. Please refer to the SQLScripts folder for the physical model.


IMP NOTE: Please import the sqlscripts to build the tables and populate Diseases table using the dataset provide before running this bot, else the bot will fail to scrape tweets.


Database tables for this assignment:
# Diseases table:
1. We created a Diseases table and we are using this table's diseaseas as tags in the Python bot, such that the bot retrieves twitter data per each disesase name.
2. This "Diseases" table is present in the master branch under the SQL Scripts folder like "Diseases.sql"
# Users table:
1. We created a "Users" table which contains all users' twitter account data.
2. This "Users" table is present in the master branch under the SQL Scripts folder like "Users.sql"
# Tweets table:
1. We created a "Tweets" table which contains all the tweets created by users in relavance to their illnesses/symptoms that they experience.
2. This "Tweets" table is present in the master branch under the SQL Scripts folder like "Tweets.sql"
# Tweet tags table:
1. We created a "TweetTags" table which contains all the hashtags that the user used in their tweet text.
2. This "TweetTags" table is present in the master branch under the SQL Scripts folder like "Tweet Tags.sql"
# Tweet mentions table:
1. We created a "TweetMentions" table which contains data of the source users who mentions other users in their tweets and those mentioned users
are stored in this table as target users.
2. This "TweetMentions" table is present in the master branch under the SQL Scripts folder like "Tweet Mentions.sql"



