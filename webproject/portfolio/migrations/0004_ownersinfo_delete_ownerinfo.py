# Generated by Django 5.0.6 on 2024-06-29 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_ownerinfo_alter_contact_name_alter_education_degree_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnersInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('short_intro', models.TextField()),
                ('image', models.ImageField(upload_to='owner_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='OwnerInfo',
        ),
    ]
