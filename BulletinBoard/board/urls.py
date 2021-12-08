from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', MainView.as_view()),
    path('board/', PosterListView.as_view(), name='posters_list'),
    path('board/<int:pk>',PosterDetailView.as_view(), name='poster_detail'),
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('create/', PosterCreateView.as_view()),

]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)