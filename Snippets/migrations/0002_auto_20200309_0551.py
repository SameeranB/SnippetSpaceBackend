# Generated by Django 3.0.3 on 2020-03-09 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snippet',
            name='special_instructions',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
