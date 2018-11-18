from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user_in_django, logout as finish_user_session
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView

from blogs.models import Blog
from users.forms import SignupForm


class UserBlogsView(View):

    def get(self, request, username):
        user = get_object_or_404(User, username__iexact=username)

        blogs = Blog.objects.filter(author=user.id)

        context = {'blogs': blogs}
        return render(request, 'users/blogs.html', context)


class UsersView(ListView):
    model = User
    template_name = 'users/users.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class LoginView(View):

    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST.get('form_username')
        password = request.POST.get('form_password')
        user = authenticate(request, username=username, password=password)
        if user is None:  # si no existe el usuario con ese username/password
            messages.error(request, 'Wrong username or password')
        else:
            # si el usuario existe, tenemos que hacer login del usuario en la sesión
            login_user_in_django(request, user)
            welcome_url = request.GET.get('next', 'home')
            return redirect(welcome_url)

        return render(request, 'users/login.html')


class LogoutView(View):

    def get(self, request):
        finish_user_session(request)
        messages.success(request, 'You have been logged out successfully!')
        return redirect('login')


class SignupView(View):

    def get(self, request):
        form = SignupForm()
        return render(request, 'users/signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = User()
            new_user.first_name = form.cleaned_data.get('first_name')
            new_user.last_name = form.cleaned_data.get('last_name')
            new_user.username = form.cleaned_data.get('username')
            new_user.email = form.cleaned_data.get('email')
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()
            messages.success(request, 'User registered successfully!')
            form = SignupForm()

        return render(request, 'users/signup.html', {'form': form})

