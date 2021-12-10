import json

from django.shortcuts import render
from my_module.url_pages import site_links
import datetime

# Create your views here.

page_title = 'каталог'


def catalog(request):
    site_time = datetime.datetime.now()
    with open('json/product_info.json') as file:
        return render(request, 'catalogapp/catalog.html',
                      {'site_links': site_links,
                       'products': json.load(file),
                       'page_title': page_title,
                       'site_time': site_time,
                       }
                      )
