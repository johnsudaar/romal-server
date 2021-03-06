# Generated by Django 2.0.4 on 2018-06-01 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_auto_20180427_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runningchallenges',
            name='challenge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='running', to='challenges.Challenge'),
        ),
        migrations.AlterField(
            model_name='runningchallenges',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sites.Site'),
        ),
    ]
