# Generated by Django 3.0.3 on 2020-03-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
