# Generated by Django 3.1.1 on 2023-04-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.CharField(default=123456, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
