# Generated by Django 4.1.5 on 2023-01-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_pub_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.URLField(blank=True),
        ),
    ]
