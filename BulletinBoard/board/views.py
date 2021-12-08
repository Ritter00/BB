from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Poster, ResponseTTPoster, Category
from django.http import HttpResponse
from .forms import PosterForm

def index(request):
    post= Poster.objects.get(id=1)
    return HttpResponse(f'{post.content}', request)

class MainView(TemplateView):
    template_name= 'main.html'


class PosterListView(ListView):
    queryset = Poster.objects.all()
    template_name = 'board/poster.html'
    context_object_name = 'posters'
    ordering = ['-date_upgrade']


class PosterDetailView(DetailView):
    model = Poster
    template_name = 'board/poster_detail.html'



class CategoryDetailView(DetailView):
    model = Category
    template_name = 'board/category_detail.html'
    queryset = Category.objects.all()



class CategoryListView(ListView):
    model = Category
    template_name = 'board/categories.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PosterCreateView(CreateView):
    form_class = PosterForm
    template_name = 'board/poster_create.html'

    def form_valid(self, form):
        post= form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)



