from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import PostForm

# Create your views here.
class PostsList(ListView):
    model = Post  
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow() # добавим переменную текущей даты time_now
        context['value1'] = None # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context

# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post 
    template_name = 'post.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = '/posts/'

class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'

# дженерик для редактирования объекта
class PostUpdateView(UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = '/posts/'
    
    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        context['isUpdateView'] = True        
        return context
 