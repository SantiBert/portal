from audit.models import AuditActions
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)


class Audits:

    @classmethod
    def audit_action(cls, user, action, description, action_type):
        try:
            audit_instance = AuditActions()
            audit_instance.user = user
            audit_instance.action = action
            audit_instance.description = description
            audit_instance.action_type = action_type
            audit_instance.save()
        except Exception as e:
            logger.error(str(e))
