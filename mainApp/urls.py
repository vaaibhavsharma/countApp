from django.urls import path
from .views import main, countHandler
urlpatterns = [
    path('', main, name='main'),
    path('ajax', countHandler, name='handler')
]