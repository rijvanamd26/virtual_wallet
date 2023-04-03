# Generated by Django 4.1 on 2023-04-03 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sender_charges', models.FloatField(default=0.0)),
                ('receiver_charges', models.FloatField(default=0.0)),
                ('sender_wallet', models.FloatField(default=0.0)),
                ('receiver_wallet', models.FloatField(default=0.0)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Denied', 'Denied')], default='Pending', max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('req_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='req_by', to=settings.AUTH_USER_MODEL)),
                ('req_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='req_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]