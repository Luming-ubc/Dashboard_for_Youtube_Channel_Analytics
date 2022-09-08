# %%
import requests
import pandas as pd
import time

# Get API_KEY followed instructions here: https://www.slickremix.com/docs/get-api-key-for-youtube
# load in API KEY
with open('youtube_api_key.txt', 'r') as f:
    API_KEY = f.read()
    

# %%
# use search url
url = 'https://www.googleapis.com/youtube/v3/search'
# UCupvZG-5ko_eiXAupbDfxWw
# UCP-3kpzMMSUek7EqStDWypA
params = {'key': API_KEY, 'part': 'snippet', 'channelId': 'UCP-3kpzMMSUek7EqStDWypA', 'maxResults': 50}
response = requests.get(url, params=params)
r_dict = response.json()

# get relevant information from search url
channelTitle = r_dict['items'][0]['snippet']['channelTitle']
channelId = r_dict['items'][0]['snippet']['channelId']

videoId = r_dict['items'][0]['id']['videoId']

title = r_dict['items'][0]['snippet']['title']
description = r_dict['items'][0]['snippet']['description']
publishTime = r_dict['items'][0]['snippet']['publishTime']

videoId
# %%
# use Videos url
url = 'https://www.googleapis.com/youtube/v3/videos'

params = {'key': API_KEY, 'part': ['statistics', 'localizations', 'contentDetails'], 'id': videoId, 'maxResults': 50}
response = requests.get(url, params=params)
r_dict = response.json()

# get relevant information from Video url
videoId = r_dict['items'][0]['id']
viewCount = r_dict['items'][0]['statistics']['viewCount']
likeCount = r_dict['items'][0]['statistics']['likeCount']
favoriteCount = r_dict['items'][0]['statistics']['favoriteCount']
commentCount = r_dict['items'][0]['statistics']['commentCount']
r_dict


# %%
# get overall stats for a channel
url = "https://www.googleapis.com/youtube/v3/channels"

params = {'key': API_KEY, 'part': 'statistics', 'id': channelId, 'maxResults': 50}
response = requests.get(url, params=params)
r_dict = response.json()

viewCount = r_dict['items'][0]['statistics']['viewCount']
subscriberCount = r_dict['items'][0]['statistics']['subscriberCount']
videoCount = r_dict['items'][0]['statistics']['videoCount']
r_dict


# %%
# get channel country
url = "https://www.googleapis.com/youtube/v3/channels"

params = {'key': API_KEY, 'part': 'brandingSettings', 'id': channelId, 'maxResults': 50}
response = requests.get(url, params=params)
r_dict = response.json()

keywords = r_dict['items'][0]['brandingSettings']['channel']['keywords']
country = r_dict['items'][0]['brandingSettings']['channel']['country']
image = r_dict['items'][0]['brandingSettings']['image']['bannerExternalUrl']

# %%
# use playlists url
url = 'https://www.googleapis.com/youtube/v3/playlists'

params = {'key': API_KEY, 'part': 'contentDetails', 'channelId': channelId}
response = requests.get(url, params=params)
r_dict = response.json()
r_dict
# %%
params = {'key': API_KEY, 'part': 'brandingSettings', 'id': channelId, 'maxResults': 50}
response = requests.get(url, params=params)
r_dict = response.json()

country = r_dict['items'][0]['brandingSettings']['channel']['country']

# %%
# find channelId
# use search url
url = 'https://www.googleapis.com/youtube/v3/search'
params = {'key': API_KEY, 'part': 'snippet', 'maxResults': 50}
response = requests.get(url, params=params)
r_dict = response.json()

r_dict















# %%
channel_id_input = 'UCP-3kpzMMSUek7EqStDWypA'
# %%
channel_id_input = 'UCupvZG-5ko_eiXAupbDfxWw'

# %%
# 1. channels
url = "https://www.googleapis.com/youtube/v3/channels"
# 1.2. part:snippet + filter: id (channelID)
params = {'key': API_KEY, 'part': 'snippet', 'id': channel_id_input, 'maxResults': 50}
response = requests.get(url, params=params)
r_dict = response.json()

r_dict
# %%
channelTitle = r_dict['items'][0]['snippet']['title']
channelTitle


# %%
# 1.3 brandingSettings + ID
params = {'key': API_KEY, 'part': 'brandingSettings', 'id': channel_id_input, 'maxResults': 50}
response = requests.get(url, params=params)
r_dict = response.json()

if 'country' in r_dict['items'][0]['brandingSettings']['channel'].keys():
    country = r_dict['items'][0]['brandingSettings']['channel']['country']
else:
    country = 'Not Specified'
# %%
country
# %%
