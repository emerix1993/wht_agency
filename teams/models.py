from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100,unique=True)

    class Meta:
        ordering = ['name']
        db_table = 'team'

    def __str__(self):
        return self.name
