from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.TextField(unique=True)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'User: id = {self.id}, nickname = {self.nickname}'
