# Generated by Django 5.0.1 on 2024-02-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=500)),
                ('Book_Aurthor', models.CharField(max_length=500)),
                ('Book_Type', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Love',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=500)),
                ('Book_Aurthor', models.CharField(max_length=500)),
                ('Book_Type', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Sci_Fyi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=500)),
                ('Book_Aurthor', models.CharField(max_length=500)),
                ('Book_Type', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=500)),
                ('Book_Aurthor', models.CharField(max_length=500)),
                ('Book_Type', models.CharField(max_length=500)),
            ],
        ),
    ]
