"""
Contains all models that are used in app.
"""

from django.db import models
from django.conf import settings


class Language(models.Model):
    """Supported language in the app."""
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=3)

    class Meta:
        db_table = 'languages'

    def __str__(self) -> str:
        return f'Language: id = {self.id}, full_name = {self.full_name}, ' \
               f'short_name = {self.short_name}'


class Term(models.Model):
    """Represents word."""
    word = models.CharField(max_length=30)
    translation = models.CharField(max_length=100)
    language_from = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='language_from_id',
    )
    language_to = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='language_to_id',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    is_learned = models.BooleanField(default=False)
    added_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('word', 'language_to', 'language_from', 'user_id',)
        db_table = 'terms'

    def __str__(self) -> str:
        return f'Term: word = {self.word}, translation = {self.translation}, ' \
               f'user_id = {self.user.id}'
