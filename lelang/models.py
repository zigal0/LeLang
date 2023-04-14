"""
Contains all models that are used in app.
"""

from django.db import models


class Word(models.Model):
    """Represents word for remembering."""
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=30)
    translation = models.CharField(max_length=100)
    added_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'words'

    def __str__(self) -> str:
        return f'Word: id = {self.id}, word = {self.word}, ' \
               f'translation = {self.translation}, added_at = {self.added_at}'
