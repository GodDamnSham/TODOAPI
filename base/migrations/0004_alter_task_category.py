# Generated by Django 4.0.6 on 2022-08-10 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_categories_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('Arbeit', 'Arbeit'), ('Studium', 'Studium'), ('Freizeit', 'Freizeit'), ('Haushalt', 'Haushalt'), ('others', 'others'), ('none', 'none')], default='Arbeit', max_length=8),
        ),
    ]
