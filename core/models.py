import uuid
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


def get_upload_user_path(instance, filename):
    return '/'.join([settings.FILES_PATH, "profile", str(instance.id), filename])


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, related_name="Profile", on_delete=models.PROTECT)
    phone = models.CharField(max_length=12)
    image = models.ImageField(
        upload_to=get_upload_user_path, default="no-profile-picture.jpg", null=True, blank=True)
    description = models.TextField("Descripción", null=True, blank=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.user.username
