# Generated by Django 4.0.4 on 2022-04-22 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upswebsite', '0002_world_ack_world_id_deliveringtruck_world_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_id', models.IntegerField(default=0)),
                ('world_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='hasresend',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='package',
            name='status',
            field=models.CharField(choices=[('delivering', 'delivering'), ('delivered', 'delivered'), ('loading', 'loading'), ('pick_up', 'pick_up')], default='pick_up', max_length=32),
        ),
        migrations.AlterField(
            model_name='truck',
            name='status',
            field=models.CharField(choices=[('delivering', 'delivering'), ('traveling', 'traveling'), ('idle', 'idle'), ('loading', 'loading'), ('arrive warehouse', 'arrive warehouse')], default='idle', max_length=32),
        ),
    ]
