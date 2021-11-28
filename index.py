from moviepy.video.VideoClip import ImageClip
from moviepy.video.fx.resize import resize
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip, concatenate
from Request import VideoService
from PIL import Image
import Create
import json
import os

'''
Final steps
'''

def compile_memes_raw() -> None:
    clips = []

    print('Cleaning previously used memes...')
    for filename in os.listdir('images'):
        os.remove(os.path.join('images', filename))
    Create.download_memes('images')

    print('Compressing images and attaching to video...')
    for filename in os.listdir('images'):
        if not filename.endswith('.mp4'):
            f = Image.open(os.path.join('images', filename))
            w, h = f.width, f.height

            try:
                f = f.resize((w+600, h+600), Image.ANTIALIAS)
                f.save(os.path.join('images', filename))
            except OSError:
                pass
            
            clip = ImageClip(os.path.join('images', filename))
            clip.duration = 4
            clip.fps = 10

            clips.append(clip)

    print('Writing to memes_noaudio.mp4...')
    video = concatenate(clips, method='compose')
    video.write_videofile('memes_noaudio.mp4')
    return None
def compile_memes(m) -> None:
    try:
        os.remove('memes_noaudio.mp4')
        os.remove('memes.mp4')
    except FileNotFoundError:
        pass

    compile_memes_raw()

    print('Adding default background music...')
    videoclip = VideoFileClip('memes_noaudio.mp4')
    audioclip = AudioFileClip(m)

    videoclip.audio = CompositeAudioClip([audioclip])
    videoclip.write_videofile('memes.mp4')

if __name__ == '__main__':
    compile_memes('assets/default_music.mp3')
    
    count = json.load(open('bot.config.json'))
    VideoService.post_video('memes.mp4', 'Freshly made memes #{}'.format(count['bot_video']), count['web']['host'])
    
    count['bot_video'] += 1
    json.dump(count, open('bot.config.json', 'w'))

