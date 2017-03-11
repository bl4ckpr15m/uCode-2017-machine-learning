from django import template
from random import randint
from uCode.local_settings import tumblr_api


register = template.Library()


@register.simple_tag
def picture():
    offset = randint(0, 100)
    # offset = 0

    data = tumblr_api.posts('adidasoriginals', limit=1, offset=offset)
    try:
        image = data['posts'][0]['photos'][0]['original_size']['url']
        if(not image is None):
            return image
        else:
            picture()
    except KeyError:
        picture()
    except IndexError:
        picture()
