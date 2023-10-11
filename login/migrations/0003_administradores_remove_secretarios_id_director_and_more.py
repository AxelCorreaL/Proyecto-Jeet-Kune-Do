# Generated by Django 4.2.5 on 2023-10-05 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_alumnos_id_alumno_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administradores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('rol', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido_paterno', models.CharField(max_length=200)),
                ('apellido_materno', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='secretarios',
            name='id_Director',
        ),
        migrations.RemoveField(
            model_name='sedes',
            name='id_Guardian',
        ),
        migrations.DeleteModel(
            name='Directores',
        ),
        migrations.DeleteModel(
            name='Guardian',
        ),
        migrations.DeleteModel(
            name='Secretarios',
        ),
        migrations.AddField(
            model_name='sedes',
            name='id_Administrador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.administradores'),
            preserve_default=False,
        ),
    ]
