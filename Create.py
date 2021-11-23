from lib.Request import Reddit
import requests

def download_memes() -> None:
    '''
    Handle Reddit content
    '''

    videos = Reddit.pull_meme_videos(Reddit.auth('secrets/reddit_secrets.json'), 'funny9000')
    ids = []

    for v in videos:
        req = requests.get(v)
        id = v.split('/')[3].split('.')[0]
        if not 'mpd' in v and id not in ids:

            print(v)
            try:
                with open('images/{}.{}'.format(id, v.rsplit('.', 1)[-1].replace('}','').replace(']','')).split('?')[0], 'wb') as f:
                    for chunk in req.iter_content(1024):
                        f.write(chunk)
            except FileNotFoundError:
                pass
            
        ids.append(id)
