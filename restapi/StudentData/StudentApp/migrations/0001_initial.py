# Generated by Django 2.2.5 on 2021-09-12 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roll_Number', models.IntegerField()),
                ('First_Name', models.CharField(max_length=64)),
                ('Second_Name', models.CharField(max_length=64)),
                ('Age', models.IntegerField()),
            ],
        ),
    ]
