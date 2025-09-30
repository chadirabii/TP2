from urllib import request
from django.shortcuts import get_object_or_404, render

from meetings.models import Meeting

# Create your views here.


def home_view(request):
    context = {'nbre_meeting': Meeting.objects.count()}
    return render(request, "website/home.html", context=context)


def about_view(request):
    return render(request, "website/about.html")


def all_meetings_view(request):
    meetings = {'meetings': Meeting.objects.all()}
    return render(request, "website/all_meetings.html", context=meetings)


def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def detail(request, id):
    meeting = get_object_or_404(Meeting, id=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})
