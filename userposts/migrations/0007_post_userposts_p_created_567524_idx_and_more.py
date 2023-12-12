# Generated by Django 4.2.7 on 2023-11-27 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userposts', '0006_alter_comment_options'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['created'], name='userposts_p_created_567524_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['user'], name='userposts_p_user_id_18e3d3_idx'),
        ),
    ]