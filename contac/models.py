from django.db import models
# Create your models here.


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombres', max_length=100)
    lastname = models.CharField('Apellidos', max_length=150)
    email = models.EmailField('E-mail', max_length=200)
    issue = models.CharField('Asunto', max_length=100)
    messaje = models.TextField('Mensaje')
    state = models.BooleanField('Estado', default=True)
    date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.issue
