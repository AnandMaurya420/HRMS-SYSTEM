# Generated by Django 4.1.7 on 2024-02-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_leave_request_notify_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_request',
            name='selectleave',
            field=models.CharField(choices=[('first half', 'first half'), ('second half', 'second half'), ('full day', 'full day')], max_length=100, null=True),
        ),
    ]
