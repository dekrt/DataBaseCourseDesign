# Generated by Django 2.2.1 on 2019-05-24 12:58

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
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('publish', models.CharField(max_length=50)),
                ('time', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('state', models.SmallIntegerField(default=0)),
                ('description', models.CharField(max_length=100)),
                ('administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_administrator_id', to=settings.AUTH_USER_MODEL)),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_reader_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('state', models.SmallIntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hust_library.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('state', models.SmallIntegerField(default=0)),
                ('administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_administrator_id', to=settings.AUTH_USER_MODEL)),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_reader_id', to=settings.AUTH_USER_MODEL)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hust_library.Store')),
            ],
        ),
        migrations.CreateModel(
            name='Write',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=50)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hust_library.Book')),
            ],
            options={
                'unique_together': {('writer', 'book')},
            },
        ),
    ]