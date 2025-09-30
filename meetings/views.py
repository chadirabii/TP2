from django.shortcuts import render

from meetings.models import Meeting

# Create your views here.


def meetings_list_view(request):
    meetings = Meeting.objects.all()
    return render(request, "meetings.html", {"meetings": meetings})
