from tortoise import fields
from tortoise.models import Model

from app.integrations.enums import IntegrationStatus


class Integration(Model):
    integration_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True, min_length=1)
    token = fields.CharField(max_length=50)
    user = fields.ForeignKeyField("models.User", related_name="integrations")
    status = fields.CharEnumField(enum_type=IntegrationStatus)

    def __str__(self):
        return self.name

    class Meta:
        table = "integrations"
