# Generated by Django 4.2 on 2024-03-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0006_testquestion_correct_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='testform',
            name='company',
            field=models.CharField(default=11, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testform',
            name='dept',
            field=models.CharField(default=11, max_length=50),
            preserve_default=False,
        ),
    ]
