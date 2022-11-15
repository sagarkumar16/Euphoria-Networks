import json
import os
import requests

"""
Code from "An Extensive Guide to collecting tweets from Twitter API v2 for academic research using Python 3" by Andrew 
Edward (https://andrew37edward.medium.com/) which was formatted for use in this project and package by Sagar Kumar.
"""

# TODO: add docstrings

def create_url_kw(keyword, endpoint, start_date, end_date, max_results):

    search_url = "https://api.twitter.com/2/" + endpoint



    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}

    return search_url, query_params


def create_url_id(ids, endpoint, start_date, end_date, max_results):

    search_url = f"https://api.twitter.com/2/users/{ids}/" + endpoint

    query_params = {'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}

    return search_url, query_params


def connect_to_endpoint(url, headers, params, next_token=None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


class TweetCollector:

    def __init__(self,
                 endpoint: "string of API endpoint to be used ('tweets/search/all', '/users/:id/tweets', etc)",
                 start_date: "start date in format YYYY-MM-DD",
                 end_date: "end date in format YYYY-MM-DD",
                 max_results: "Maximum number of results to collect",
                 keyword: "keyword to search the API for" = None,
                 ids: "Tweet or User IDs to collect" = None
                 ):
        self.auth = os.getenv('TOKEN')

        self.endpoint = endpoint

        self.start_date = start_date
        self.end_date = end_date

        bearer_token = self.auth

        self.headers = create_headers(bearer_token)

        keyword = keyword

        start_time = self.start_date
        end_time = self.end_date

        max_results = max_results

        if keyword is not None:

            self.url = create_url_kw(keyword, endpoint, start_time, end_time, max_results)

        elif ids is not None:
            self.url = create_url_id(ids, endpoint, start_time, end_time, max_results)

    def __call__(self,
                 save_file: "filepath to save output as json"):
        json_return = connect_to_endpoint(self.url[0], self.headers, self.url[1])

        tweet_json = json.dumps(json_return, indent=4)

        with open(save_file, 'a') as outfile:
            outfile.write(tweet_json)





