# Generated by Django 3.0.1 on 2019-12-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
                ('create_at', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
