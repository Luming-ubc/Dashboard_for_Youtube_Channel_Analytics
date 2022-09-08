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
    Args:
        channel_id_input (str): youtube channel id
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
    data={
            'channel_title': [channelTitle],
            'channel_id':[channel_id_input], 
            'country': [country],
            'view_count': [viewCount], 
            'subscriber_count': [subscriberCount], 
            'video_count': [videoCount]
            }
    df = pd.DataFrame(data=data)
    return df

get_channel_summary('UCCKlp1JI9Yg3-cUjKPdD3mw')
# %%
# TEST get_channel_summary BY CNN
get_channel_summary('UCP-3kpzMMSUek7EqStDWypA')

# %%
# TEST get_channel_summary BY DAOYUESHE
get_channel_summary('UCupvZG-5ko_eiXAupbDfxWw')






































#  TTTTTTTTTTTT    EEEEEEEEEEE         SSSSSSSSSS        TTTTTTTTTTTTT
#      TTT         EEE                SSSS      SSS            TTT
#      TTT         EEE                   SSSS                  TTT
#      TTT         EEEEEEEEE                SSS                TTT
#      TTT         EEE                        SSS              TTT
#      TTT         EEE                SSSS      SSS            TTT
#      TTT         EEEEEEEEEEEE         SSSSSSSS               TTT    

# %%
channel_id_input = 'UCupvZG-5ko_eiXAupbDfxWw'
# %%
channel_id_input = 'UCP-3kpzMMSUek7EqStDWypA'



# %%
def get_video_details(video_id):
    with open('youtube_api_key.txt', 'r') as f:
        API_KEY = f.read()
    
    url = 'https://www.googleapis.com/youtube/v3/videos'

    params = {'key': API_KEY, 'part': ['statistics', 'localizations', 'contentDetails'], 'id': video_id, 'maxResults': 50}
    response = requests.get(url, params=params)
    r_dict = response.json()

    view_count = r_dict['items'][0]['statistics']['viewCount']
    like_count = r_dict['items'][0]['statistics']['likeCount']
    favoriteCount = r_dict['items'][0]['statistics']['favoriteCount']
    dislike_count = r_dict['items'][0]['statistics']['dislikeCount']
    comment_count = r_dict['items'][0]['statistics']['commentCount']

    return view_count, like_count, favoriteCount, dislike_count, comment_count



# %%
# FROM A CHANNEL ID TO GET ALL ITS VIDEO IDS

def get_videos_summary_from_channel(channel_id_input):
    with open('youtube_api_key.txt', 'r') as f:
        API_KEY = f.read()

    pageToken = ""

    videoId = []
    title = []
    description = []
    publishTime = []

    while True:
        # 2. search url
        url = "https://www.googleapis.com/youtube/v3/search/"
        
        # 2.1 snipet + id
        params = {'key': API_KEY, 'part': 'snippet', 'channelId': channel_id_input, 'maxResults': 50, 'pageToken': pageToken}
        response = requests.get(url, params=params)
        time.sleep(1)
        r_dict = response.json()

        # update lists
        for item in r_dict['items']:
            if 'videoId' in item['id'].keys():
                vi = item['id']['videoId']
                videoId.append(vi)
                title.append(item['snippet']['title'])
                description.append(item['snippet']['description'])
                publishTime.append(item['snippet']['publishTime'])

        print(len(videoId))

        # automatic turn to next page
        try:
            if r_dict['nextPageToken'] != None: #if none, it means it reached the last page and break out of it
                pageToken = r_dict['nextPageToken']

        except:
            break

    df = pd.DataFrame(data = {
        'video_id': videoId,
        'video_title': title,
        'publish_time': publishTime,
        "description": description
        })

    return df


get_videos_summary_from_channel('UCP-3kpzMMSUek7EqStDWypA')
## FROM VIDEO ID TO GET ITS STATISTICS


# %%
videoId
# %%
title
# %%
description
# %%
publishTime



























# %%

def get_video_summary(channel_id_input):
    # 2. search url
    url = "https://www.googleapis.com/youtube/v3/search"

    # 2.1 snipet + id
    params = {'key': API_KEY, 'part': 'snippet', 'channelId': channel_id_input, 'maxResults': 50}
    response = requests.get(url, params=params)
    r_dict = response.json()

    videoId = []
    title = []
    description = []
    publishTime = []
    for item in r_dict['items']:
        if 'videoId' in item['id'].keys():
            videoId.append(item['id']['videoId'])
            title.append(item['snippet']['title'])
            description.append(item['snippet']['description'])
            publishTime.append(item['snippet']['publishTime'])



# %%
len(videoId)
# %%
