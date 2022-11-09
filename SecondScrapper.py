
import os
import pandas as pd
import mysql.connector
import sql.SqlConnectorGenerator

#mydbConnectorInstance = sql.SqlConnectorGenerator.SqlConnectorGenerator("localhost", "root", "password", "DMDD")
#mydbConnectorInstance = mydbConnectorInstance.createConnector()

#mycursor= mydbConnectorInstance.cursor()
#diseasesSubsetResult = "Select name from Diseases";
#result = mycursor.execute(diseasesSubsetResult)
#print(result)



# Using OS library to call CLI commands in Python
os.system("snscrape --jsonl --max-results 1 --since 2020-06-01 twitter-search \"its the elephant until:2020-07-31\" > text-query-tweets.json")




# Reads the json generated from the CLI commands above and creates a pandas dataframe
tweets_df = pd.read_json('text-query-tweets.json', lines=True)


tweets_df = tweets_df.reset_index()
#columnHeaders = list(tweets_df.columns.values)




#print(columnHeaders)
print(tweets_df.to_string())

print(tweets_df['url'][0])


