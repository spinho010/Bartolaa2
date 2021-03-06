# Generated by Django 2.2.24 on 2021-12-16 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_attconcluida_attpendete_metodopag_notafiscal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conclu_Serviço',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviço_concluido', models.CharField(blank=True, max_length=60, verbose_name='Serviço Concluido?: ')),
                ('descric', models.CharField(blank=True, max_length=60, verbose_name='Descrição:')),
            ],
        ),
        migrations.AlterField(
            model_name='notafiscal',
            name='metodo_pago',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.MetodoPag'),
        ),
        migrations.AddField(
            model_name='attpendete',
            name='finalizado',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Conclu_Serviço'),
        ),
    ]
