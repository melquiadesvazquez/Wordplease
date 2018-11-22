from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView

from blogs.forms import BlogForm
from blogs.models import Blog


class BlogListView(ListView):

    model = Blog
    template_name = 'blogs/blog_list.html'
    paginate_by = 3


class BlogDetailView(DetailView):

    model = Blog
    template_name = 'blogs/blog_detail.html'


class NewBlogView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = BlogForm()
        return render(request, 'blogs/new_blog.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        new_blog = Blog(owner=request.user)
        form = BlogForm(request.POST, instance=new_blog)

        if form.is_valid():
            new_blog = form.save()
            messages.success(request, 'Blog {0} created successfully!'.format(new_blog.title))
            form = BlogForm()

        return render(request, 'blogs/new_blog.html', {'form': form})



