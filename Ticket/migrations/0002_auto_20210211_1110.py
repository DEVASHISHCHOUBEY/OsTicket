# Generated by Django 3.1.4 on 2021-02-11 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('tpl_id', models.IntegerField()),
                ('sla_id', models.IntegerField()),
                ('schedule_id', models.IntegerField()),
                ('email_id', models.IntegerField()),
                ('autoresp_email_id', models.IntegerField()),
                ('manager_id', models.IntegerField()),
                ('flags', models.IntegerField()),
                ('name', models.IntegerField()),
                ('signature', models.TextField(max_length=65535)),
                ('ispublic', models.SmallIntegerField()),
                ('group_membership', models.SmallIntegerField()),
                ('ticket_auto_response', models.SmallIntegerField()),
                ('message_auto_response', models.SmallIntegerField()),
                ('path', models.CharField(max_length=128)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'ost_department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.IntegerField()),
                ('role_id', models.IntegerField()),
                ('username', models.CharField(max_length=32)),
                ('firstname', models.CharField(max_length=32)),
                ('lastname', models.CharField(max_length=32)),
                ('passwd', models.CharField(max_length=128)),
                ('backend', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=24)),
                ('phone_ext', models.CharField(max_length=6)),
                ('mobile', models.CharField(max_length=24)),
                ('signature', models.TextField(max_length=65535)),
                ('lang', models.CharField(max_length=16)),
                ('timezone', models.CharField(max_length=64)),
                ('locale', models.CharField(max_length=16)),
                ('notes', models.TextField(max_length=65535)),
                ('isactive', models.SmallIntegerField(max_length=1)),
                ('isadmin', models.SmallIntegerField(max_length=1)),
                ('isvisible', models.SmallIntegerField(max_length=1)),
                ('onvacation', models.SmallIntegerField(max_length=1)),
                ('assigned_only', models.SmallIntegerField()),
                ('change_passwd', models.SmallIntegerField()),
                ('max_page_size', models.IntegerField()),
                ('auto_refresh_rate', models.IntegerField()),
                ('extra', models.TextField(max_length=65535)),
                ('permissions', models.TextField(max_length=65535)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lastlogin', models.DateTimeField(auto_now_add=True)),
                ('passwdreset', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'ost_staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ticket_priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority_id', models.SmallIntegerField()),
                ('priority', models.CharField(max_length=60)),
                ('priority_desc', models.CharField(max_length=30)),
                ('priority_color', models.CharField(max_length=7)),
                ('priority_urgency', models.SmallIntegerField()),
                ('ispublic', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'ost_ticket_priority',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='help_topic',
            options={'managed': False},
        ),
    ]
