# Generated by Django 5.1.2 on 2024-10-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_uz', models.CharField(max_length=100, null=True)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_ru', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=500)),
                ('description_uz', models.CharField(max_length=500, null=True)),
                ('description_en', models.CharField(max_length=500, null=True)),
                ('description_ru', models.CharField(max_length=500, null=True)),
                ('when_created', models.CharField(max_length=36)),
                ('by_who', models.CharField(max_length=36)),
                ('tarif', models.CharField(max_length=36)),
                ('tarif_uz', models.CharField(max_length=36, null=True)),
                ('tarif_en', models.CharField(max_length=36, null=True)),
                ('tarif_ru', models.CharField(max_length=36, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
                ('name_uz', models.CharField(max_length=36, null=True)),
                ('name_en', models.CharField(max_length=36, null=True)),
                ('name_ru', models.CharField(max_length=36, null=True)),
                ('email', models.CharField(max_length=36)),
                ('email_uz', models.CharField(max_length=36, null=True)),
                ('email_en', models.CharField(max_length=36, null=True)),
                ('email_ru', models.CharField(max_length=36, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('year', models.DateField(blank=True, null=True)),
                ('hour', models.TextField(blank=True, null=True)),
                ('text', models.TextField(max_length=100)),
                ('text_uz', models.TextField(max_length=100, null=True)),
                ('text_en', models.TextField(max_length=100, null=True)),
                ('text_ru', models.TextField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpertsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
                ('name_uz', models.CharField(max_length=36, null=True)),
                ('name_en', models.CharField(max_length=36, null=True)),
                ('name_ru', models.CharField(max_length=36, null=True)),
                ('email', models.CharField(max_length=36)),
                ('email_uz', models.CharField(max_length=36, null=True)),
                ('email_en', models.CharField(max_length=36, null=True)),
                ('email_ru', models.CharField(max_length=36, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=36)),
                ('subject_uz', models.CharField(max_length=36, null=True)),
                ('subject_en', models.CharField(max_length=36, null=True)),
                ('subject_ru', models.CharField(max_length=36, null=True)),
                ('text', models.TextField(max_length=100)),
                ('text_uz', models.TextField(max_length=100, null=True)),
                ('text_en', models.TextField(max_length=100, null=True)),
                ('text_ru', models.TextField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
