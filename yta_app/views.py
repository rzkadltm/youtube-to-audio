from .youtube_to_audio import YoutubeToAudio
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            yta = YoutubeToAudio(url)
            audio_file = yta.convert_to_audio()
            return render(request, 'index.html', {'audio_file': audio_file})
    return render(request, 'index.html')
