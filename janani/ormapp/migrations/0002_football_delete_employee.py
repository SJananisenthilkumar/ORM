# Generated by Django 4.2.6 on 2023-11-04 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Football',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('mobileno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('age', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
