from django.contrib.auth.views import LoginView
from allauth.account.views import LoginView as AllAuthLoginView

from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
import datetime

class MyCustomLoginView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_datetime = datetime.datetime.now()  
        context['current_datetime'] = current_datetime
        context['is_not_author'] = not self.request.user.groups.filter(name = 'authors').exists()
        return context


# # не понятно вообще это где то используется?
# class MyLoginView(AllAuthLoginView):
#     template_name = 'account/login.html'
    


from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

    def form_valid(self, form):
        #save the new user first
        form.save()
        #get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)
    
@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')