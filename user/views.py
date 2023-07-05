from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from news.models import Category

def profile(request, pk):
    if request.user.is_authenticated:
        profile = User.objects.get(pk=pk)
        categories_subscribed_to = list(Category.objects.all().filter(subscribers=request.user))
        # categories = Category.objects.all()
        # subscribed_to = []
        # for cat in categories:
        #     if cat.subscribers.filter(id=pk).exists():
        #         subscribed_to.append(cat)
        return render(request,"user/profile.html", {"profile":profile,"categories_subscribed_to": categories_subscribed_to})
    else:
        messages.success(request,('Надо залогиниться'))
        return redirect('home')