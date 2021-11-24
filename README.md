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

Then, create a Google Cloud app instance with the YouTube Data API v3 libary added.
