# Assignment 2 - Scraping Twitter - Team Data Sherpas

Python Bot for this assignment:

*Rohit Panicker to explain in points about what each file is for; their uses like which file is used to scrape twitter 
data and which file is used to feed data to db tables*


Database tables for this assignment:

# DISEASES table:

1. We created a Diseases table and we are using this table's diseaseas as tags in the Python bot, such that the bot retrieves twitter data per each disesase name.
2. This "Diseases" table is present in the master branch like "Diseases.sql"

# USERS table:

1. We created a "Users" table which contains all users' twitter account data.
2. This "Users" table is present in the master branch like "Users.sql"

# TWEETS table:

1. We created a "Tweets" table which contains all the tweets created by users in relavance to their illnesses/symptoms that they experience.
2. This "Tweets" table is present in the master branch like "Tweets.sql"

# TWEET TAGS table:

1. We created a "TweetTags" table which contains all the hashtags that the user used in their tweet text.
2. This "TweetTags" table is present in the master branch like "Tweet Tags.sql"

# TWEET MENTIONS table:

1. We created a "TweetMentions" table which contains data of the source users who mentions other users in their tweets and those mentioned users 
are stored in this table as target users.
2. This "TweetMentions" table is present in the master branch like "Tweet Mentions.sql"






