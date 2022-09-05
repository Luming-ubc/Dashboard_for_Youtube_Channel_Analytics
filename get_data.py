# %%
import requests
import pandas as pd
import numpy as np
import time

# %%
# function get_channel_summary
def get_channel_summary(channel_id_input):
    """ This function summarize below info by youtube channel
        title, id, country, view_count, sub_count, video_count 
    Argument:
    ----------
    channel_id_input: str
                    youtube channel id
    Returns:
        pandas DataFrame: a summary table of key info
    """
    
    with open('youtube_api_key.txt', 'r') as f:
        API_KEY = f.read()
    
    # 1. channels url
    url = "https://www.googleapis.com/youtube/v3/channels"

    # 1.1 statistics + id (ChannelID
    params = {'key': API_KEY, 'part': 'statistics', 'id': channel_id_input, 'maxResults': 50}
    response = requests.get(url, params=params)
    r_dict = response.json()

    viewCount = r_dict['items'][0]['statistics']['viewCount']
    subscriberCount = r_dict['items'][0]['statistics']['subscriberCount']
    videoCount = r_dict['items'][0]['statistics']['videoCount']

    # 1.2 part:snippet + filter: id (channelID)
    params = {'key': API_KEY, 'part': 'snippet', 'id': channel_id_input, 'maxResults': 50}
    response = requests.get(url, params=params)
    r_dict = response.json()

    channelTitle = r_dict['items'][0]['snippet']['title']
    
    # 1.3 brandingSettings + ID
    params = {'key': API_KEY, 'part': 'brandingSettings', 'id': channel_id_input, 'maxResults': 50}
    response = requests.get(url, params=params)
    r_dict = response.json()

    if 'country' in r_dict['items'][0]['brandingSettings']['channel'].keys():
        country = r_dict['items'][0]['brandingSettings']['channel']['country']
    else:
        country = np.nan
    
    # fomualte a dataframe
    channel_summary={
            'channel_title': [channelTitle],
            'channel_id':[channel_id_input], 
            'country': [country],
            'view_count': [viewCount], 
            'subscriber_count': [subscriberCount], 
            'video_count': [videoCount]
            }
    channel_summary = pd.DataFrame(data=channel_summary)
    return channel_summary

def main():

    # Get channel summary
    channel_summary = get_channel_summary('UCCKlp1JI9Yg3-cUjKPdD3mw')
    channel_summary.to_csv('data/channel_summary.csv')


