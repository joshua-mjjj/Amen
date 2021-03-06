# Generated by Django 3.2.8 on 2021-12-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20211218_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deleted_Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=32)),
                ('deletor_name', models.CharField(max_length=32)),
                ('deletor_file_number', models.CharField(max_length=32)),
                ('deleted_name', models.CharField(max_length=32)),
                ('deleted_file_number', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Deleted Employee',
                'verbose_name_plural': 'Deleted Employees',
            },
        ),
    ]
