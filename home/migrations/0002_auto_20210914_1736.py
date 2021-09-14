# Generated by Django 3.2.7 on 2021-09-14 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('url', models.URLField(max_length=500)),
                ('description', models.TextField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('rank', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('', 'inactive')], max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='slider',
            name='description',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='slider',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('', 'inactive')], max_length=50),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300, unique=True)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True, max_length=300)),
                ('status', models.CharField(blank=True, choices=[('active', 'active'), ('', 'inactive')], max_length=50)),
                ('labels', models.CharField(blank=True, choices=[('hot', 'hot'), ('new', 'new'), ('sale', 'sale'), ('', 'default')], max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subcategory')),
            ],
        ),
    ]
