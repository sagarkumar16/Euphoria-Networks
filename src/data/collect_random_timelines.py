from TweetCollector import TweetCollector
from unpack import unpack
import pandas as pd
import os
import time
from tqdm import tqdm
import os
import csv
import datetime


def collect_random_timelines():

    """
    :return: timelines from an unrelated, given set of users
    """

    keys = pd.read_csv('/home/sagar/keys/twitter-keys.csv')
    os.environ['TOKEN'] = keys['BEARER_TOKEN'][0]


    ids = list()

    with open('sagiwaffles_following.csv', 'r') as file:
        for line in csv.reader(file):
            ids.extend(line)

    ids = [i.replace('\'', '') for i in ids]
    ids = [i.replace(' ', '') for i in ids]
    ids = ids[1:]

    for u in tqdm(ids):

        week0 = datetime.date(2022,6,1)

        week = 0
        while week < 12:

            start = week0 + datetime.timedelta(weeks=week)
            start_str = start.strftime("%Y-%m-%dT%H:%M:%S%zZ")
            end = start + datetime.timedelta(weeks=1)
            end_str = end.strftime("%Y-%m-%dT%H:%M:%S%zZ")

            query = TweetCollector('tweets',
                                   start_date=start_str,
                                   end_date=end_str,
                                   max_results=25,
                                   ids=u)

            random_timelines = query('/data_users1/sagar/Euphoria-Project/random_sample/timelines_2.json')

            week += 1
            time.sleep(1)


# run
collect_random_timelines()