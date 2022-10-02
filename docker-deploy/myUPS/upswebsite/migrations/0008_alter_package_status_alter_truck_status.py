# Generated by Django 4.0.4 on 2022-04-23 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upswebsite', '0007_alter_package_status_alter_truck_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='status',
            field=models.CharField(choices=[('pick_up', 'pick_up'), ('delivered', 'delivered'), ('delivering', 'delivering'), ('loading', 'loading')], default='pick_up', max_length=32),
        ),
        migrations.AlterField(
            model_name='truck',
            name='status',
            field=models.CharField(choices=[('arrive warehouse', 'arrive warehouse'), ('delivering', 'delivering'), ('idle', 'idle'), ('traveling', 'traveling'), ('loading', 'loading')], default='idle', max_length=32),
        ),
    ]
