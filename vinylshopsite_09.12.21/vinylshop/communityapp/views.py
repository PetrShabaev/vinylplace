from django.shortcuts import render
from my_module.url_pages import site_links
import datetime
# Create your views here.

page_title = 'сообщество'


def community(request):
    site_time = datetime.datetime.now()
    return render(request, 'communityapp/community.html',
                  {'site_links': site_links, 'page_title': page_title, 'site_time': site_time})
