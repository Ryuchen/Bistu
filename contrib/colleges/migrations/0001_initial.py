# Generated by Django 2.1.7 on 2019-05-04 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='唯一标识ID', primary_key=True, serialize=False, unique=True)),
                ('aca_avatar', models.ImageField(default='default.png', help_text='学院图标', null=True, upload_to='academies')),
                ('aca_nickname', models.CharField(help_text='学院简称', max_length=128, null=True)),
                ('aca_cname', models.CharField(help_text='学院名称(中)', max_length=128, null=True)),
                ('aca_ename', models.CharField(help_text='学院名称(英)', max_length=128, null=True)),
                ('aca_code', models.IntegerField(help_text='学院代码', null=True)),
                ('aca_phone', models.CharField(help_text='学院电话', max_length=128, null=True)),
                ('aca_fax', models.CharField(help_text='学院传真', max_length=128, null=True)),
                ('aca_href', models.URLField(help_text='学院网址', max_length=256, null=True)),
                ('aca_brief', models.TextField(help_text='学院简介')),
                ('aca_user', models.ForeignKey(help_text='学院负责人', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aca_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '学院',
                'verbose_name_plural': '学院',
                'db_table': 'academy',
                'permissions': [('can_insert_academy', '新增学院'), ('can_delete_academy', '删除学院'), ('can_update_academy', '修改学院'), ('can_search_academy', '查询学院')],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='唯一标识ID', primary_key=True, serialize=False, unique=True)),
                ('cla_name', models.CharField(help_text='班级名称', max_length=128, null=True)),
                ('cla_code', models.IntegerField(help_text='班级代码', null=True)),
            ],
            options={
                'verbose_name': '班级',
                'verbose_name_plural': '班级',
                'db_table': 'classes',
                'permissions': [('can_insert_class', '新增班级'), ('can_delete_class', '删除班级'), ('can_update_class', '修改班级'), ('can_search_class', '查询班级')],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='唯一标识ID', primary_key=True, serialize=False, unique=True)),
                ('maj_name', models.CharField(help_text='学科名称', max_length=128, null=True)),
                ('maj_code', models.IntegerField(help_text='学科编号', null=True)),
                ('maj_type', models.CharField(choices=[('C1', '专业硕士学位'), ('C2', '学科硕士学位')], help_text='学科类型', max_length=128)),
                ('maj_first', models.BooleanField(help_text='是否一级学科')),
                ('maj_second', models.BooleanField(help_text='是否二级学科')),
                ('maj_first_uuid', models.UUIDField(help_text='所属一级学科', null=True)),
                ('maj_setup_time', models.DateField(help_text='获批时间')),
                ('maj_degree', models.CharField(choices=[('D1', '哲学'), ('D2', '经济学'), ('D3', '法学'), ('D4', '教育学'), ('D5', '文学'), ('D6', '历史学'), ('D7', '理学'), ('D8', '工学'), ('D9', '农学'), ('D10', '医学'), ('D11', '军事学'), ('D12', '管理学'), ('D13', '艺术学')], help_text='学位类型', max_length=128)),
            ],
            options={
                'verbose_name': '学科专业',
                'verbose_name_plural': '学科专业',
                'db_table': 'major',
                'permissions': [('can_insert_major', '新增学科专业'), ('can_delete_major', '删除学科专业'), ('can_update_major', '修改学科专业'), ('can_search_major', '查询学科专业')],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Reform',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='唯一标识ID', primary_key=True, serialize=False, unique=True)),
                ('time', models.IntegerField(help_text='年份')),
                ('ref_type', models.CharField(choices=[('RT1', '研究生教改项目立项'), ('RT2', '研究生教改论文发表'), ('RT3', '研究生课程教材出版'), ('RT4', '研究生教育相关获奖'), ('RT5', '精品/在线课程建设'), ('RT6', '研究生实践基地建设'), ('RT7', '研究生国际交流项目')], help_text='教改成果类型', max_length=128)),
                ('ref_name', models.TextField(help_text='教改项目名称')),
                ('academy', models.ForeignKey(help_text='学院名称', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='r_academy', to='学院管理.Academy')),
            ],
            options={
                'verbose_name': '教育改革成果',
                'verbose_name_plural': '教育改革成果',
                'db_table': 'reform',
                'permissions': [('can_insert_reform', '新增教改成果'), ('can_delete_reform', '删除教改成果'), ('can_update_reform', '修改教改成果'), ('can_search_reform', '查询教改成果')],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ReformResults',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='唯一标识ID', primary_key=True, serialize=False, unique=True)),
                ('time', models.IntegerField(help_text='年份')),
                ('project_count', models.IntegerField(default=0, help_text='研究生教育相关教改项目立项数量')),
                ('paper_count', models.IntegerField(default=0, help_text='发表研究生教育相关教改论文数量')),
                ('textbook_count', models.IntegerField(default=0, help_text='出版研究生教材数量')),
                ('award_count', models.IntegerField(default=0, help_text='研究生教育相关获奖数量')),
                ('course_count', models.IntegerField(default=0, help_text='精品/在线课程建设数量')),
                ('base_count', models.IntegerField(default=0, help_text='实践基地建设数量')),
                ('exchange_project_count', models.IntegerField(default=0, help_text='研究生国际交流数量')),
                ('academy', models.ForeignKey(help_text='学院名称', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rr_academy', to='学院管理.Academy')),
            ],
            options={
                'verbose_name': '教育改革成果统计',
                'verbose_name_plural': '教育改革成果统计',
                'db_table': 'reform_result',
                'permissions': [('can_insert_reform_result', '新增教改统计'), ('can_delete_reform_result', '删除教改统计'), ('can_update_reform_result', '修改教改统计'), ('can_search_reform_result', '查询教改统计')],
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='唯一标识ID', primary_key=True, serialize=False, unique=True)),
                ('res_name', models.CharField(help_text='研究方向', max_length=128, null=True)),
            ],
            options={
                'verbose_name': '研究方向',
                'verbose_name_plural': '研究方向',
                'db_table': 'research',
                'permissions': [('can_insert_research', '新增研究方向'), ('can_delete_research', '删除研究方向'), ('can_update_research', '修改研究方向'), ('can_search_research', '查询研究方向')],
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='major',
            name='research',
            field=models.ManyToManyField(help_text='科研方向', related_name='research', to='学院管理.Research'),
        ),
        migrations.AddField(
            model_name='class',
            name='major',
            field=models.ForeignKey(help_text='专业名称', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cla_major', to='学院管理.Major'),
        ),
        migrations.AddField(
            model_name='academy',
            name='majors',
            field=models.ManyToManyField(related_name='majors', to='学院管理.Major'),
        ),
    ]
