from django.db.models import Model, IntegerField, ForeignKey, CharField, ManyToManyField, CASCADE
from django.contrib.auth.models import User


class Entity(Model):
    modified_by = ForeignKey(User, on_delete=CASCADE)
    value = IntegerField()
    properties = ManyToManyField('Property')


class Property(Model):
    key = CharField(max_length=50)
    value = CharField(max_length=50)

    def __str__(self):
        return f"{self.key}: {self.value}"
