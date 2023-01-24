
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('todo', include('todo_app.urls')),
    path('api/', include('taskapi.urls')),
    path('', include('base.urls')),
    path('names/', include('numeroji.urls')),
    path('yt/', include('yt_downloader.urls')),
    path('weather', include('weather.urls')),
]
