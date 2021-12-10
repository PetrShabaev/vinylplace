from django.shortcuts import render
from my_module.url_pages import site_links
import datetime
# Create your views here.



def white_stripes(request):
    site_time = datetime.datetime.now()
    return render(request, 'productsapp/white_stripes.html', {'site_links': site_links,  'site_time': site_time})


def led_zeppelin(request):
    site_time = datetime.datetime.now()
    return render(request, 'productsapp/led_zeppelin.html', {'site_links': site_links, 'site_time': site_time})


def pink_floyd_dark_side(request):
    site_time = datetime.datetime.now()
    return render(request, 'productsapp/pink_floyd_dark_side.html', {'site_links': site_links, 'site_time': site_time})


def ratm_renegade(request):
    site_time = datetime.datetime.now()
    return render(request, 'productsapp/ratm_renegade.html', {'site_links': site_links, 'site_time': site_time})
