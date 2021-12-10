from django.urls import path
from .views import *

urlpatterns = [
    path('white_stripes/', white_stripes, name='white_stripes'),
    path('led_zeppelin/', led_zeppelin, name='led_zeppelin'),
    path('ratm_renegade/', ratm_renegade, name='ratm_renegade'),
    path('pink_floyd_dark_side/', pink_floyd_dark_side, name='pink_floyd_dark_side'),
]