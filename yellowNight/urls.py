from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from yellowBot.views import keyboard
from yellowBot.views import message

urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^$', keyboard),
    #url(r'^message', message),
    #url(r'^keyboard/', keyboard),
    url(r'',include('yellowBot.urls'))
   
]
