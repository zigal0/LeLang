# pylint: disable=missing-class-docstring, missing-module-docstring

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=30)),
                ('translation', models.CharField(max_length=100)),
                ('is_learned', models.BooleanField(default=False)),
                ('added_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL),
                 ),
            ],
            options={
                'db_table': 'words',
            },
        ),
    ]
