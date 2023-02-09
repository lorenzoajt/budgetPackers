# Generated by Django 4.1.6 on 2023-02-03 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('budget_limit', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type_of_expense', models.CharField(choices=[('GR', 'General'), ('TR', 'Travel'), ('FD', 'Food'), ('AC', 'Accomodation')], default='GR', max_length=2)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.trip')),
            ],
        ),
    ]
