from TweetCollector import TweetCollector
import pandas as pd
import datetime
import time
from tqdm import tqdm
import os


# search_string: takes a list of keywords and hashtags and creates a search string from it
def search_string(l: "list of keywords or hashtags"):
    return ' OR '.join(l)


def collect_users():

    keys = pd.read_csv('/home/sagar/keys/twitter-keys.csv')
    os.environ['TOKEN'] = keys['BEARER_TOKEN'][0]

    # Collecting N tweets/week for 12 weeks, Top Gun release data in the middle (May 27, 2022)
    # Storing in data_users1/sagar/Euphoria-Networks/user-collection/top-gun

    start_tg = datetime.date(2022,4,15)

    sample_window = tqdm(range(84), ascii=True)

    for _ in sample_window:

        kw_tg = ['#TopGun', '(top gun)','#TopGunMaverick', '#icemav', 'maverick', '(tom miles)']

        start_str = start_tg.strftime("%Y-%m-%dT%H:%M:%S%zZ")

        end = start_tg + datetime.timedelta(days=1)
        end_str = end.strftime("%Y-%m-%dT%H:%M:%S%zZ")

        query = TweetCollector('tweets/search/all',
                               start_date=start_str,
                               end_date=end_str,
                               max_results=100,
                               keyword=search_string(kw_tg))

        top_gun_tweets = query('/data_users1/sagar/Euphoria-Project/top_gun_tweets/responses.json')

        start_tg = start_tg + datetime.timedelta(days=1)
        time.sleep(1)

    # Collecting N tweets/week for 12 weeks, two weeks before start of Euphoria S2 and 2 weeks after
    # Storing in data_users1/sagar/Euphoria-Networks/user-collection/Euphoria

    time.sleep(15*60)

    start_eu = datetime.date(2022,1,2)

    for _ in sample_window:

        # Lots of conversations about characters without hashtags so distinct character names chosen as well as
        # character pairs for more generic names

        kw_eu = ['#Euphoria', 'euphoria', '(Sydney Sweeney)', '(Nate Jacobs)', 'Rue', '(Lexi Fez)']

        start_str = start_eu.strftime("%Y-%m-%dT%H:%M:%S%zZ")

        end = start_eu + datetime.timedelta(days=1)
        end_str = end.strftime("%Y-%m-%dT%H:%M:%S%zZ")

        query = TweetCollector('tweets/search/all',
                               start_date=start_str,
                               end_date=end_str,
                               max_results=100,
                               keyword=search_string(kw_eu))
        euphoria_tweets = query('/data_users1/sagar/Euphoria-Project/euphoria_tweets/responses.json')

        start_eu = start_eu + datetime.timedelta(days=1)
        time.sleep(1)


# run
collect_users()
