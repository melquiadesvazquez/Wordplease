from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):

    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=30)
    description = models.TextField(max_length=150, blank=True, default='')
    slug = models.SlugField()

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.slug)

    def save(self, *args, **kwargs):
        """
        Automatically converts the category name into a slug
        """
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
