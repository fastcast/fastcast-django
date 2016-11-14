from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

import markdown
import markdown.extensions.tables
import bleach

register = template.Library()


# Modified from http://greg-brant.ghost.io/2015/10/02/rendering-markdown-in-a-django-template/
@register.filter()
@stringfilter
def mark_down(value):
    """
    Renders the given value as Markdown.
    """
    markdown_description = bleach.clean(
        markdown.markdown(value, extensions=['markdown.extensions.tables', 'markdown.extensions.toc']),
        tags=['p', 'a', 'img',
              'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr',
              'ul', 'ol', 'li',
              'blockquote', 'em', 'code', 'pre', 'strong',
              'table', 'thead', 'tbody', 'th', 'tr', 'td'],
        attributes=['id', 'href', 'title', 'src', 'alt']
    )
    return mark_safe(markdown_description)
