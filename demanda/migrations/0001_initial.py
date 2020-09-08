# Generated by Django 3.1.1 on 2020-09-08 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contato', '0002_auto_20200908_0953'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('endereco', '0002_auto_20200908_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demanda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('A', 'Aberto'), ('F', 'Finalizado')], default='A', max_length=1)),
                ('anunciante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='demandas_anunciantes', to=settings.AUTH_USER_MODEL, verbose_name='Anunciante')),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='demanda_contato', to='contato.contato', verbose_name='Contato')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='demanda_endereço', to='endereco.endereco', verbose_name='Endereço')),
            ],
        ),
    ]
