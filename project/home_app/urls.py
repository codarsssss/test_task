from django.urls import path

from .views import index

app_name = 'home_app'

urlpatterns = [
    path('', index, name='home')
]
