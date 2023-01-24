from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
import os

import pytube
import ssl
from django.http import FileResponse
# Create your views here.
def home(request):
    if request.method =='POST':
        # url = request.POST['q']
        
        result = download_video('https://www.youtube.com/watch?v=5YZZSsYSp88')
        
        print(f"download {result}")
        
    return render(request, 'yt_downloader/home.html')


def download_video(url):
    
    if url:
        try:
            
            ssl._create_default_https_context = ssl._create_unverified_context

            # youtube = pytube.YouTube(url)
            # video = pytube.YouTube(url).streams.get_highest_resolution()
            video = pytube.YouTube(url).streams.get_lowest_resolution()

            # video = youtube.streams.first()
            out_file = video.download()

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            print("out_file:" , out_file)
            print('*' * 20)
            print("new file:", new_file)
            print("*" * 20)
            print('video:', video)

            try:
                # with open('my_video.mp4', 'wb') as f:
                #     f.write(new_file)
                rea_response = HttpResponse(new_file, content_type='video/mp4')
                rea_response['Content-Disposition'] = 'attachment; filename=my_video.mp4'
                return rea_response
            except TimeoutError:
                return HttpResponse(TimeoutError)
            # print(video)
            #
            # return video

        except ValueError:
            print(ValueError.args)
            print('Error')
            
            return False