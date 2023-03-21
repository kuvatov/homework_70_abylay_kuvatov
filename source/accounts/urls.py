from django.urls import path
from django.contrib.auth import views as auth
from accounts.views import RegisterView

urlpatterns = [
    path('login/', auth.LoginView.as_view(), name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register')
]
