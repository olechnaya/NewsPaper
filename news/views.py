from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
class PostsList(ListView):
    model = Post  
    template_name = 'posts.html'
    context_object_name = 'posts'

# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post 
    template_name = 'post.html'
    context_object_name = 'post'
