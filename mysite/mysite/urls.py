from django.contrib import admin  
from django.urls import path, include  


urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('news', include('news.urls')),  # наше приложение news
    path('', include('news.urls')),  # наше приложение news
]