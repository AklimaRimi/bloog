# Generated by Django 4.0.3 on 2022-03-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='Images'),
        ),
    ]
