# Generated by Django 5.2 on 2025-04-07 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contato',
        ),
        migrations.AlterModelOptions(
            name='consulta',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='medico',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='paciente',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='prontuario',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'managed': False},
        ),
    ]
