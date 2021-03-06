# Generated by Django 3.0.8 on 2020-08-03 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import realty.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Realty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('street', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('city', models.CharField(max_length=100)),
                ('apartments', models.IntegerField(blank=True, null=True)),
                ('building_number', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realty', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('room_number', models.PositiveIntegerField(blank=True)),
                ('floor', models.PositiveIntegerField(blank=True)),
                ('beds', models.PositiveIntegerField(default=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
                ('realty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='realty.Realty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('image', models.ImageField(upload_to=realty.models.room_image_path)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='realty.Room')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RealtyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('image', models.ImageField(upload_to=realty.models.realty_image_path)),
                ('realty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='realty.Realty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('name_ar', models.CharField(max_length=200, null=True)),
                ('name_en', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_ar', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to=realty.models.category_image_path)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='realty.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
