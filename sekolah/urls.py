from django.urls import path
from . import views

app_name = 'sekolah'
urlpatterns = [
    # post views
    path('', views.guru_list, name='post_list'),

    ]