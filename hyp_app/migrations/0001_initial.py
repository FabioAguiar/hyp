# Generated by Django 2.1.7 on 2019-03-04 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('broker_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('port', models.IntegerField()),
                ('keep_alive', models.IntegerField()),
                ('user_name', models.CharField(default='', max_length=50)),
                ('passwd', models.CharField(default='', max_length=50)),
                ('is_activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('cycle_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=50)),
                ('is_activated', models.BooleanField(default=False)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('start_cycle', models.DateTimeField(blank=True, null=True)),
                ('end_cycle', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Peripheral',
            fields=[
                ('peripheral_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('technical_name', models.CharField(default='', max_length=50)),
                ('topic_base', models.CharField(default='', max_length=50)),
                ('type_peripheral', models.CharField(default='', max_length=10)),
                ('topic_name', models.CharField(default='', max_length=50)),
                ('specification', models.CharField(default='', max_length=10)),
                ('description', models.TextField(default='')),
                ('mqtt_topic', models.CharField(default='', max_length=50)),
                ('is_activated', models.BooleanField(default=False)),
                ('last_record', models.CharField(default='', max_length=100, null=True)),
                ('last_record_state', models.CharField(default='', max_length=10)),
                ('data_metric', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='cycle',
            name='actuador_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hyp_app.Peripheral'),
        ),
    ]
