import os
import pdb
import re
from pytube import YouTube
from moviepy.editor import *
from django.conf import settings

dir_path = os.path.dirname(os.path.realpath(__file__))

class YoutubeToAudio:
    def __init__(self, url):
        self.title = ''
        self.url = url

    def youtube_to_mp4(self):
        yt = YouTube(self.url)

        self.title = yt.title
        self.title = re.sub(r'[^\w]', '', self.title)
        self.title = self.title.replace(' ', '')
        
        yt_audio = yt.streams.get_audio_only(subtype='mp4')
        yt_audio.download(output_path=settings.MEDIA_ROOT, filename=self.title + ".mp4")

    def MP4ToMP3(self):
        FILETOCONVERT = AudioFileClip(settings.MEDIA_ROOT + "\\" + self.title + ".mp4")
        FILETOCONVERT.write_audiofile(settings.MEDIA_ROOT + "\\" + self.title + ".mp3")
        FILETOCONVERT.close()
        os.remove(settings.MEDIA_ROOT + "\\" + self.title + ".mp4")

        import base64

        with open(settings.MEDIA_ROOT + "\\" + self.title + ".mp3", 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded_data = base64.b64encode(binary_file_data)
            base64_output = base64_encoded_data.decode('utf-8')

            print(base64_output)