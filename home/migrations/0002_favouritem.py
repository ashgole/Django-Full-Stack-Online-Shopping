# Generated by Django 3.2.5 on 2021-07-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='favouriteM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('username', models.CharField(max_length=50)),
                ('productid', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'favourite',
            },
        ),
    ]