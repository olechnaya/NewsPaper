from django.contrib.auth.views import LoginView
import datetime

class MyCustomLoginView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_datetime = datetime.datetime.now()  
        context['current_datetime'] = current_datetime
        return context