# Generated by Django 3.2.15 on 2022-09-02 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_order_class_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cleared',
            field=models.BooleanField(default=False),
        ),
    ]
