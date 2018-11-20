from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView

from blogs.models import Blog
from posts.forms import PostForm
from posts.models import Post


class PostListView(ListView):

    template_name = 'posts/post_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects. \
            select_related('blog'). \
            select_related('author'). \
            select_related('category'). \
            filter(status=Post.PUBLISHED). \
            order_by('-last_modification')

        if 'blog_slug' in self.kwargs:
            blog = get_object_or_404(Blog, slug__iexact=self.kwargs['blog_slug'])
            queryset = queryset.filter(blog=blog.id)

        return queryset


class PostDetailView(DetailView):

    model = Post
    template_name = 'posts/post_detail.html'


class NewPostView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = PostForm(request.user)
        return render(request, 'posts/new_post.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        new_post = Post(author=request.user)
        form = PostForm(request.user, request.POST, request.FILES, instance=new_post)

        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post {0} created successfully!'.format(new_post.title))
            form = PostForm()

        return render(request, 'posts/new_post.html', {'form': form})
