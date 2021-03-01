import uuid
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django.conf import settings


def get_upload_user_path(instance, filename):
    return '/'.join([settings.FILES_PATH, "profile", str(instance.id), filename])


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, related_name="Profile", on_delete=models.PROTECT)
    phone = models.CharField(max_length=12)
    image = models.ImageField(
        upload_to="profile/", default="no-profile-picture.jpg", null=True, blank=True)
    description = models.TextField("Descripción", null=True, blank=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.user.username


class Description(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('titulo', null=True, blank=True, max_length=20)
    description = models.TextField("Descripción", null=True, blank=True)
    link = models.FileField(upload_to='web/files/', null=True, blank=True)
    is_active = models.BooleanField(default=True)


class OtherSites(models.Model):
    color_choices = (
        ("AZUL", "AZUL"),
        ("CELESTE", "CELESTE"),
        ("ROJO", "ROJO"),
        ("NARANJA", "NARANJA"),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField('titulo', null=True, blank=True, max_length=50)
    link = models.URLField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    color = models.CharField(
        max_length=100, choices=color_choices, null=False, blank=False, default="AZUL")


class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.CharField('titulo', null=True, blank=True, max_length=50)
    text = models.TextField()
    book = models.CharField('titulo', null=True, blank=True, max_length=70)
    active = models.BooleanField(default=True)


class Suscriptor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', null=True, blank=True, max_length=250)
    date = models.DateField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)
    email = models.EmailField('E-mail', max_length=200)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['date']


class FriendSites(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)
    name = models.CharField('titulo', null=True, blank=True, max_length=50)
    site_name = models.CharField('sitio', null=True, blank=True, max_length=50)
    link = models.URLField(max_length=255, null=True, blank=True)
    image_ref = models.ImageField(
        upload_to='friendsites/', default="default.jpg", null=True, blank=True)


class Music(models.Model):
    id = models.AutoField(primary_key=True)
    song = models.FileField(upload_to='music/')
    is_active = models.BooleanField(default=True)
