"""
Contains all models that are used in app.
"""

from django.db import models


class User(models.Model):
    """User is example model-class"""
    id = models.AutoField(primary_key=True)
    nickname = models.TextField(unique=True)
    birth_date = models.DateField()

    class Meta:
        db_table = 'user'

    def __str__(self) -> str:
        return f'User: id = {self.id}, ' \
               f'nickname = {self.nickname}, birth_date = {self.birth_date}'
