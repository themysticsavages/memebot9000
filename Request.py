from collections import OrderedDict
import requests
import json
import os
import re

'''
Special types of requests to send
'''

class Reddit:
  def auth(config: str) -> str:
    if os.path.isfile(config):
      _json = json.loads(open(config, encoding='utf-8').read())
      bot = requests.auth.HTTPBasicAuth(_json['client_id'], _json['client_secret'])
      res = requests.post(
        'https://www.reddit.com/api/v1/access_token', 
        auth=bot, 
        data=
        {
        'grant_type': 'password',
        'username': _json['user']['name'],
        'password': _json['user']['passwd']
        }, 
        headers=
        {
        'User-Agent': '{}/0.0.1'.format(_json['app_name'])
        }
      )
      return json.loads(res.text)['access_token']
    else:
      return 'File doesn\'t exist'
  def pull_meme_videos(token: str, app_name: str) -> dict:
    res = requests.get(
      'https://oauth.reddit.com/r/memes/hot', 
      headers=
      {
        **{'User-Agent': '{}/0.0.1'.format(app_name)}, **{'Authorization': f'bearer {token}'}
      }
    )

    return \
      list(
        OrderedDict.fromkeys(
          [
            i.replace('"', '').replace(',', '') \
            for i in re.findall("(?P<url>https?://[^\s]+)", res.text) \
              # video and image urls
              if 'https://v.redd.it/' in i \
                or 'https://i.redd.it' in i \
                  # excludes the Wholesome Award and other stuff
                  and not 'award_images' in i \
                    # exclude post id for the r/memes rules
                    and not 'zi1a2p511m081' in i
          ]
        )
      )

class VideoService:
  '''
  Video service stuff
  '''
  def post_video(f: str, t: str, host: str='http://localhost:5000') -> dict:
    url = host+'/api/post/'
    my_img = {'fstream': open(f, 'rb')}
    r = requests.post(url, files=my_img, data={'title': t})

    return json.loads(r.text)
