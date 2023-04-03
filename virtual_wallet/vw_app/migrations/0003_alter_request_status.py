# Generated by Django 4.1 on 2023-04-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vw_app', '0002_alter_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Accepted', 'Accepted'), ('Denied', 'Denied'), ('Pending', 'Pending')], default='Pending', max_length=10),
        ),
    ]
