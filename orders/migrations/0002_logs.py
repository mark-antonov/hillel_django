# Generated by Django 3.2.4 on 2021-06-13 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
                ('method', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]