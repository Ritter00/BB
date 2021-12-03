from django.urls import path
from .views import index, MainView, PosterListView

urlpatterns = [
    path('', MainView.as_view()),
    path('board/', PosterListView.as_view(), name='posters_list')
]