import tweepy

# these are your own Twitter API keys, replace XXX with your own keys.
consumer_key = "sJe963XeD1r1F591UOlJA22EC"
consumer_secret = "Qv0z6iiw3aUF3p0HaHuxyuD4EbYp9LnB1zeon5h2lysBZkEmWv"
access_token = "1675875449925246977-52eLlEwxkaNUwhbif1l7VsWTPz5ip9"
access_token_secret = "Isv2cC8JpRZSrDfAkTidVjKNqN6ipDsZ9i3UTa7UvfyDk"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline(screen_name='elonmusk', count=5)
for tweet in public_tweets:
    print(tweet.text)
