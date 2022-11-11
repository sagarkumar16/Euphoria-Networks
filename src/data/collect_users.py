from TweetCollector import TweetCollector
import datetime

keys = pd.read_csv('/home/sagar/keys/twitter-keys.csv')

def collect_users():

    # Collecting N tweets/week for 12 weeks, Top Gun release data in the middle (May 27, 2022)
    # Storing in data_users1/sagar/Euphoria-Project/user-collection/top-gun

    top_gun_tweets = TweetCollector('/tweets/search/all', )

    # Collecting N tweets/week for 12 weeks, two weeks before start of Euphoria S2 and 2 weeks after
    # Storing in data_users1/sagar/Euphoria-Project/user-collection/Euphoria

    euphoria_tweets = TweetCollector('/tweets/search/all', )

    # Collecting user IDs from top_gun tweets
    # Collecting user IDs from Euphoria tweets

