# Generated by Django 3.2.8 on 2022-06-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='review',
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(auto_created=True),
        ),
    ]