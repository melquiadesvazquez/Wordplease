from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from rest_framework.exceptions import ValidationError

from blogs.models import Blog
from categories.models import Category


class Post(models.Model):

    PUBLISHED = 'PUB'
    DRAFT = 'DRF'

    STATUS = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft')
    )

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name="posts")

    title = models.CharField(max_length=150)
    description = models.TextField()
    content = models.TextField()
    image = models.FileField(blank=True, default='')
    video = models.CharField(max_length=150, blank=True, default='')

    status = models.CharField(max_length=3, choices=STATUS)
    slug = models.SlugField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.get_status_display())

    def save(self, *args, **kwargs):
        """
        Automatically assigns the post to one the user's blog
        """
        if self.blog_id is None:
            blog = Blog.objects.filter(owner=self.author).first()
            if blog is None:
                raise ValidationError('blog field is missing or not valid.')
            else:
                self.blog_id = blog.id

        """
        Automatically converts the post title into a slug
        """
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    """
    def clean(self):

        if self.status == DRAFT and self.pub_date is not None:
            raise ValidationError('Draft entries may not have a publication date.')
        if self.status == PUBLISHED and self.pub_date is None:
            self.pub_date = datetime.date.today()
    """
