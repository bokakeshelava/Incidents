# Generated by Django 4.1.2 on 2022-10-18 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentName',
            fields=[
                ('name', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_creation', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('cve_number', models.CharField(max_length=255)),
                ('object', models.CharField(max_length=255)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.incidentname')),
            ],
        ),
    ]
