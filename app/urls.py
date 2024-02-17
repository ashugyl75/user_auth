from django.urls import path
from .views import RegisterView, UserLoginView, UserLogoutView, LoginSuccessView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('login/success/', LoginSuccessView.as_view(), name='login_success'),
]