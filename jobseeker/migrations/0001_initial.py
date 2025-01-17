# Generated by Django 5.1 on 2024-09-02 14:08

import django.core.validators
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
            name='Jobseeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fathers_name', models.CharField(max_length=20)),
                ('mothers_name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('contact_no', models.CharField(blank=True, max_length=11)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18)])),
                ('education', models.TextField()),
                ('experience', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='job_seeker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
