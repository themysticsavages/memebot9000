<div align="center">
  <img src="https://raw.githubusercontent.com/ajskateboarder/stuff/main/this.png" height="150"> <br><br>
  An active meme bot on YouTube which uploads random memes based on internet knowledge. <br>
  <h1></h1>
</div>

I know [this thing](https://github.com/sakkshm/MemeBot) exists, but that d̶o̶e̶s̶n̶'̶t̶ ̶g̶e̶t̶ won't be as random.

Meme compilation example:

<a href="https://www.youtube.com/watch?v=n-1HtN4IPiE" target="blank"><img src="https://i.ytimg.com/vi/n-1HtN4IPiE/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBG5aFk-WA9YvtNYbdzMdfmXJg_qA"></a>

## How it works
- Choose between making a meme compilation or a meme edit of a popular video (sh*tpost), or just a sound effect with effects.
  - [x] Traditional meme compilation (incomplete)
    - Take trending memes from the r/memes subreddit on Reddit
    - Download all attachments that are images or videos
    - When using a video, the first frame is used. (not done)
    - Form video with images, and some calm background music
  - [ ] S*hitpost
    - Take any popular video on YouTube
    - Randomly add
      - `what da dog doin`
      - `bruh`
      - `vine boom bass boosted`
      - `...` 
  - [ ] Popular sound with effects
    - Take any sound effect from the YouTube channel "Gaming Sound FX"
    - Add any of the following effects:
      - `bass`
      - `echo`
      - `reverb`
      - `...`  

This is pretty much how the whole thing will work.

## Usage
Clone the repo:
```bash
git clone https://github.com/themysticsavages/memebot9000.git
cd memebot9000
```
Install required pip packages:
```bash
python3 -m pip install -r requirements.txt
```

Then, create a Google Cloud app instance with the YouTube Data API v3 libary added. It is free and no credit card is needed, unless you happened to reach the project quota. Make sure to add a consent screen in order to create Oauth credentials. When you make a consent screen and finish adding Oauth credentials, make sure to download the JSON for it, and put it in the secrets directory as `client_secrets.json`.

After that, create a Reddit application (set the type to script) under an account that wasn't created with Google or other platforms. <br>
Save the following values to the respective keys in `reddit_secrets.json` in the secrets directory:
```json
{
    "app_name": "",
    "client_id":"", 
    "client_secret": "",
    "user": {
      "name": "",
      "passwd":""
    }
}
```

! unfinished !
