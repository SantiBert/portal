from django.contrib.auth.models import User
from django.db import models

POSIBLE_ACTIONS = [
    ("DELETE", "DELETE"),
    ("CREATE", "CREATE"),
    ("EDIT", "EDIT"),
]


class AuditActions(models.Model):
    """Este modelo se utiliza para guardar las diferentes acciones que se realizan 
    en la base de datos.
    """
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    action = models.CharField(null=False, blank=False, max_length=400)
    description = models.CharField(null=True, blank=True, max_length=400)
    action_type = models.CharField(
        null=False, blank=False, max_length=100, choices=POSIBLE_ACTIONS
    )

    def __str__(self):
        return f"{self.date} - {self.action}"
