# pylint: disable=missing-class-docstring, missing-module-docstring

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

SQL_INITIAL_LANGUAGES = """
INSERT INTO public.languages (short_name, full_name) VALUES
    ('en', 'English'),
    ('ru', 'Russian');
"""


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=30)),
                ('short_name', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'languages',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'),
                 ),
                ('word', models.CharField(max_length=30)),
                ('translation', models.CharField(max_length=100)),
                ('is_learned', models.BooleanField(default=False)),
                ('added_at', models.DateField(auto_now_add=True)),
                ('language_from', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='language_from_id',
                    to='lelang.language'),
                 ),
                ('language_to', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='language_to_id',
                    to='lelang.language'),
                 ),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL),
                 ),
            ],
            options={
                'db_table': 'words',
                'unique_together': {('word', 'language_to', 'language_from', 'user_id')},
            },
        ),
        migrations.RunSQL(SQL_INITIAL_LANGUAGES),
    ]
