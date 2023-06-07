from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import PostForm
from .filters import PostFilter



class PostsList(ListView):
    model = Post  
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 5 # поставим постраничный вывод в один элемент

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow() # добавим переменную текущей даты time_now
        context['is_not_author'] = not self.request.user.groups.filter(name = 'authors').exists()
        return context
    
    

# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post 
    template_name = 'post.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = '/'
    login_url = '/accounts/login/'
    
    def handle_no_permission(self):        
        # add custom message
        messages.error(self.request, 'Чтобы создать статью, вам нужно войти в качестве автора')
        return redirect(self.get_login_url())

class PostDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post')
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/'
    login_url = '/accounts/login/'
    
    def handle_no_permission(self):        
        # add custom message
        messages.error(self.request, 'Чтобы удалить статью, вам нужно войти в качестве автора')
        return redirect(self.get_login_url())

# дженерик для редактирования объекта
class PostUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')    
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = '/'
    login_url = '/accounts/login/'
    
    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        context['isUpdateView'] = True        
        return context
    
    def handle_no_permission(self):        
        # add custom message
        messages.error(self.request, 'Чтобы редактировать статью, вам нужно войти в качестве автора')
        return redirect(self.get_login_url())

class PostSearch(ListView):
    model = Post  
    template_name = 'posts_search.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-dateCreation')

    def get_context_data(self, **kwargs): # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset()) # вписываем наш фильтр в контекст
        return context

