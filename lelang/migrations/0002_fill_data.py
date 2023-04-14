# pylint: disable=missing-class-docstring, missing-module-docstring

from django.db import migrations

WORDS_EXAMPLE_DATA = """
INSERT INTO public.words (word, translation, added_at) VALUES
    ('I', 'Я', CURRENT_DATE),
    ('Hate', 'Ненавижу', CURRENT_DATE),
    ('Front', 'Передний', CURRENT_DATE),
    ('End', 'Конец', CURRENT_DATE);
"""


class Migration(migrations.Migration):

    dependencies = [
        ('lelang', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(WORDS_EXAMPLE_DATA)
    ]
