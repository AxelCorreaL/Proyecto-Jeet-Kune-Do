# Generated by Django 4.2.7 on 2023-11-20 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_alter_userprofile_apellido_materno_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dias_Semana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.PositiveSmallIntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sábado'), (7, 'Domingo')])),
            ],
        ),
        migrations.CreateModel(
            name='GruposDias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.dias_semana')),
            ],
        ),
        migrations.RenameField(
            model_name='grupos',
            old_name='id_Sede',
            new_name='sede',
        ),
        migrations.RenameField(
            model_name='inscripciones',
            old_name='id_Grupo',
            new_name='grupo',
        ),
        migrations.RemoveField(
            model_name='grupos',
            name='id_Instructor',
        ),
        migrations.RemoveField(
            model_name='inscripciones',
            name='id_Alumno',
        ),
        migrations.AddField(
            model_name='grupos',
            name='grupo',
            field=models.CharField(default='000', max_length=6),
        ),
        migrations.AddField(
            model_name='grupos',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.userprofile'),
        ),
        migrations.AddField(
            model_name='inscripciones',
            name='alumno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.userprofile'),
        ),
        migrations.AddField(
            model_name='sedes',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.userprofile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='grupos',
            name='curso',
            field=models.CharField(choices=[('jiu jitsu', 'Jiu Jitsu'), ('karete do', 'Karate Do'), ('taido', 'Taido'), ('taekwondo', 'Taekwondo'), ('capoeira', 'Capoeira'), ('kickboxing', 'Kickboxing'), ('tai chi', 'Tai Chi')], default='Jiu Jitsu', max_length=200),
        ),
        migrations.RemoveField(
            model_name='grupos',
            name='dias_semana',
        ),
        migrations.AlterField(
            model_name='grupos',
            name='duracion',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='grupos',
            name='hora_inicio',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='rol',
            field=models.CharField(choices=[('guardian', 'Guardian'), ('director', 'Director'), ('secretario', 'Secretario'), ('instructor', 'Instructor'), ('alumno', 'Alumno')], default='director', max_length=25),
        ),
        migrations.DeleteModel(
            name='Alumnos',
        ),
        migrations.DeleteModel(
            name='Instructores',
        ),
        migrations.AddField(
            model_name='gruposdias',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.grupos'),
        ),
        migrations.AddField(
            model_name='grupos',
            name='dias_semana',
            field=models.ManyToManyField(through='login.GruposDias', to='login.dias_semana'),
        ),
    ]
