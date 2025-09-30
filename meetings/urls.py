from django.contrib import admin
from django.urls import path, include
from meetings.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', include('website.urls')),
    path('getAll/', meetings_list_view, name='meetings_list')
]
