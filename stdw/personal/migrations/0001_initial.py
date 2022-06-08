# Generated by Django 3.0.6 on 2022-05-17 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('perccod', models.CharField(db_column='PerCCod', max_length=6, primary_key=True, serialize=False)),
                ('pertdescrip', models.CharField(blank=True, db_column='PerTDescrip', max_length=60, null=True)),
                ('pertnombre', models.CharField(blank=True, db_column='PerTNombre', max_length=50, null=True)),
                ('pertapepat', models.CharField(blank=True, db_column='PerTApePat', max_length=50, null=True)),
                ('pertapemat', models.CharField(blank=True, db_column='PerTApemat', max_length=50, null=True)),
                ('pertdireccion', models.CharField(blank=True, db_column='PerTDireccion', max_length=100, null=True)),
                ('pertnumtlf', models.CharField(blank=True, db_column='PerTNumtlf', max_length=10, null=True)),
                ('perttipo', models.CharField(blank=True, db_column='PerTTipo', max_length=1, null=True)),
                ('pertsexo', models.CharField(blank=True, db_column='PerTSexo', max_length=1, null=True)),
                ('pertestaciv', models.CharField(blank=True, db_column='PerTEstaciv', max_length=1, null=True)),
                ('perffechnac', models.DateTimeField(blank=True, db_column='PerFFechnac', null=True)),
                ('perffeching', models.DateTimeField(blank=True, db_column='PerFFeching', null=True)),
                ('perccoddoc', models.CharField(blank=True, db_column='PerCCoddoc', max_length=2, null=True)),
                ('percnumdoc', models.CharField(blank=True, db_column='PerCNumdoc', max_length=20, null=True)),
                ('percnumeruc', models.CharField(blank=True, db_column='PerCNumeruc', max_length=11, null=True)),
                ('perccodiplz', models.CharField(blank=True, db_column='PerCCodiplz', max_length=6, null=True)),
                ('perccodcar', models.CharField(blank=True, db_column='PerCCodcar', max_length=6, null=True)),
                ('perccoduorg', models.CharField(blank=True, db_column='PerCCoduorg', max_length=5, null=True)),
                ('perccodban', models.CharField(blank=True, db_column='PerCCodban', max_length=2, null=True)),
                ('percnumcta', models.CharField(blank=True, db_column='PerCNumcta', max_length=12, null=True)),
                ('pertlugproc', models.CharField(blank=True, db_column='PerTLugProc', max_length=100, null=True)),
                ('pertasig', models.CharField(blank=True, db_column='PerTAsig', max_length=1, null=True)),
                ('perffechreg', models.DateTimeField(blank=True, db_column='PerFFechreg', null=True)),
                ('perffechult', models.DateTimeField(blank=True, db_column='PerFFechult', null=True)),
                ('pertestad', models.CharField(blank=True, db_column='PerTestad', max_length=1, null=True)),
                ('pertflag', models.CharField(blank=True, db_column='PerTflag', max_length=1, null=True)),
                ('pernord', models.SmallIntegerField(blank=True, db_column='PerNOrd', null=True)),
                ('peroper', models.CharField(blank=True, db_column='PerOper', max_length=6, null=True)),
                ('pertcorreo', models.CharField(blank=True, db_column='PerTCorreo', max_length=200, null=True)),
            ],
            options={
                'db_table': 'oeimPersonal',
                'managed': False,
            },
        ),
    ]