from django.urls import path

from . import views

# domain.com/website/...
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('home', views.home_view, name="home"),
    path('all_meetings', views.all_meetings_view, name='all_meetings')
]
