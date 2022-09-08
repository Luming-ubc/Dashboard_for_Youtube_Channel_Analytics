# %%
import requests
import pandas as pd
import numpy as np
import time

# %%
# function get_channel_summary
def get_channel_summary(channel_id):
    """ This function summarize below info by youtube channel
        title, id, country, view_count, sub_count, video_count 
    Argument:
    ----------
    channel_id_input: str
                    youtube channel id
    Returns:
        pandas DataFrame: a summary table of key info
    """
    
    with open('youtube_api_key_2.txt', 'r') as f:
        API_KEY = f.read()
    
    # use channels url
    url = "https://www.googleapis.com/youtube/v3/channels"

    # access channel snippet, statistics, and brandingSettings
    params = {'key': API_KEY, 'part': ['snippet', 'statistics', 'brandingSettings'], 'id': channel_id, 'maxResults': 50}
    response = requests.get(url, params=params)
    r_dict = response.json()

    # get view_count, subscriber_count, video_count, channel_title
    view_count = r_dict['items'][0]['statistics']['viewCount']
    subscriber_count = r_dict['items'][0]['statistics']['subscriberCount']
    video_count = r_dict['items'][0]['statistics']['videoCount']
    channel_title = r_dict['items'][0]['snippet']['title']

    # get brandingSettings country
    if 'country' in r_dict['items'][0]['brandingSettings']['channel'].keys():
        country = r_dict['items'][0]['brandingSettings']['channel']['country']
    else:
        country = np.nan
    
    # fomualte a dataframe
    channel_summary={
            'channel_title': [channel_title],
            'channel_id':[channel_id], 
            'country': [country],
            'view_count': [view_count], 
            'subscriber_count': [subscriber_count], 
            'video_count': [video_count]
            }
    channel_summary = pd.DataFrame(data=channel_summary)
    return channel_summary


# Get channel summary
channel_id = 'UCCKlp1JI9Yg3-cUjKPdD3mw'  # Magic Ingredient
channel_summary = get_channel_summary(channel_id)
channel_summary
channel_summary.to_csv('data/channel_summary.csv')

# %%
with open('youtube_api_key_2.txt', 'r') as f:
        API_KEY = f.read()

# use Videos url
url = 'https://www.googleapis.com/youtube/v3/videos'

# video_id = 'TXOOuYbH6zU' # daoyue she 1st
video_id = 'OvEXdjpZQpM' # downtown van
video_id = 'K0pVebp63Tg'

params = {'key': API_KEY, 'part': ['statistics', 'localizations', 'contentDetails', 'recordingDetails'], 'id': video_id, 'maxResults': 2}
response = requests.get(url, params=params)
r_dict = response.json()

# get relevant information from Video url
videoId = r_dict['items'][0]['id']
viewCount = r_dict['items'][0]['statistics']['viewCount']
likeCount = r_dict['items'][0]['statistics']['likeCount']
favoriteCount = r_dict['items'][0]['statistics']['favoriteCount']
commentCount = r_dict['items'][0]['statistics']['commentCount']
duration = r_dict['items'][0]['contentDetails']['duration']

r_dict

# %%
location_description = r_dict['items'][0]['recordingDetails']['locationDescription']
latitude = r_dict['items'][0]['recordingDetails']['location']['latitude']
longitude = r_dict['items'][0]['recordingDetails']['location']['longitude']

# %%
import requests

with open('youtube_api_key_2.txt', 'r') as f:
        API_KEY = f.read()

# use Videos url
url = 'https://www.googleapis.com/youtube/v3/commentThreads'

video_id = 'TXOOuYbH6zU'
params = {'key': API_KEY, 'part': ['id', 'replies', 'snippet'], 'videoId': video_id, 'maxResults': 50}
response = requests.get(url, params=params)
r_dict = response.json()
r_dict

# comment_author_channel_id  = 'UCChfzR-VFarcUlwCNF7pj9Q'


# %%

# get relevant information from Video url
videoId = r_dict['items'][0]['id']
viewCount = r_dict['items'][0]['statistics']['viewCount']
likeCount = r_dict['items'][0]['statistics']['likeCount']
favoriteCount = r_dict['items'][0]['statistics']['favoriteCount']
commentCount = r_dict['items'][0]['statistics']['commentCount']
duration = r_dict['items'][0]['contentDetails']['duration']
r_dict

