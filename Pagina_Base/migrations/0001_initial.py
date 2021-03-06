# Generated by Django 3.0.4 on 2020-11-11 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client_DSW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('rut', models.CharField(max_length=150)),
                ('direction', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Machine_DSW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Machine_ID_Code', models.CharField(max_length=100)),
                ('Patent', models.CharField(max_length=100)),
                ('Device_Type', models.CharField(choices=[('I', 'Cargador Frontal'), ('N', 'Retro excavadora'), ('G', 'Bulldozer'), ('E', 'Camión tolva con gato'), ('S', 'Tractor con guinche'), ('C', 'Camión CUNA')], default='C', max_length=2)),
                ('Date_Buy', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status_DSW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status_Machine_Code', models.CharField(max_length=100)),
                ('Date_Last_Maintenance', models.DateTimeField(blank=True, null=True)),
                ('Time_Usage', models.PositiveIntegerField()),
                ('Maintenance_Time_Program', models.DateTimeField(blank=True, null=True)),
                ('Status_Description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Rent_Machine_DSW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_To_Rent', models.DateTimeField(blank=True, null=True)),
                ('Date_To_Return', models.DateTimeField(blank=True, null=True)),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina_Base.Client_DSW')),
                ('Machine_ID_Code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina_Base.Machine_DSW')),
            ],
        ),
        migrations.AddField(
            model_name='machine_dsw',
            name='Status_Device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pagina_Base.Status_DSW'),
        ),
    ]
