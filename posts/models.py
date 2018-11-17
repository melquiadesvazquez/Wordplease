from django.contrib.auth.models import User
from django.db import models

from categories.models import Category


class Post(models.Model):

    PUBLISHED = 'PUB'
    DRAFT = 'DRF'

    STATUS = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    content = models.TextField()
    image = models.FileField()
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=Category.DEFAULT_PK)
    likes = models.IntegerField(default=0)
    status = models.CharField(max_length=3, choices=STATUS)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.get_status_display())
