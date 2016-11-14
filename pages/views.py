from django.http import Http404
from django.shortcuts import render
from django.views import generic

from torrents.models import Torrent
from pages.models import Page, Piece, Section, Carousel, CarouselItem

def index(request):
    carousel_items = CarouselItem.objects.filter(carousel__page__name='home').order_by('slide')
    latest_torrent_list = Torrent.objects.order_by('-pub_date')[:6]
    marketing_content = Piece.objects.filter(page__name='home', section__name='column')[:3]

    return render(request, 'pages/index.html', {'carousel_items': carousel_items, 'latest_torrent_list': latest_torrent_list, 'marketing_content': marketing_content})

def about(request):
    page = Page.objects.filter(name='about')

    piece_container = Piece.objects.filter(page__name='about', section__name='container')[:1]
    return render(request, 'pages/about.html', {'page': page, 'piece_container': piece_container})

def contact(request):
    page = Page.objects.filter(name='contact')

    return render(request, 'pages/contact.html', {'page': page})
