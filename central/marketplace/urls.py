from marketplace.views import *
from django.urls import path, include

app_name = 'marketplace'

urlpatterns = [
    path('', index, name='home'),

]
