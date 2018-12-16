from django.contrib import messages
from django.contrib.auth import authenticate, login as log_user_in_django, logout as log_user_out_django
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView

from users.forms import UserForm


class UserListView(ListView):

    model = User
    template_name = 'users/user_list.html'
    paginate_by = 3


class UserDetailView(DetailView):

    model = User
    template_name = 'users/user_detail.html'


class NewUserView(View):

    def get(self, request):
        form = UserForm()
        return render(request, 'users/new_user.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            new_user = User()
            new_user.first_name = form.cleaned_data.get('first_name')
            new_user.last_name = form.cleaned_data.get('last_name')
            new_user.username = form.cleaned_data.get('username')
            new_user.email = form.cleaned_data.get('email')
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()
            messages.success(request, 'User {0} created successfully!'.format(new_user.username))
            form = UserForm()

        return render(request, 'users/new_user.html', {'form': form})


class LoginView(View):

    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST.get('form_username')
        password = request.POST.get('form_password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            """
            Return error if the user doesn't exist
            """
            messages.error(request, 'Wrong username or password')
        else:
            """
            if the user exists, store the django session and redirect to the welcome url
            """
            log_user_in_django(request, user)
            welcome_url = request.GET.get('next', 'home')
            return redirect(welcome_url)

        return render(request, 'users/login.html')


class LogoutView(View):

    def get(self, request):
        """
        remove the user from the django session
        """
        log_user_out_django(request)
        messages.success(request, 'You have been logged out successfully!')
        return redirect('login')
