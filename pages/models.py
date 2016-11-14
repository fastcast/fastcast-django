from django.db import models
from accounts.models import UserProfile
from django.core.files.storage import FileSystemStorage

class Page(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Piece(models.Model):
    title = models.CharField(max_length=70)
    page = models.ForeignKey(Page, related_name='pages_piece')
    section = models.ForeignKey(Section, related_name='sections_piece')
    content = models.TextField(help_text='Content can be written in Markdown.')
    image = models.ImageField(null=True, blank=True)
    button = models.CharField(null=True, blank=True, max_length=70)
    url = models.CharField(null=True, blank=True, max_length=70)

    def __str__(self):
        return self.title

class Carousel(models.Model):
    name = models.CharField(max_length=70)
    page = models.ForeignKey(Page, related_name='pages_carousel')

    def __str__(self):
        return self.name

class CarouselItem(models.Model):
    carousel = models.ForeignKey(Carousel, related_name='images')
    title = models.CharField(max_length=70)
    description = models.TextField(null=True, blank=True)
    button = models.CharField(null=True, blank=True, max_length=70)
    url = models.CharField(max_length=70)
    image = models.ImageField()
    slide = models.IntegerField(default=0)

    def __str__(self):
        return self.title
