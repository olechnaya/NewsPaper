from django.contrib.auth.views import LoginView

from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
import datetime

from news.models import Author

class MyCustomLoginView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_datetime = datetime.datetime.now()  
        context['current_datetime'] = current_datetime
        context['is_not_author'] = not self.request.user.groups.filter(name = 'authors').exists()
        return context

@login_required
def upgrade_me(request):
    user = request.user
    #Author.objects.create(name_id=user.id) можно и так
    Author.objects.create(name=user)

    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')

@login_required
def downgrade_me(request):
    user = request.user
    Author.objects.get(name_id=user.id).delete()

    authors_group = Group.objects.get(name='authors')
    if request.user.groups.filter(name='authors').exists():
        authors_group.user_set.remove(user)
    return redirect('/')