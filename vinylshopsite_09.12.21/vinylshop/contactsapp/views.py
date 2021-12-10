from django.shortcuts import render
from my_module.url_pages import site_links
import datetime
# Create your views here.

page_title = 'контакты'


def contacts(request):
    site_time = datetime.datetime.now()
    return render(request, 'contactsapp/contacts.html',
                  {'site_links': site_links, 'page_title': page_title, 'site_time': site_time})
