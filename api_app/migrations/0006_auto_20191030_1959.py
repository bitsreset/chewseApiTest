# Generated by Django 2.2.6 on 2019-10-30 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0005_order_portions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='PortionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratio', models.PositiveIntegerField(default=None, null=True)),
                ('allocated_portions', models.PositiveIntegerField(default=None, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PortionDetails_itemName', to='api_app.Item', to_field='name')),
                ('itemID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PortionDetails_itemid', to='api_app.Item')),
                ('orderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PortionDetails_orderID', to='api_app.Order')),
            ],
        ),
    ]
