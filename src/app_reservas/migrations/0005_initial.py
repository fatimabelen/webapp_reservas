# Generated by Django 4.2.7 on 2023-12-01 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_reservas', '0004_delete_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reserva', models.DateTimeField(auto_now_add=True)),
                ('fecha_reservada', models.DateField()),
            ],
        ),
    ]
