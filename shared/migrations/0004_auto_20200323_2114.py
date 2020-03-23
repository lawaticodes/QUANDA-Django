# Generated by Django 2.2.7 on 2020-03-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_user_confirmed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='logged_in',
            field=models.BooleanField(default=False),
        ),
    ]