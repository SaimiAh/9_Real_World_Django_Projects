# Generated by Django 4.1.4 on 2023-08-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.everestkitchenpa.com%2Fassets%2Fpages%2FcoldBeverages.html&psig=AOvVaw094-QpBID5Ec0UiP5HLdQ8&ust=1691246636437000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCLjV98mew4ADFQAAAAAdAAAAABAJ', max_length=1000),
        ),
    ]
