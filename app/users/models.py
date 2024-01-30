from tortoise import fields
from tortoise.models import Model

from app.users.enums import UserStatus


class User(Model):
    user_id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50)
    last_name = fields.CharField(max_length=50)
    email = fields.CharField(max_length=100)
    status = fields.CharEnumField(enum_type=UserStatus)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        table = "users"


class Team(Model):
    team_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, unique=True)
    users = fields.ManyToManyField("models.User", through="teams_memberships", related_name="team")

    class Meta:
        table = "teams"


class TeamMembership(Model):
    membership_id = fields.IntField(pk=True)
    team_id = fields.ForeignKeyField("models.Team", related_name="team_memberships")
    user_id = fields.ForeignKeyField("models.User", related_name="team_membership")

    class Meta:
        table = "teams_memberships"
