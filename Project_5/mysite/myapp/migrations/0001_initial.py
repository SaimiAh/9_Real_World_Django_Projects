# Generated by Django 4.1.4 on 2023-09-09 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('carbs', models.FloatField()),
                ('protien', models.FloatField()),
                ('fats', models.FloatField()),
                ('calorie', models.FloatField()),
            ],
        ),
    ]
