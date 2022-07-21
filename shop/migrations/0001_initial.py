# Generated by Django 4.0.5 on 2022-07-15 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=54, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('image', models.ImageField(upload_to='products', verbose_name='image')),
                ('price', models.FloatField(verbose_name='price')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='discount')),
                ('description', models.TextField(verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.categorymodel', verbose_name='category')),
                ('tag', models.ManyToManyField(related_name='products', to='shop.tagmodel', verbose_name='tag')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]