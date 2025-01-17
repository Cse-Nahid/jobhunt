# Generated by Django 5.1.4 on 2025-01-17 12:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('company_name', models.CharField(max_length=30)),
                ('experience', models.CharField(max_length=255)),
                ('employee_type', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('offer_salary', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('responsibilities', models.TextField()),
                ('qualifications', models.TextField()),
                ('skills_experience', models.TextField()),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='jobs.jobcategory')),
            ],
        ),
    ]