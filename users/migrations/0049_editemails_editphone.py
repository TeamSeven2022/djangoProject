# Generated by Django 3.2.9 on 2022-03-10 09:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0048_auto_20220217_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditEmails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(default='', max_length=254, verbose_name='Новая почта')),
                ('v_code', models.CharField(default='', max_length=6, verbose_name='Код подтверждения')),
            ],
            options={
                'verbose_name': 'Email verification',
                'verbose_name_plural': 'Email verification',
            },
        ),
        migrations.CreateModel(
            name='EditPhone',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('id_num', models.CharField(default='', max_length=15, verbose_name='ИИН')),
                ('phone', models.CharField(default='', max_length=12, verbose_name='Новый телефон')),
                ('v_code', models.CharField(default='', max_length=6, verbose_name='Код подтверждения')),
            ],
            options={
                'verbose_name': 'Phone verification',
                'verbose_name_plural': 'Phone verification',
            },
        ),
    ]
