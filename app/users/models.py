from tortoise import fields
from tortoise.models import Model

from app.users.enums import UserStatus


class User(Model):
    user_id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50, min_length=1)
    last_name = fields.CharField(max_length=50, min_length=1)
    email = fields.CharField(max_length=100, unique=True, min_length=1)
    status = fields.CharEnumField(enum_type=UserStatus)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        table = "users"


class Team(Model):
    team_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True, min_length=1)
    users = fields.ManyToManyField("models.User", through="teams_memberships", related_name="teams")

    class Meta:
        table = "teams"
