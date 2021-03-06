# Generated by Django 2.1.7 on 2019-03-09 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='Street_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='byScrapy',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='way',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip',
            field=models.IntegerField(null=True),
        ),
    ]
