# memebot9000
An active meme bot on YouTube which uploads random memes based on internet knowledge. <br>
I know [this thing](https://github.com/sakkshm/MemeBot) exists, but that doesn't get as random.

## How it works
- Choose between making a meme compilation or a meme edit of a popular video (sh*tpost), or just a sound effect with effects.
  - Traditional meme compilation
    - Take trending memes from the r/memes subreddit on Reddit
    - Download all attachments that are images or videos
    - Scan OCR on images and the first frame of a video
    - Create TTS speech from text
    - Form video with images, TTS, and background music
  - S*hitpost
    - Take any popular video on YouTube
    - Randomly add
      - `what da dog doin`
      - `bruh`
      - `vine boom bass boosted`
      - `...` 
  - Popular sound with effects
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
Install the required packages for pytesseract:
```bash
sudo apt-get update
sudo apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev
```
And required pip packages:
```bash
python3 -m pip install -r requirements.txt
```

Then, create a Google Cloud app instance with the YouTube Data API v3 libary added. Make sure to add a consent screen in order to create Oauth credentials. When you make a consent screen and finish adding Oauth credentials, make sure to download the JSON for it, and put it in the secrets directory as `client_secrets.json`.

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
