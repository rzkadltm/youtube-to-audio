import os
import re
from pytube import YouTube
from moviepy.editor import AudioFileClip
from django.conf import settings


class YoutubeToAudio:
    def __init__(self, url):
        self.url = url

    def convert_to_audio(self):
        yt = YouTube(self.url)
        title = self._clean_title(yt.title)
        mp4_file = self._download_mp4(title)
        mp3_file = self._convert_to_mp3(mp4_file)
        return mp3_file

    def _clean_title(self, title):
        return re.sub(r'[^\w]', '', title).replace(' ', '')

    def _download_mp4(self, title):
        yt_audio = YouTube(self.url).streams.get_audio_only(subtype='mp4')
        filename = os.path.join(settings.MEDIA_ROOT, title + ".mp4")
        yt_audio.download(output_path=settings.MEDIA_ROOT, filename=filename)
        return filename

    def _convert_to_mp3(self, mp4_file):
        mp3_file = mp4_file.replace(".mp4", ".mp3")
        clip = AudioFileClip(mp4_file)
        clip.write_audiofile(mp3_file)
        clip.close()
        os.remove(mp4_file)
        return os.path.basename(mp3_file)