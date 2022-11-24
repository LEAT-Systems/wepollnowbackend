# Generated by Django 4.1.1 on 2022-11-20 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voters', '0001_initial'),
        ('utilities', '0009_party_logo'),
        ('poll', '0010_merge_20221120_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pollcategory',
            name='poll_description',
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='party_votes', to='utilities.party')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll_votes', to='poll.poll')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voter_votes', to='voters.voter')),
            ],
        ),
    ]