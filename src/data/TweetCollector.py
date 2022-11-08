import json
import os
import requests



def create_url(keyword, start_date, end_date, max_results = 10):

    search_url = "https://api.twitter.com/2/tweets/search/all" #Change to the endpoint you want to collect data from

    #change params based on the endpoint you are using
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
                 keyword: "keyword to search the API for",
                 start_date: "start date in format YYYY-MM-DD",
                 end_date: "end date in format YYYY-MM-DD",
                 max_results: "Maximum number of results to collect"
                 ):
        self.auth = os.getenv('TOKEN')
        self.start_date = start_date+"T00:00:00.000Z"
        self.end_date = end_date+"T00:00:00.000Z"

        bearer_token = self.auth

        self.headers = create_headers(bearer_token)

        keyword = keyword

        start_time = self.start_date
        end_time = self.end_date
        max_results = max_results

        self.url = create_url(keyword, start_time,end_time, max_results)

    def __call__(self,
                 save_file: "filepath to save output as json"):
        json_return = connect_to_endpoint(self.url[0], self.headers, self.url[1])

        tweet_json = json.dumps(json_return, indent=4)

        with open(save_file, 'w') as outfile:
            outfile.write(tweet_json)



