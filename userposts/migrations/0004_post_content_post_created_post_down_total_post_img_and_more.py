# Generated by Django 4.2.7 on 2023-11-27 03:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userposts', '0003_remove_post_userposts_p_created_567524_idx_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='down_total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='up_total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['created'], name='userposts_p_created_567524_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['user'], name='userposts_p_user_id_18e3d3_idx'),
        ),
    ]