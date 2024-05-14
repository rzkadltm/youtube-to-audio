import pdb
from . import views
from . import youtube_to_audio
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import FileResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        pdb.set_trace()
        yta = youtube_to_audio.YoutubeToAudio("http://youtube.com/watch?v=2lAe1cqCOXo")
        yta.youtube_to_mp4()
        yta.MP4ToMP3()
        data = request.POST
        url = data.get('url')

        context = {'index': 'success'}
        return render(request, 'index.html', context)

    context = {'index': 'get'}
    return render(request, 'index.html', context)

            # return FileResponse(song.audio_file.open())
