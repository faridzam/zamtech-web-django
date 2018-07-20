# Generated by Django 2.0.5 on 2018-06-05 13:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='finance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField(null=True)),
                ('withdrawal', models.IntegerField(null=True)),
                ('deposit', models.IntegerField(null=True)),
                ('activity_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
