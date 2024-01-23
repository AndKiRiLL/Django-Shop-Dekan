from django.urls import path, include
from .views import *

urlpatterns = [
    path('', page_1, name='page1'),
    path('videocards/', page_2, name='page2'),
    path('ram/', page_3, name='page3'),
    path('pageform/', page_form, name='page_form')
]
