# Generated by Django 4.2.7 on 2023-11-27 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userposts', '0005_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Post Comment', 'verbose_name_plural': 'Post Comments'},
        ),
    ]
