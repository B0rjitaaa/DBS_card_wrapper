# Generated by Django 4.0.5 on 2022-07-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_checker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]