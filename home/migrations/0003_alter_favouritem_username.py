# Generated by Django 3.2.5 on 2021-07-26 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_favouritem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouritem',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.signupm'),
        ),
    ]