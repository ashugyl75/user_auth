from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm 


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # name of the url where to redirect after a successful registration

    def form_valid(self, form):
        # save the new user
        form.save()
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name = 'login.html'
    

class UserLogoutView(LogoutView):
    next_page = 'login'  # specify the page to redirect to after logout, usually homepage



class LoginSuccessView(TemplateView):
    template_name = 'login_success.html'