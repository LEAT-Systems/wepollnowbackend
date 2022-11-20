# Generated by Django 4.1.1 on 2022-11-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0003_candidate_candidate_picture_candidate_main_candidate'),
        ('poll', '0006_poll_poll_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='party',
            field=models.ManyToManyField(related_name='poll_parties', to='utilities.party'),
        ),
    ]