from django.urls import path
from .views import add_author, add_quote

urlpatterns = [
    path('add_author/', add_author, name='add_author'),
    path('add_quote/', add_quote, name='add_quote'),
]
