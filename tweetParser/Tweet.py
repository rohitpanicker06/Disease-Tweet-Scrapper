class Tweet:
    type = None
    url = None
    date = None
    content = None
    renderedContent = None
    id = None
    user = None
    replyCount = None
    retweetCount = None
    likeCount = None
    quoteCount = None
    converstionId = None
    lang = None
    source = None
    sourceUrl = None
    sourceLabel = None
    outlinks = None
    tcooutLinks = None
    media = None
    retweetedTweet = None
    quotedTweet = None
    inReplyToTweetId = None
    inReplyToUser = None
    mentionedUsers = None
    coordinates = None
    place = None
    hashtags = None
    cashtags = None

    def __init__(self, typeTweet, url, date, content, renderedContent, id, user, replyCount, retweetCount, likeCount,
                 quoteCount, conversationId, lang, source, sourceUrl, sourceLabel, outlinks, tccoutLinks, media,
                 retweetedTweet, quotedTweet, inReplyToTweetId, inReplyToUser, mentionedUsers, coordinates, place, hashtags,
                 cashtags):
        self.type = typeTweet
        self.url = url
        self.date = date
        self.content = content
        self.renderedContent = renderedContent
        self.id = id
        self.user = user
        self.replyCount = replyCount
        self.retweetCount = retweetCount
        self.likeCount = likeCount
        self.quoteCount = quoteCount
        self.converstionId = conversationId
        self.lang = lang
        self.source = source
        self.sourceUrl = sourceUrl
        self.sourceLabel = sourceLabel
        self.outlinks = outlinks
        self.tcooutLinks = tccoutLinks
        self.media = media
        self.retweetedTweet = retweetedTweet
        self.quotedTweet = quotedTweet
        self.inReplyToTweetId = inReplyToTweetId
        self.inReplyToUser = inReplyToUser
        self.mentionedUsers = mentionedUsers
        self.coordinates = coordinates
        self.place = place
        self.hashtags = hashtags
        self.cashtags = cashtags


