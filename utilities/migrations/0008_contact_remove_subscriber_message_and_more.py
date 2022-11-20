# Generated by Django 4.1.1 on 2022-11-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0007_alter_candidate_party_alter_candidate_senatorial_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='message',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='name',
        ),
    ]
