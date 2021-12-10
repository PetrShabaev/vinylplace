from django.shortcuts import render
from my_module.url_pages import site_links
import datetime
# Create your views here.

page_title = 'главная'


def index(request):
    site_time = datetime.datetime.now()
    return render(request, 'mainapp/index.html',
                  {'site_links': site_links, 'site_time': site_time, 'page_title': page_title})
