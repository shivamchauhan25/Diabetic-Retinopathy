# Generated by Django 3.2 on 2021-04-27 04:11

from django.db import migrations, models
import predict.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eyeimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=predict.models.blog_image_upload)),
            ],
        ),
    ]