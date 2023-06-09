# Generated by Django 4.1 on 2023-01-06 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('zumba', 'zumba'), ('pilates', 'pilates'), ('musculación', 'musculación')], default='musculación', max_length=11)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('time', models.TimeField()),
                ('picture', models.ImageField(upload_to='image')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.instructor')),
            ],
        ),
    ]
