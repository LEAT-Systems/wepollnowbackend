# Generated by Django 4.1.1 on 2022-11-22 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0009_party_logo'),
        ('voters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='candidate',
        ),
        migrations.AddField(
            model_name='vote',
            name='party',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='utilities.party'),
        ),
    ]
