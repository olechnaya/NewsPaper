from django.urls import path
from . import views

app_name="user"

urlpatterns = [
    # path('<int:pk>',ProfileView.as_view(), name="index"),
    path('<int:pk>', views.profile, name="index"),
]