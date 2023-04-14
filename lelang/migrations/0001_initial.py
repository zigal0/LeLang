# pylint: disable=missing-class-docstring, missing-module-docstring

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=30)),
                ('translation', models.CharField(max_length=100)),
                ('added_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'words',
            },
        ),
    ]
