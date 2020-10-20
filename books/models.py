import uuid
from django.db import models
from django.conf import settings


def get_upload_blog_path(instance, filename):
    return '/'.join([settings.FILES_PATH, "books", str(instance.blog.id), filename])

# Create your models here.


class BookEntry(models.Model):
    # Modelo para crear categoria
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='books/images/', null=True, blank=True)
    link = models.FileField(upload_to='books/files/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
