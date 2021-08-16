from django.urls import path
from BATTING.views import *

app_name='BATTING'

urlpatterns=[
    path('HIGHESTRUNS/',HIGHESTRUNS,name='HIGHESTRUNS'),
]