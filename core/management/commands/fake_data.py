#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-03 22:18 
# @Author : ryuchen
# @Site :  
# @File : fake_data.py 
# @Desc : 
# ==================================================
import os
import time
import random
import string
import datetime

from faker import Faker

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import Group, Permission
from core.definition.mock import *
from contrib.accounts.models import *
from contrib.colleges.models import *
from contrib.education.models import *


class Command(BaseCommand):
    help = 'Import mock data for test'

    @staticmethod
    def create_phone():
        # 第二位数字
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]

        # 第三位数字
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]

        # 最后八位数字
        suffix = random.randint(9999999, 100000000)

        # 拼接手机号
        return "010-{}{}".format(third, suffix)

    @staticmethod
    def create_telephone():
        # 第二位数字
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]

        # 第三位数字
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]

        # 最后八位数字
        suffix = random.randint(9999999, 100000000)

        # 拼接手机号
        return "1{}{}{}".format(second, third, suffix)

    @staticmethod
    def create_card_id():
        # 列表里面的都是一些地区的前六位号码
        first_list = ['362402', '362421', '362422', '362423', '362424', '362425', '362426', '362427', '362428',
                      '362429', '362430', '362432', '110100', '110101', '110102', '110103', '110104', '110105',
                      '110106', '110107', '110108', '110109', '110111']
        first = random.choice(first_list)
        now = time.strftime('%Y')
        second = random.randint(1948, int(now) - 18)
        three = random.randint(1, 12)
        # 月份小于10以下，前面加上0填充
        if three < 10:
            three = '0' + str(three)
        four = random.randint(1, 31)
        # 日期小于10以下，前面加上0填充
        if four < 10:
            four = '0' + str(four)
        five = random.randint(1, 9999)
        if five < 10:
            five = '000' + str(five)
        elif 10 < five < 100:
            five = '00' + str(five)
        elif 100 < five < 1000:
            five = '0' + str(five)

        return str(first) + str(second) + str(three) + str(four) + str(five)

    @staticmethod
    def create_birthday(entrance_year):
        fake = Faker('zh_CN')
        year = fake.random.choice([(entrance_year.year - 18), (entrance_year.year - 19), (entrance_year.year - 20)])
        month = fake.random.choice([i for i in range(1, 13)])
        day = fake.random.choice([i for i in range(1, 29)])
        return entrance_year.replace(year=year, month=month, day=day).strftime("%Y-%m-%d")

    def clear_all_data(self):
        self.stdout.write(self.style.NOTICE('清除测试用的假数据~~~~~~'))
        # 清除用户相关的假数据
        Education.objects.all().delete()
        Tutor.objects.all().delete()
        Student.objects.all().delete()
        MidCheckReport.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Account 相关内容清除完毕！"))
        # 清除学院相关的假数据
        Research.objects.all().delete()
        Major.objects.all().delete()
        Class.objects.all().delete()
        Academy.objects.all().delete()
        Reform.objects.all().delete()
        ReformResults.objects.all().delete()
        # 清除培养相关的假数据
        self.stdout.write(self.style.SUCCESS("College 相关内容清除完毕！"))
        Thesis.objects.all().delete()
        ThesisPlaCheck.objects.all().delete()
        ThesisBlindReview.objects.all().delete()
        ThesisOpenReport.objects.all().delete()
        ThesisQualityReport.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Cultivate 相关内容清除完毕！"))
        # 清除账户相关的假数据
        User.objects.all().delete()
        Group.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("User/Group/Permission 相关内容清除完毕！"))
        self.stdout.write(self.style.NOTICE('清除完毕！'))

    def fake_data(self):
        self.clear_all_data()
        fake = Faker('zh_CN')
        self.stdout.write(self.style.NOTICE('开始生成测试使用的假数据~~~~~~'))
        permissions = Permission.objects.all()

        # 生成超级管理员用户组
        superuser_group = Group.objects.create(name='superuser')
        for permission in permissions:
            superuser_group.permissions.add(permission)
        self.stdout.write(self.style.SUCCESS('生成超级管理员用户组'))
        # 生成超级管理员账户
        admin_username = fake.name()
        superuser = User.objects.create_superuser(
            username='admin',
            password='ant.design',
            first_name=admin_username[:1],
            last_name=admin_username[1:],
            email=fake.email(),
            is_superuser=True
        )
        superuser.groups.add(superuser_group)
        self.stdout.write(self.style.SUCCESS('生成超级管理员'))

        # 生成学院管理员用户组
        college_staff_group = Group.objects.create(name='staff')
        for permission in permissions:
            if any(item in permission.codename for item in ['search', 'delete', 'insert', 'update']):
                college_staff_group.permissions.add(permission)
        self.stdout.write(self.style.SUCCESS('生成学院管理员用户组'))
        # 生成学院管理员账户
        staff_user_list = []
        for _ in range(len(AcademiesList)):
            staff_username = fake.name()
            staff = User.objects.create_user(
                username='staff-{0}'.format(_),
                password='ant.design',
                first_name=staff_username[:1],
                last_name=staff_username[1:],
                email=fake.email(),
                is_staff=True
            )
            staff.groups.add(college_staff_group)
            staff_user_list.append(staff)
        self.stdout.write(self.style.SUCCESS('生成学院管理员'))

        # 生成导师用户组
        teacher_group = Group.objects.create(name='teacher')
        for permission in permissions:
            if any(item in permission.codename for item in ['search', 'insert', 'update']):
                teacher_group.permissions.add(permission)
        self.stdout.write(self.style.SUCCESS('生成导师用户组'))
        # 生成研究生导师账户
        teacher_list = []
        for _ in range(60):
            teacher_username = fake.name()
            teacher = User.objects.create_user(
                username='teacher-{0}'.format(_),
                password='ant.design',
                first_name=teacher_username[:1],
                last_name=teacher_username[1:],
                email=fake.email()
            )
            teacher.groups.add(teacher_group)
            teacher_list.append(teacher)
        self.stdout.write(self.style.SUCCESS('生成导师用户'))

        # 生成研究生学生账户
        student_list = []
        default_password = make_password('123456')
        for _ in range(400):
            student_username = fake.name()
            student = User(
                username='student-{0}'.format(_),
                password=default_password,
                first_name=student_username[:1],
                last_name=student_username[1:],
                email=fake.email(),
                is_active=False
            )
            student_list.append(student)
        User.objects.bulk_create(student_list)
        student_list = list(User.objects.filter(username__contains='student', is_active=False).all())
        self.stdout.write(self.style.SUCCESS('生成学生用户'))

        self.stdout.write(self.style.NOTICE('账户相关数据生成完毕~~~~~~'))

        # 生成学院相关的数据
        research_list = []
        major_list = []
        academy_list = []
        for item in AcademiesList:
            academy = Academy.objects.create(
                aca_nickname=''.join(random.sample(string.ascii_letters + string.digits, 8)),
                aca_cname=item,
                aca_ename=''.join(random.sample(string.ascii_letters + string.digits, 8)),
                aca_code=random.randint(100, 999),
                aca_phone=self.create_phone(),
                aca_fax=self.create_phone(),
                aca_href=fake.url(),
                aca_brief=fake.text(),
                aca_user=staff_user_list.pop(),
            )
            avatar_name = fake.random.choice(Avatars)
            academy.aca_avatar.save(avatar_name, File(
                open(os.path.join(settings.MEDIA_ROOT, "avatar", fake.random.choice(Avatars)), "rb")))

            maj_degree = fake.random.choice([tag.name for tag in MajorDegree])
            for _ in range(random.randint(2, 5)):
                major = Major.objects.create(
                    maj_name=fake.random.choice(AcademyOfDegree),
                    maj_code=random.randint(10000, 99999),
                    maj_type=fake.random.choice([tag.name for tag in MajorType]),
                    maj_first=fake.random.choice([True, False]),
                    maj_second=fake.random.choice([True, False]),
                    maj_setup_time=fake.date(),
                    maj_degree=maj_degree,
                )
                for _ in range(random.randint(1, 3)):
                    research = Research.objects.create(res_name=fake.sentence())
                    research_list.append(research)
                    major.research.add(research)
                academy.majors.add(major)

            maj_degree = fake.random.choice([tag.name for tag in MajorDegree])
            for _ in range(random.randint(1, 3)):
                major = Major.objects.create(
                    maj_name=fake.random.choice(ProfessionalOfDegree),
                    maj_code=random.randint(10000, 99999),
                    maj_type=fake.random.choice([tag.name for tag in MajorType]),
                    maj_first=fake.random.choice([True, False]),
                    maj_second=fake.random.choice([True, False]),
                    maj_setup_time=fake.date(),
                    maj_degree=maj_degree,
                )
                major_list.append(major)
                for _ in range(random.randint(1, 2)):
                    research = Research.objects.create(res_name=fake.sentence())
                    research_list.append(research)
                    major.research.add(research)
                academy.majors.add(major)

            # for _ in range(10):
            #     reforms_data = []
            #     reform_time = datetime.datetime.now().replace(year=(2019 - _)).year
            #     for reform in [tag.name for tag in ReformType]:
            #         counts = random.randint(10, 30)
            #         reforms_data.append(counts)
            #         for count in range(counts):
            #             Reform.objects.create(
            #                 time=reform_time,
            #                 ref_type=reform,
            #                 ref_name=fake.sentence()
            #             )
                # ReformResults.objects.create(
                #     time=reform_time,
                #     project_count=reforms_data[0],
                #     paper_count=reforms_data[1],
                #     textbook_count=reforms_data[2],
                #     award_count=reforms_data[3],
                #     course_count=reforms_data[4],
                #     base_count=reforms_data[5],
                #     exchange_project_count=reforms_data[6],
                #     academy=academy
                # )
            academy.save()
            self.stdout.write(self.style.SUCCESS('生成{}相关数据'.format(item)))
            academy_list.append(academy)
        self.stdout.write(self.style.NOTICE('学院相关数据生成完毕~~~~~~'))

        # 生成用户相关的数据
        tutors_list = []
        teachers_num = len(teacher_list)
        for _ in range(teachers_num):
            education = Education.objects.create(
                edu_begin_time=fake.date_of_birth(minimum_age=32, maximum_age=33),
                edu_finish_time=fake.date_of_birth(minimum_age=27, maximum_age=28),
                edu_school_name=fake.random.choice(SchoolsName),
                edu_study_major=fake.random.choice(major_list),
                edu_study_field=fake.random.choice(research_list)
            )

            teacher = Tutor(
                tut_number=random.randint(197901010000, 201901010000),
                tut_gender=fake.random.choice([tag.name for tag in GenderChoice]),
                tut_title=fake.random.choice([tag.name for tag in TitleChoice]),
                tut_cardID=self.create_card_id(),
                tut_birth_day=fake.date_of_birth(minimum_age=32, maximum_age=65),
                tut_entry_day=fake.date(),
                tut_political=fake.random.choice([tag.name for tag in PoliticalChoice]),
                tut_telephone=self.create_telephone(),
                tut_degree=fake.random.choice([tag.name for tag in DegreeChoice]),
            )
            avatar_name = fake.random.choice(Avatars)
            teacher.tut_avatar.save(avatar_name, File(
                open(os.path.join(settings.MEDIA_ROOT, "avatar", fake.random.choice(Avatars)), "rb")))
            teacher.user = teacher_list.pop()
            teacher.tut_name = teacher.user.first_name + teacher.user.last_name
            teacher.education = education
            teacher.academy = fake.random.choice(academy_list)
            teacher.save()
            tutors_list.append(teacher)
        self.stdout.write(self.style.NOTICE('导师相关数据生成完毕~~~~~~'))

        # 论文相关数据
        _thesis_list = []
        for t_name in range(100):
            the_final_score = fake.random.choice([True, False])
            thesis = Thesis(
                the_title="关于{0}的研究".format(t_name),
                the_start_time="2019-09-01",
                the_final_score=the_final_score,
                the_start_result=fake.random.choice([True, False])
            )
            the_is_delay = fake.random.choice([True, False])
            thesis.the_is_delay = the_is_delay  # 毕设开题是否延期
            if the_is_delay:
                thesis.the_delay_reason = "aaa"
                thesis.the_is_superb = False
            else:
                if the_final_score:
                    thesis.the_is_delay = False
                    thesis.the_is_superb = fake.random.choice([True, False])
            thesis.save()
            _thesis_list.append(thesis)
            # 生成论文查重次数
            for _ in range(random.randint(1, 3)):
                placheck = ThesisPlaCheck.objects.create(
                    pla_date=datetime.datetime.now().replace(month=9, day=1, hour=0, minute=0, second=0, microsecond=0),
                    pla_result=fake.random.choice([True, False]),
                    pla_rate=(fake.random.randint(1, 30) / 100),
                )
                placheck.thesis = thesis

            # 生成论文盲审成绩
            for _ in range(random.randint(1, 3)):
                blindcheck = ThesisBlindReview.objects.create(
                    bli_date=datetime.datetime.now().replace(month=9, day=1, hour=0, minute=0, second=0, microsecond=0),
                    bli_score=fake.random.choice(['合格', '不合格', '再审查']),

                )
                blindcheck.thesis = thesis

        # TODO: rebuild reducer the mock students method
        students_num = len(student_list)
        entrance_time = datetime.datetime.now().replace(month=9, day=1, hour=0, minute=0, second=0, microsecond=0)
        entrance_years = [entrance_time.replace(year=(2019 - i)) for i in range(10)]
        for entrance_year in entrance_years:
            _student_list = []
            student_num = int('{0}0101001'.format(entrance_year.year))
            if (2019 - entrance_year.year) >= 3:
                graduate_year = entrance_year.replace(year=(entrance_year.year + 3))
            else:
                graduate_year = None
            for _ in range(int(students_num / 10)):
                student_num += 1
                student = Student(
                    stu_number=student_num,
                    stu_gender=fake.random.choice([tag.name for tag in GenderChoice]),
                    stu_card_type='身份证',
                    stu_cardID=self.create_card_id(),
                    stu_candidate_number=random.randint(12101000000000, 12201000000000),
                    stu_birth_day=self.create_birthday(entrance_year),
                    stu_nation=fake.random.choice(EthnicChoice),
                    stu_source=fake.random.choice([x[1] for x in ProvinceOfChina]),
                    stu_is_village=fake.random.choice([True, False]),
                    stu_political=fake.random.choice([tag.name for tag in PoliticalChoice]),  # 政治面貌
                    stu_type=fake.random.choice([tag.name for tag in StudentType]),  # 学生类型
                    stu_learn_type=fake.random.choice([tag.name for tag in StudentCategory]),  # 学习类型
                    stu_learn_status=fake.random.choice([tag.name for tag in DegreeChoice]),  # 学习阶段
                    stu_grade=random.randint(1, 3),  # 年级
                    stu_system=3,
                    stu_entrance_time=entrance_year,
                    stu_graduation_time=graduate_year,
                    stu_cultivating_mode=fake.random.choice([tag.name for tag in CultivatingMode]),
                    stu_enrollment_category=fake.random.choice([tag.name for tag in EnrollmentCategory]),
                    stu_nationality='中国',
                    stu_special_program=fake.random.choice([tag.name for tag in SpecialProgramChoice]),
                    stu_is_regular_income=fake.random.choice([True, False]),
                    stu_is_tuition_fees=fake.random.choice([True, False]),
                    stu_is_archives=fake.random.choice([True, False]),
                    stu_is_exemption=fake.random.choice([True, False]),
                    stu_is_adjust=fake.random.choice([True, False]),
                    stu_is_volunteer=fake.random.choice([True, False]),
                    stu_gain_diploma=fake.random.choice([True, False]) if graduate_year else False,
                    stu_gain_cert=fake.random.choice([True, False]) if graduate_year else False,
                    stu_telephone=self.create_telephone(),
                    stu_status=fake.random.choice([tag.name for tag in StatusChoice]),
                    stu_mid_check=fake.random.choice([tag.name for tag in MidCheckChoice]),
                )
                student.user = student_list.pop()
                student.stu_name = student.user.first_name + student.user.last_name
                student.stu_tutor = fake.random.choice(tutors_list)
                # 学生的学院/专业/班级信息
                stu_academy = fake.random.choice(academy_list)
                student.stu_academy = stu_academy   # 学院
                stu_major = fake.random.choice(stu_academy.majors.all())
                student.stu_major = stu_major  # 专业
                student.stu_research = fake.random.choice(stu_major.research.all())

                Class.objects.get_or_create(
                    cla_name=stu_major.maj_name,
                    cla_code='{}0{}'.format(entrance_year.year, fake.random.randint(1, 3)),
                    major=stu_major
                )  # 班级

                student.stu_class = Class.objects.filter(
                    cla_code='{}0{}'.format(entrance_year.year, fake.random.randint(1, 3))).first()

                # 入学在2018年之前的都需要有对应的中期考核成绩
                if entrance_year.year < 2018:

                    # 中期考核确认状态
                    student.stu_is_delay = fake.random.choice([True, False])
                    if student.stu_is_delay:
                        student.stu_delay_reason = fake.sentence()

                    student.stu_mid_check = fake.random.choice([tag.name for tag in MidCheckChoice])  # 中期考核成绩
                    student.stu_is_superb = fake.random.choice([True, False])
                # 论文
                stu_thesis = fake.random.choice(_thesis_list)
                student.stu_thesis = stu_thesis
                _student_list.append(student)
            Student.objects.bulk_create(_student_list)
        self.stdout.write(self.style.NOTICE('学生相关数据生成完毕~~~~~~'))

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('begin import'))
        self.fake_data()
        self.stdout.write(self.style.SUCCESS('end import'))
