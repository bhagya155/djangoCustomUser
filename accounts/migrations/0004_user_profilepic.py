# Generated by Django 3.1.1 on 2023-04-11 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]
