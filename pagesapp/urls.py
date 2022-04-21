from django.urls import path
from .views import *
urlpatterns=[
    path('',HomepageView.as_view(),name='home'),
    path('home/',home,name='home'),
    path('about/',AboutpageView.as_view(),name='about'),
]