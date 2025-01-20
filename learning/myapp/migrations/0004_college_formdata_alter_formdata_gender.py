# Generated by Django 5.1.4 on 2025-01-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_formdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='College_Formdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=100)),
                ('college_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='formdata',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Male', max_length=10),
        ),
    ]