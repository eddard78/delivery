# Generated by Django 3.2.5 on 2021-07-20 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('total_price', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True, verbose_name='Цена')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес доставки')),
                ('status', models.CharField(choices=[('N', 'New courier appointed'), ('T', 'The manager looked at the order and appointed a courier'), ('O', 'On my way'), ('D', 'Delivered'), ('С', 'Сanceled')], max_length=100)),
                ('courier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courier_order', to='users.courier')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_order', to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Количество товара')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prodect_order_product', to='orders.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
            options={
                'verbose_name': 'Заказ продукта',
                'verbose_name_plural': 'Заказ продуктов',
            },
        ),
    ]
