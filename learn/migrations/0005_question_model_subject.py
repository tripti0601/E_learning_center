# Generated by Django 3.0.6 on 2020-08-01 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_auto_20200801_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_model',
            name='subject',
            field=models.CharField(default='Mathematics', max_length=50),
            preserve_default=False,
        ),
    ]
