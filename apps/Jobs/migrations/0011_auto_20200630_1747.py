# Generated by Django 3.0.5 on 2020-06-30 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0010_auto_20200630_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='filled',
        ),
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(default='', max_length=100),
        ),
    ]