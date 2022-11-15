from TweetCollector import TweetCollector
import unpack
import pandas as pd
import os
import time
from tqdm import tqdm
import os


def collect_timelines():

    '''
    :return: None
    '''

    """
    collect_timelines() is meant to be run after having a collection of tweets for both shock-related keyword searches.
    This function unpacks the output of those functions and extracts a set of users from which it iteratively collects
    timelines.

    The function collects a maximum of 25 tweets/user/week.
    """

    keys = pd.read_csv('/home/sagar/keys/twitter-keys.csv')
    os.environ['TOKEN'] = keys['BEARER_TOKEN'][0]

    # Unpacking the json responses
    tg_tweets = unpack('top_gun_tweets')
    euphoria_tweets = unpack('euphoria_tweets')

    # Extracting users from the tweets collected in Top Gun keyword search
    tg_users = []
    for day, objs in enumerate(tg_tweets):
        tweets = objs['data']
        for t in tweets:
            tg_users.append(t['author_id'])

    # trimming duplicates
    tg_users = list(set(tg_users))

    # Extracting users from the tweets collected in Euphoria keyword search
    eu_users = []
    for day, objs in enumerate(euphoria_tweets):
        tweets = objs['data']
        for t in tweets:
            eu_users.append(t['author_id'])

    # trimming duplicates
    euphoria_users = list(set(eu_users))

    iter_tg_users = tqdm(tg_users, ascii=True)
    iter_eu_users = tqdm(euphoria_users, ascii=True)

    # Iterating over all the top gun users, and iterating over each week to ensure that at least one tweet in each time
    # window is collected by each user
    # Max/week/user is 25 tweets

    for u in iter_tg_users:

        start_tg = datetime.date(2022,4,15)

        week = 0
        while week < 12:

            start_tg = start_tg + datetime.timedelta(weeks=week)
            start_str = start_tg.strftime("%Y-%m-%dT%H:%M:%S%zZ")
            end = start_tg + datetime.timedelta(weeks=1)
            end_str = end.strftime("%Y-%m-%dT%H:%M:%S%zZ")

            query = TweetCollector('users/:id/tweets',
                                   start_date=start_str,
                                   end_date=end_str,
                                   max_results=25,
                                   ids=u)

            top_gun_timelines = query('/data_users1/sagar/Euphoria-Project/top_gun_tweets/timelines.json')

            week += 1
            time.sleep(1)

    time.sleep(1)

    for u in iter_eu_users:

        start_eu = datetime.date(2022,1,2)

        week = 0
        while week < 12:

            start_eu = start_eu + datetime.timedelta(weeks=week)
            start_str = start_eu.strftime("%Y-%m-%dT%H:%M:%S%zZ")
            end = start_eu + datetime.timedelta(weeks=1)
            end_str = end.strftime("%Y-%m-%dT%H:%M:%S%zZ")

            query = TweetCollector('users/:id/tweets',
                                   start_date=start_str,
                                   end_date=end_str,
                                   max_results=25,
                                   ids=u)

            euphoria_timelines = query('/data_users1/sagar/Euphoria-Project/euphoria_tweets/timelines.json')

            week += 1
            time.sleep(1)

# run
collect_timelines()

