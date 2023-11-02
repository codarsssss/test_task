from django.urls import path

from .views import display_model


urlpatterns = [
    path('', display_model),
    path('<int:model_pk>', display_model),
]