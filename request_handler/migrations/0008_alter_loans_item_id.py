# Generated by Django 4.2.8 on 2023-12-17 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request_handler', '0007_rename_item_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='request_handler.items'),
        ),
    ]
