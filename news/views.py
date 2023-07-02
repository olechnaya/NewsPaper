from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages



from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import PostForm
from .filters import PostFilter

from django.shortcuts import render

class AuthorList(ListView):
    model = Author
    template_name = 'authors.html'
    context_object_name = 'authors'
    queryset = Author.objects.order_by('name')

class PostList(ListView):
    model = Post  
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 5 # поставим постраничный вывод в n- элементов

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow() # добавим переменную текущей даты time_now
        context['is_author'] = self.request.user.groups.filter(name = 'authors').exists()
        # context['all_posts'] =  Post.objects.order_by('-dateCreation')
        return context
       
# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post 
    template_name = 'post.html'
    context_object_name = 'post'

# class based  views  выполняют за нас значительную часть задач
# function based views можно использовать также - не забывать
# Каждый раз, когда мы создаем какую-то страницу в джанге, это трехэтапный процесс - создание url, создание вью, создание темплейта
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import timedelta

class PostCreateView(UserPassesTestMixin,LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = '/'
    login_url = '/accounts/login/'

    def test_func(self):
        yesterday = datetime.now() - timedelta(days=1)
        author = Author.objects.get(name_id=self.request.user.id)
        post_per_day = Post.objects.filter(author=author, dateCreation__gt=yesterday).count()
        if post_per_day > 3:
            raise PermissionDenied("Вы уже достаточно наваяли сегодня, отдохните. Допускается постить до 3 штук в день")
        else:
            return redirect('/')
       
    def handle_no_permission(self):        
        # add custom message
        messages.error(self.request, 'Чтобы создать статью, вам нужно войти в качестве автора')
        return redirect(self.get_login_url())
        
class NewsCategoryView(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'
    queryset = Category.objects.all()

# functional view
# def CategoryDetailView(request, pk): # легче дернуть реквест юрл чем в дженериках
#     # нам не нужна модель категорий, всё что нужно от категории - мы получили в cats урла, т.е. только её имя
#     category_posts = Post.objects.filter(category = pk) # в скобках - обращение к полю модели category (models.py - на момент написания кода - 51 строка)
   
#     category = Category.objects.get(id=pk)
#     subscribers = category.subscribers.all()
#     return render(request,'category.html', {'pk': pk, 'category' : category, 'category_posts' : category_posts, 'subscribers': subscribers}) # реквест, шаблон, словарь контекста


#from django.http import JsonResponse
@login_required
def UnsubscribeCategory(request, pk): 
    category = Category.objects.get(pk=pk)
    category.subscribers.remove(request.user.id)
    result = 'Unsubscribed'
    return redirect(request.META.get('HTTP_REFERER'))
    # return JsonResponse(result, safe= False)

@login_required
def SubscribeCategory(request, pk): 
    category = Category.objects.get(pk=pk)
    category.subscribers.add(request.user.id)
    result = 'Unsubscribed'
    return redirect(request.META.get('HTTP_REFERER'))
    #return JsonResponse(result, safe= False)

def CategoryDetailView(request, pk):
   category = Category.objects.get(pk=pk)
   is_subscribed = True if len(category.subscribers.filter(id=request.user.id)) else False
   return render(request,'category.html', 
                 {'category': category,  
                  'is_subscribed' : is_subscribed, #,
                #   'subscribers': category.subscribers.all()
                  'subscribers': category.subscribers.all()
                  }) 
# from django.urls import resolve

# from django.urls import reverse
# from django.http import HttpResponseRedirect
# class NewsCategoryView(ListView):
#     model = Post  
#     template_name = 'categories.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
#     context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты
#     ordering = ['-time_creation']
#     paginate_by = 15
#     #form_class = NewsForm
#     def get_queryset(self):
#         self.id = resolve(self.request.path_info).kwargs['pk']
#         c = Category.objects.get(id=self.id)
#         queryset = Post.objects.filter(category=c)
#         return queryset
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user
#         category  = Category.objects.get(id=self.id)
#         subscribed = category.subscribers.filter(email=user.email)
#         if not subscribed: 
#             context['sub'] = True
#         else:
#             context['sub'] = False
#         context['category'] = category
#         return context    

# def subscribe_to_category(request,pk):
#     user = request.user
#     category = Category.objects.get(id=pk)
#     if not category.subscribers.filter(id=user.id).exists():
#         category.subscribers.add(user.id)
#         email = user.email
#         html_content = render_to_string (
#             'mailing/subscribed.html',
#             {
#                 'categories': category,
#                 'user' : user,
#             },
#         )
#         msg = EmailMultiAlternatives(
#             subject=f'Подтверждение подписи на категорию - {category}',
#             body='',
#             from_email='studium2002_1@mail.ru',
#             to=[email,], # это то же, что и recipients_list
#         )
#         msg.attach_alternative(html_content, "text/html") # добавляем html
#         try:
#             msg.send() # отсылаем  
#         except Exception as e:
#             print(e)
#         return redirect('index')
#     return redirect(request.Meta.get('HTTP_REFERER'))

# def unsubscribe_to_category(request,pk):
#     user = request.user
#     category = Category.objects.get(id=pk)
#     if category.subscribers.filter(id=user.id).exists():
#         category.subscribers.remove(user.id)
#     return redirect('index')

# class CategoryDetail(DetailView):
#     model = Category
#     template_name = 'category.html'
#     queryset = Post.objects.all

class СategoryCreateView(CreateView):
    model = Category
    template_name = 'category_create.html'
    fields = '__all__'
    # form_class = PostForm
    success_url = '/'

# проверка на то, что удаляет её создатель или админ, а не какой либо другой автор 
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

# проверка на то, что редактирует её создатель или админ, а не какой либо другой автор 
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


def error_404(request, exception):
       return render(request, 'errors/404.html', {'exception': exception})

def error_403(request, exception):
        return render(request, 'errors/403.html', {'exception': exception})
