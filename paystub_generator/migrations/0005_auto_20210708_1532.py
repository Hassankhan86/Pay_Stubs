# Generated by Django 3.1.4 on 2021-07-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paystub_generator', '0004_image_upld'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_upld',
            name='logo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]