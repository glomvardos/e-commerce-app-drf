# Generated by Django 4.0.6 on 2022-12-03 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]