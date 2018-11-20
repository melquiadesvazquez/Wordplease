from django.contrib import messages
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView

from blogs.forms import BlogForm
from blogs.models import Blog


class BlogListView(ListView):

    model = Blog
    template_name = 'blogs/blog_list.html'
    paginate_by = 10


class BlogDetailView(DetailView):

    model = Blog
    template_name = 'blogs/blog_detail.html'


class NewBlogView(View):

    def get(self, request):
        form = BlogForm()
        return render(request, 'blogs/new_blog.html', {'form': form})

    def post(self, request):
        form = BlogForm(request.POST)

        if form.is_valid():
            new_blog = form.save()
            messages.success(request, 'Blog {0} created successfully!'.format(new_blog.title))
            form = BlogForm()

        return render(request, 'blogs/new_blog.html', {'form': form})
