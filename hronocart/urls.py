from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_window.as_view())
]