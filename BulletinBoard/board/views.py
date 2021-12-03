from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Poster, ResponseTTPoster, Category
from django.http import HttpResponse

def index(request):
    post= Poster.objects.get(id=1)
    return HttpResponse(f'{post.content}', request)

class MainView(TemplateView):
    template_name= 'main.html'


class PosterListView(ListView):
    queryset = Poster.objects.all().last()
    template_name = 'board/poster.html'
    context_object_name = 'posters'