import uuid

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from ckeditor.fields import RichTextField


def get_upload_blog_path(instance, filename):
    return '/'.join([settings.FILES_PATH, "blog", str(instance.blog.id), filename])


class BlogCategory(models.Model):
    # Modelo para crear categoria
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class BlogEntry(models.Model):
    # Modelo para crear post
    user = models.ForeignKey(User, related_name="users",
                             on_delete=models.PROTECT)
    name = models.CharField(max_length=128, null=True, blank=True)
    category = models.ManyToManyField(BlogCategory, related_name="categories")
    date = models.DateTimeField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    image_ref = models.ImageField(
        upload_to='blog/', default="image_placeholder.jpg", null=True, blank=True)

    def __str__(self):
        return "blog: {} // De: ".format(self.name, self.user.username)
