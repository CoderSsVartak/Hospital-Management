# Generated by Django 2.1 on 2020-05-25 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200525_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='consultant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Doctor'),
        ),
    ]