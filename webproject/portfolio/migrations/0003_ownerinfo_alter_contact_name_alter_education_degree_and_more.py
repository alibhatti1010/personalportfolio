# Generated by Django 5.0.6 on 2024-06-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_contact_product_delete_contactmessage_delete_project_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('intro', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='education',
            name='institution',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='education',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='company',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='experience',
            name='duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='experience',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
