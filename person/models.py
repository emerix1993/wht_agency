from django.db import models
from teams.models import Team


class Person(models.Model):
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True,unique=True)
    team = models.ForeignKey(Team, related_name='persons', on_delete=models.SET_DEFAULT, null=True, default=None)

    class Meta:
        ordering = ['last_name', 'first_name']
        db_table = 'person'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"