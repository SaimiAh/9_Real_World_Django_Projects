# Generated by Django 4.1.4 on 2023-08-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.google.com/search?q=placeholder+food+images&hl=en&sxsrf=AB5stBgWTWy287BZrybEHVk0gnFdo2KxGA%3A1691160225330&source=hp&ei=oQ7NZMu7Bf3X5OUP-6Gd8A4&iflsig=AD69kcEAAAAAZM0csTWq8QuOIH_IcPoRu2_VqiAZHxwO&oq=placeholder+food+&gs_lp=Egdnd3Mtd2l6IhFwbGFjZWhvbGRlciBmb29kICoCCAAyBRAAGIAEMgYQABgWGB4yBhAAGBYYHki7NlAAWMYpcAF4AJABAJgB8QOgAfU0qgEGMy0xMy41uAEDyAEA-AEBwgILEAAYgAQYsQMYgwHCAgsQABiKBRixAxiDAcICERAuGIAEGLEDGIMBGMcBGNEDwgILEC4YgAQYsQMYgwHCAggQABiABBixA8ICExAuGIAEGLEDGIMBGMcBGNEDGArCAgoQABgWGB4YDxgK&sclient=gws-wiz#vhid=Ag1_-7HSofts3M&vssid=l', max_length=1000),
        ),
    ]
