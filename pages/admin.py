from django.contrib import admin

from pages.models import Page, Section, Piece, Carousel, CarouselItem

class PieceInline(admin.StackedInline):
    model = Piece
    extra = 1

class PageAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {
    #         'fields': ('page', 'section', 'title')
    #     }),
    # ]
    inlines = [PieceInline]

class CarouselItemInline(admin.TabularInline):
    model = CarouselItem
    extra = 3

class CarouselAdmin(admin.ModelAdmin):
    inlines = [ CarouselItemInline, ]

admin.site.register(Section)
admin.site.register(Page, PageAdmin)
admin.site.register(Carousel, CarouselAdmin)
