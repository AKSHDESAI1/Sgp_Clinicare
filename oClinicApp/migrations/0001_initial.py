# Generated by Django 4.0 on 2022-02-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('gender1', models.CharField(choices=[('male1', 'Male'), ('female1', 'Female')], max_length=7)),
                ('date1', models.DateField()),
                ('blood1', models.CharField(choices=[('male1', 'Male'), ('female1', 'Female')], max_length=7)),
                ('dia1', models.CharField(choices=[('male1', 'Male'), ('female1', 'Female')], max_length=7)),
                ('medical', models.TextField()),
                ('alergies', models.TextField()),
            ],
        ),
    ]
