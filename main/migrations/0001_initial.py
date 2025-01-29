# Generated by Django 5.1.4 on 2024-12-20 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kutubxonachi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('ish_vaqt', models.CharField(choices=[('08:00-13:00', '08:00-13:00'), ('13:00-18:00', '13:00-18:00'), ('18:00-23:00', '18:00-23:00')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=10)),
                ('t_sana', models.DateField(blank=True, null=True)),
                ('kitob_soni', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('tirik', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('guruh', models.CharField(max_length=50)),
                ('kurs', models.PositiveSmallIntegerField(default=1)),
                ('kitob_soni', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('janr', models.CharField(max_length=50)),
                ('sahifa', models.PositiveSmallIntegerField()),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.muallif')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olingan_sana', models.DateTimeField()),
                ('qaytargan_sana', models.DateTimeField(blank=True, null=True)),
                ('qaytardi', models.BooleanField(default=False)),
                ('kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kitob')),
                ('kutubxonachi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kutubxonachi')),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.talaba')),
            ],
        ),
    ]
