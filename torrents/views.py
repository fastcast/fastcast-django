from django.http import Http404
from django.shortcuts import render

from .models import Torrent

def index(request):
    latest_torrent_list = Torrent.objects.order_by('-pub_date')[:10]
    context = {'latest_torrent_list': latest_torrent_list}
    return render(request, 'torrents/index.html', context)

def detail(request, torrent_id):
    try:
        torrent = Torrent.objects.get(pk=torrent_id)
    except Torrent.DoesNotExist:
        raise Http404("Torrent does not exist")
    similar_torrent_list = Torrent.objects.order_by('?')[:10]
    return render(request, 'torrents/detail.html', {'torrent': torrent, 'similar_torrent_list': similar_torrent_list})

def videos(request):
    latest_torrent_list = Torrent.objects.order_by('-pub_date')[:10]
    return render(request, 'torrents/videos.html', {'latest_torrent_list': latest_torrent_list})
