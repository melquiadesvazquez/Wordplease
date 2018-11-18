from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView

from blogs.models import Blog
from posts.forms import PostForm
from posts.models import Post


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class BlogPostsView(View):

    def get(self, request, blog_slug):
        blog = get_object_or_404(Blog, slug__iexact=blog_slug)

        published_posts = Post.objects.select_related('author').filter(status=Post.PUBLISHED, blog=blog.id). \
            order_by('-last_modification')

        posts_list = published_posts[:4]

        context = {'posts': posts_list}
        return render(request, 'posts/posts.html', context)


class BlogsView(ListView):
    model = Blog
    template_name = 'posts/blogs.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class NewPostView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = PostForm()
        return render(request, 'posts/new_post.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        new_post = Post(author=request.user)
        form = PostForm(request.POST, request.FILES, instance=new_post)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post {0} created successfully!'.format(new_post.title))
            form = PostForm()
        return render(request, 'posts/new_post.html', {'form': form})


class HomeView(View):

    def get(self, request):
        # 1) Obtener los anuncios de la base de datos que están en estPosto PublicPosto
        published_posts = Post.objects. \
            select_related('author'). \
            filter(status=Post.PUBLISHED). \
            order_by('-last_modification')
        posts_list = published_posts[:4]

        # 2) Pasar los anuncios a la plantilla para que ésta los muestre en HTML
        context = {'posts': posts_list}
        return render(request, 'posts/posts.html', context)
