import tweetParser
from tweetParser.Tweet import Tweet


class TweetParser:

    def parseTweet(self, tweetDataFrame, columnHeaders):
        tweets_df = tweetDataFrame.reset_index()
        resultArray = []
        for index, row in tweets_df.iterrows():
            type_V = row['_type']
            url = row['url']
            date = row['date']
            content = row['content']
            renderedContent = row['renderedContent']
            idv = row['id']
            user = row['user']
            replyCount = row['replyCount']
            retweetCount = row['retweetCount']
            likeCount = row['likeCount']
            quoteCount = row['quoteCount']
            conversationId = row['conversationId']
            lang = row['lang']
            source = row['source']
            sourceUrl = row['sourceUrl']
            sourceLabel = row['sourceLabel']
            outLinks = row['outlinks']
            tcooutLinks = row['tcooutlinks']
            media = row['media']
            retweetedTweet = row['retweetedTweet']
            quotedTweet = row['quotedTweet']
            inReplyToTweetId = row['inReplyToTweetId']
            inReplyToUser = row['inReplyToUser']
            mentionedUsers = row['mentionedUsers']
            coordinates = row['coordinates']
            place = row['place']
            hashtags = row['hashtags']
            cashtags = row['cashtags']

            tweet = Tweet(type_V, url, date, content, renderedContent, idv, user,
                          replyCount, retweetCount, likeCount, quoteCount, conversationId, lang, source,
                          sourceUrl, sourceLabel, outLinks, tcooutLinks, media, retweetedTweet,
                          quotedTweet, inReplyToTweetId, inReplyToUser, mentionedUsers, coordinates, place,
                          hashtags, cashtags)
            resultArray.append(tweet)

        return resultArray
