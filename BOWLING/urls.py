from django.urls import path
from BOWLING.views import *

app_name='BOWLING'

urlpatterns=[
    path('WICKETS/',WICKETS,name='WICKETS'),
]