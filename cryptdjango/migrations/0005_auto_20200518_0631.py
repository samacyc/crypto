# Generated by Django 3.0.6 on 2020-05-18 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cryptdjango', '0004_auto_20200514_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='trader',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='trader',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Profit', 'Profit'), ('Loss', 'Loss')], max_length=200, null=True),
        ),
    ]