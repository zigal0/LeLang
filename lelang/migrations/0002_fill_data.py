# pylint: disable=missing-class-docstring, missing-module-docstring

from django.db import migrations

WORDS_EXAMPLE_DATA = """
INSERT INTO public.words (word, translation, added_at, is_learned, user_id) VALUES
    ('I', 'Я', CURRENT_DATE, False, 1),
    ('Hate', 'Ненавижу', CURRENT_DATE, False, 1),
    ('Front', 'Передний', CURRENT_DATE, False, 1),
    ('End', 'Конец', CURRENT_DATE, False, 1);
"""


class Migration(migrations.Migration):

    dependencies = [
        ('lelang', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(WORDS_EXAMPLE_DATA)
    ]
