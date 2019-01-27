# Generated by Django 2.1.5 on 2019-01-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField()),
                ('lieu', models.TextField()),
                ('type', models.TextField()),
                ('etat', models.TextField()),
                ('race', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField()),
                ('dispo', models.TextField()),
            ],
        ),
    ]
