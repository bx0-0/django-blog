# Generated by Django 5.0.4 on 2024-04-05 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_blog', '0006_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=4000),
        ),
    ]
