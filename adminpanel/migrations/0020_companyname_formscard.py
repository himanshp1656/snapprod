# Generated by Django 4.2 on 2024-03-18 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0019_alert_submitted_date_auditform_submitted_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='companyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='formsCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=50)),
                ('form_link', models.CharField(max_length=50)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminpanel.companyname')),
            ],
        ),
    ]