<div align="center">
  <img src="https://raw.githubusercontent.com/ajskateboarder/stuff/main/this.png" height="150"> <br><br>
  <i>An active meme bot on YouTube which compiles memes, makes sh*tposts, and makes remixes of popular sounds</i> <br>
  <h1></h1>
</div>

I know [this thing](https://github.com/sakkshm/MemeBot) exists, but that d̶o̶e̶s̶n̶'̶t̶ ̶g̶e̶t̶ won't be as random. <br>
Meme compilation example:

<a href="https://www.youtube.com/watch?v=n-1HtN4IPiE" target="blank"><img src="https://i.ytimg.com/vi/n-1HtN4IPiE/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBG5aFk-WA9YvtNYbdzMdfmXJg_qA"></a>

## How it works
- Choose between making a meme compilation or a meme edit of a popular video (sh*tpost), or just a sound effect with effects.
  - [x] Traditional meme compilation
    - Take trending memes from the r/memes subreddit on Reddit
    - Download all attachments that are images or animated GIFs
    - Form video with images, and some calm background music
  - [ ] S*hitpost
    - Take any popular video on YouTube
    - Randomly add
      - `what da dog doin`
      - `bruh`
      - `vine boom bass boosted`
      - `...` 
  - [ ] Popular sound with effects
    - Take any sound effect from the YouTube channel ["Gaming Sound FX"](https://www.youtube.com/user/gamingsoundfx)
    - Add any of the following effects:
      - `bass`
      - `echo`
      - `reverb`
      - `...`  
- Send a POST request out to the video hosting service at `/api/post/` with the video and title as headers.

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
Create a Reddit application (set the type to script) under an account that wasn't created with Google or other platforms. <br>
Save the following values to the respective keys in `reddit_secrets.json`:
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
Configure the `bot.config.json` file to your liking:
```json
{
    "web": {
      "port": 5000,
      "host": "http://localhost:5000"
    },
    "bot_video": 1 You most likely won't need to configure this.
}
```
Start the web server:
```bash
python3 wsgi.py &
```
As well as the bot:
```bash
python3 index.py
```
