from django.urls import path
from .views import index, MainView, PosterListView, CategoryDetailView, CategoryListView, PosterCreateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', MainView.as_view()),
    path('board/', PosterListView.as_view(), name='posters_list'),
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>', CategoryDetailView.as_view()),
    path('create/', PosterCreateView.as_view()),

]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)