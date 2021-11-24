from moviepy.video.VideoClip import ImageClip
from moviepy.video.fx.resize import resize
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip, concatenate
from PIL import Image
from requests import api
from lib import OCR
import Create
import gtts
import json
import os

'''
Final steps
'''

OCR_SPACE_KEY = json.loads(open('secrets/ocr_space_secrets.json').read())['key']
def compile_memes_raw() -> list:
    clips = []
    text = []

    # for filename in os.listdir('images'):
    #     os.remove(os.path.join('images', filename))
    # Create.download_memes('images')

    for filename in os.listdir('images'):
        if not filename.endswith('.mp4'):
            f = Image.open(os.path.join('images', filename))
            w, h = f.width, f.height

            try:
                f = f.resize((w+600, h+600), Image.ANTIALIAS)
                f.save(os.path.join('images', filename))
            except OSError:
                pass
            
            text.append(OCR.ocr_space_file(os.path.join('images', filename), overlay=True, api_key=OCR_SPACE_KEY))
            clip = ImageClip(os.path.join('images', filename))
            clip.duration = 4
            clip.fps = 10

            clips.append(clip)

    video = concatenate(clips, method='compose')
    video.write_videofile('memes_noaudio.mp4')
    return text
def compile_memes(m) -> None:
    gt = compile_memes_raw()
    print(gt)
    videoclip = VideoFileClip('memes_noaudio.mp4')
    audioclip = AudioFileClip(m)
    i = 0

    for text in gt:
        tts = gtts.gTTS(text=text, lang='en', slow=True)
        tts.save('assets/text{}.mp3'.format(i))
        i += 1

    videoclip.audio = CompositeAudioClip([audioclip])
    videoclip.write_videofile('memes.mp4')

if __name__ == '__main__':
    compile_memes('assets/default_music.mp3')