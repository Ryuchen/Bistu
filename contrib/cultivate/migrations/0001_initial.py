# Generated by Django 2.1.7 on 2019-04-13 07:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='唯一标识ID', primary_key=True, serialize=False, unique=True)),
                ('the_title', models.CharField(help_text='课题名称', max_length=128)),
                ('the_start_time', models.DateField(help_text='开题时间')),
                ('the_mid_score', models.CharField(help_text='中期考核结果', max_length=64)),
                ('the_start_score', models.CharField(help_text='开题结果', max_length=64)),
                ('the_check_score', models.CharField(help_text='查重结果', max_length=64)),
                ('the_blind_score1', models.CharField(help_text='盲审结果1', max_length=64)),
                ('the_blind_score2', models.CharField(help_text='盲审结果2', max_length=64)),
                ('the_final_score', models.CharField(help_text='答辩成绩', max_length=64)),
                ('the_is_superb', models.BooleanField(default=False, help_text='是否优秀论文')),
            ],
            options={
                'verbose_name': '论文',
                'verbose_name_plural': '论文',
            },
        ),
    ]
