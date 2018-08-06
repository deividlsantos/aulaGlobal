# Generated by Django 2.1 on 2018-08-04 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('products_type', models.CharField(choices=[('drinks', 'Bebida'), ('food', 'Comida'), ('candy', 'Doce')], default='food', max_length=10, verbose_name='Tipo do Produto')),
                ('category', models.ForeignKey(null=True, on_delete=False, to='products.CategoryProduct')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=False, to='providers.Provider')),
            ],
            options={
                'verbose_name': 'Produto',
            },
        ),
    ]
