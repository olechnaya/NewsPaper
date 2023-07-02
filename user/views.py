from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from news.models import Category

# Create your views here.

# @login_required
# class ProfileView(DetailView):
#     model = User 
#     categories = Category.objects.all()
#     template_name = 'user/profile.html'
#     context_object_name = 'user'

#     # categories.subscribers.filter(id=self.request.user.id)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)        
#         context['is_author'] = self.request.user.groups.filter(name = 'authors').exists()
#         #context['categories_user_subscribed'] =  
#         return context

def profile(request, pk):
    if request.user.is_authenticated:
        profile = User.objects.get(pk=pk)
        categories = Category.objects.all()
        subscribed_to = []
        for cat in categories:
            if cat.subscribers.filter(id=pk).exists():
                subscribed_to.append(cat)
        return render(request,"user/profile.html", {"profile":profile,"categories_subscribed_to": subscribed_to})
    else:
        messages.success(request,('Надо залогиниться'))
        return redirect('home')