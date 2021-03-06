# Generated by Django 3.1.1 on 2021-01-09 06:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20210109_0556'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='provider',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='provider',
            name='legacy_arc_score',
            field=models.CharField(choices=[('legacy_arc_full_support', 'Fully accepts legacy ARC number in place of ROC ID'), ('legacy_arc_separate_support', 'Accepts legacy ARC number in a separate UI (passport number, for instance)'), ('legacy_arc_no_support', 'Does not accept legacy ARC numbers')], help_text='How well does this site support legacy ARC numbers?', max_length=50, verbose_name='Legacy ARC Score'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='new_arc_score',
            field=models.CharField(choices=[('new_arc_full_support', 'Fully accepts new ARC number in place of ROC ID'), ('new_arc_separate_support', 'Accepts new ARC number in a separate UI (passport number, for instance)'), ('new_arc_no_support', 'Does not accept new ARC numbers')], help_text='How well does this site support new ARC numbers?', max_length=50, verbose_name='New ARC Score'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='registration_score',
            field=models.CharField(choices=[('registration_online', 'All users may register online using the same process'), ('registration_offline', 'Non-citizens require additional offline registration steps')], help_text='Does this site require extra registration steps for non-citizens?', max_length=50, verbose_name='Registration Score'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='requires_id',
            field=models.BooleanField(default=True, verbose_name='Provider requires ID validation'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='score',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='provider',
            name='service_score',
            field=models.CharField(choices=[('service_full', 'Provides same service to all users'), ('service_partial', 'A portion of features not available to non-citizens'), ('service_none', 'Denies all services to non-citizens')], help_text='Does this site offer the same services to citizens and ARC holders?', max_length=50, verbose_name='Service Score'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='provider',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
    ]
