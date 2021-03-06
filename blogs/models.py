from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Blog(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=150, blank=True, default='')
    slug = models.SlugField()

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.slug)

    def save(self, *args, **kwargs):
        """
        Automatically converts the blog title into a slug
        """
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
