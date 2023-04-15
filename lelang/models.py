"""
Contains all models that are used in app.
"""

from django.db import models
from django.conf import settings


class Word(models.Model):
    """Represents word for remembering."""
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=30)
    translation = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    is_learned = models.BooleanField(default=False)
    added_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'words'

    def __str__(self) -> str:
        return f'Word: id = {self.id}, word = {self.word}, ' \
               f'translation = {self.translation}, user_id = {self.user.id}'
