
import pandas as pd
import requests

# a random website
image_url = 'https://imgs.xkcd.com/comics/python.png'
r = requests.get(image_url)

# check all available methods
print(dir(r))
# print(help(r))  # more detailed
print(r.status_code)  # 200 is success
print(r.ok)  # anything < 400, or not failed
print(r.headers)

# print(r.content)  # in unicode
# save r.content to image.png
with open('image.png', 'wb') as f:  # write bits mode, in current dir
    f.write(r.content)

# test with httpbin.org with get method
payload = {'page':2, 'count':25}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text)
print(r.url)

# post method
payload = {'username': 'First', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)

r_dict = r.json() # capture json response in python dict
print(r_dict['form'])


# test Auth
r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))  # tuple
print(r.text)


r = requests.get('https://httpbin.org/delay/1', timeout=3)
print(r)
