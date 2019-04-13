#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-03 22:18 
# @Author : ryuchen
# @Site :  
# @File : fake_data.py 
# @Desc : 
# ==================================================
import time
import random
import string

from faker import Faker

from django.core.management.base import BaseCommand
from contrib.users.models import *
from contrib.academy.models import *

EthnicChoice = [
    '汉族',
    '壮族',
    '满族',
    '回族',
    '苗族',
    '维吾尔族',
    '土家族',
    '彝族',
    '蒙古族',
    '藏族',
    '布依族',
    '侗族',
    '瑶族',
    '朝鲜族',
    '白族',
    '哈尼族',
    '哈萨克族',
    '黎族',
    '傣族',
    '畲族',
    '傈僳族',
    '仡佬族',
    '东乡族',
    '高山族',
    '拉祜族',
    '水族',
    '佤族',
    '纳西族',
    '羌族',
    '土族',
    '仫佬族',
    '锡伯族',
    '柯尔克孜族',
    '达斡尔族',
    '景颇族',
    '毛南族',
    '撒拉族',
    '布朗族',
    '塔吉克族',
    '阿昌族',
    '普米族',
    '鄂温克族',
    '乌孜别克族',
    '门巴族',
    '鄂伦春族',
    '独龙族',
    '塔塔尔族',
    '赫哲族',
    '珞巴族',
]
SchoolsName = [
    '北京科技大学天津学院',
    '天津大学仁爱学院',
    '天津财经大学珠江学院',
    '天津市职业大学',
    '天津滨海职业学院',
    '天津工程职业技术学院',
    '天津青年职业学院',
    '天津渤海职业技术学院',
    '天津电子信息职业技术学院',
    '天津机电职业技术学院',
    '天津现代职业技术学院',
    '天津公安警官职业学院',
    '天津轻工职业技术学院',
    '天津商务职业学院',
    '天津国土资源和房屋职业学院',
    '天津医学高等专科学校',
    '天津开发区职业技术学院',
    '天津艺术职业学院',
    '天津交通职业学院',
    '天津冶金职业技术学院',
    '天津石油职业技术学院',
    '天津城市职业学院',
    '天津铁道职业技术学院',
    '天津工艺美术职业学院',
    '天津城市建设管理职业技术学院',
    '天津生物工程职业技术学院',
    '天津海运职业学院',
    '天津广播影视职业学院',
]
AcademiesList = [
    '计算机学院',
    '机电学院',
    '光电学院',
    '自动化学院',
    '通信学院',
    '经济管理学院',
    '信息管理学院',
    '马克思主义学院',
    '公共管理与传媒学院',
    '外国语学院',
    '理学院',
    '国际交流学院',
]
AcademyOfDegree = [
    '现代设计理论与方法学科方向',
    '汽车系统动力学与控制学科方向',
    '机器人技术学科方向',
    '智能制造学科方向',
    '机电系统测控与信息化学科方向',
    '精密仪器及机械学科方向',
    '测试计量技术及仪器学科方向',
    '光学工程学科方向',
    '控制科学与工程',
    '信息与通信工程',
    '信号与信息处理',
    '通信与信息系统',
    '智慧感知与信息处理',
]
ProfessionalOfDegree = [
    '车辆工程领域',
    '机械工程领域',
    '仪器仪表工程领域',
    '控制工程',
    '电子与通信工程',
]
Avatars = [
    'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png',
    'https://gw.alipayobjects.com/zos/rmsportal/cnrhVkzwxjPwAaCfPbdc.png',
    'https://gw.alipayobjects.com/zos/rmsportal/gaOngJwsRYRaVAuXXcmB.png',
    'https://gw.alipayobjects.com/zos/rmsportal/ubnKSIfAJTxIgXOKlciN.png',
    'https://gw.alipayobjects.com/zos/rmsportal/WhxKECPNujWoWEFNdnJE.png',
    'https://gw.alipayobjects.com/zos/rmsportal/jZUIxmJycoymBprLOUbT.png',
    'https://gw.alipayobjects.com/zos/rmsportal/psOgztMplJMGpVEqfcgF.png',
    'https://gw.alipayobjects.com/zos/rmsportal/ZpBqSxLxVEXfcUNoPKrz.png',
    'https://gw.alipayobjects.com/zos/rmsportal/laiEnJdGHVOhJrUShBaJ.png',
    'https://gw.alipayobjects.com/zos/rmsportal/UrQsqscbKEpNuJcvBZBu.png',
]
ProvinceOfChina = [
    (1, '北京市'),
    (2, '上海市'),
    (3, '香港'),
    (4, '台湾'),
    (5, '重庆市'),
    (6, '澳门'),
    (7, '天津市'),
    (8, '江苏省'),
    (9, '浙江省'),
    (10, '四川省'),
    (11, '江西省'),
    (12, '福建省'),
    (13, '青海省'),
    (14, '吉林省'),
    (15, '贵州省'),
    (16, '陕西省'),
    (17, '山西省'),
    (18, '河北省'),
    (19, '湖北省'),
    (20, '辽宁省'),
    (21, '湖南省'),
    (22, '山东省'),
    (23, '云南省'),
    (24, '河南省'),
    (25, '广东省'),
    (26, '安徽省'),
    (27, '甘肃省'),
    (28, '海南省'),
    (29, '黑龙江省'),
    (30, '内蒙古自治区'),
    (31, '新疆维吾尔自治区'),
    (32, '广西壮族自治区'),
    (33, '宁夏回族自治区'),
    (34, '西藏自治区')
]


class Command(BaseCommand):
    help = 'Import init data for test'

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

        return str(first)+str(second)+str(three)+str(four)+str(five)

    def fake_data(self):
        fake = Faker('zh_CN')
        self.stdout.write(self.style.SUCCESS('清除测试用的假数据~~~~~~'))
        # 清除学院相关的假数据
        Academy.objects.all().delete()
        Major.objects.all().delete()
        Research.objects.all().delete()
        # 清除教师职工相关的假数据
        Tutor.objects.all().delete()
        Student.objects.all().delete()
        Class.objects.all().delete()
        Education.objects.all().delete()
        # 清除账户相关的假数据
        User.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('清除完毕！'))

        self.stdout.write(self.style.SUCCESS('开始生成测试使用的假数据~~~~~~'))
        # 生成超级管理员账户
        admin_username = fake.name()
        User.objects.create_superuser(
            username='admin',
            password='ant.design',
            first_name=admin_username[:1],
            last_name=admin_username[1:],
            email=fake.email(),
            is_superuser=True
        )
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
            staff_user_list.append(staff)
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
            teacher_list.append(teacher)
        # 生成研究生学生账户
        student_list = []
        for _ in range(1000):
            student_username = fake.name()
            student = User.objects.create_user(
                username='student-{0}'.format(_),
                password='123456',
                first_name=student_username[:1],
                last_name=student_username[1:],
                email=fake.email(),
                is_active=False
            )
            student_list.append(student)
        self.stdout.write(self.style.SUCCESS('账户相关数据生成完毕~~~~~~'))

        # 生成学院相关的数据
        academy_list = []
        major_list = []
        research_list = []
        for _ in AcademiesList:
            academy = Academy.objects.create(
                aca_avatar=fake.random.choice(Avatars),
                aca_nickname=''.join(random.sample(string.ascii_letters + string.digits, 8)),
                aca_cname=_,
                aca_ename=''.join(random.sample(string.ascii_letters + string.digits, 8)),
                aca_code=random.randint(100, 999),
                aca_phone=self.create_phone(),
                aca_fax=self.create_phone(),
                aca_href=fake.url(),
                aca_brief=fake.text(),
                aca_user=staff_user_list.pop(),
            )
            academy_list.append(academy)
            print(MajorDegree)
            maj_degree = fake.random.choice([tag.name for tag in MajorDegree])
            for _ in range(random.randint(3, 7)):
                major = Major.objects.create(
                    maj_name=fake.random.choice(AcademyOfDegree),
                    maj_code=random.randint(10000, 99999),
                    maj_type=fake.random.choice([tag.name for tag in MajorType]),
                    maj_first=fake.random.choice([True, False]),
                    maj_second=fake.random.choice([True, False]),
                    maj_setup_time=fake.date(),
                    maj_degree=maj_degree,
                )
                major_list.append(major)
                for _ in range(random.randint(3, 5)):
                    research = Research.objects.create(res_name=fake.sentence())
                    research_list.append(research)
                    major.research.add(research)
                academy.majors.add(major)
            maj_degree = fake.random.choice([tag.name for tag in MajorDegree])
            for _ in range(random.randint(3, 5)):
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
                for _ in range(random.randint(3, 5)):
                    research = Research.objects.create(res_name=fake.sentence())
                    research_list.append(research)
                    major.research.add(research)
                academy.majors.add(major)
        self.stdout.write(self.style.SUCCESS('学院相关数据生成完毕~~~~~~'))

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
            teacher.user = teacher_list.pop()
            teacher.education = education
            teacher.academy = fake.random.choice(academy_list)
            teacher.save()
            tutors_list.append(teacher)

        students_num = len(student_list)
        student_num = random.randint(20160101001, 20190101001)
        for _ in range(students_num):
            student_num += 1
            student = Student(
                stu_number=student_num,
                stu_name=fake.name(),
                stu_avatar=fake.random.choice(Avatars),
                stu_gender=fake.random.choice([tag.name for tag in GenderChoice]),
                stu_card_type='身份证',
                stu_cardID=self.create_card_id(),
                stu_candidate_number=random.randint(12101000000000, 12201000000000),
                stu_birth_day=fake.date_of_birth(minimum_age=19, maximum_age=22),
                stu_nation=fake.random.choice(EthnicChoice),
                stu_source=fake.random.choice([x[1] for x in ProvinceOfChina]),
                stu_is_village=fake.random.choice([True, False]),
                stu_political=fake.random.choice([tag.name for tag in PoliticalChoice]),
                stu_type=fake.random.choice([tag.name for tag in StudentType]),
                stu_learn_type=fake.random.choice([tag.name for tag in StudentCategory]),
                stu_learn_status=fake.random.choice([tag.name for tag in DegreeChoice]),
                stu_grade=random.randint(1, 3),
                stu_system=3,
                stu_entrance_time=fake.date(),
                stu_graduation_time=fake.date(),
                stu_cultivating_mode=fake.random.choice([tag.name for tag in CultivatingMode]),
                stu_enrollment_category=fake.random.choice([tag.name for tag in EnrollmentCategory]),
                stu_nationality='中国',
                stu_special_program=fake.random.choice([tag.name for tag in SpecialProgram]),
                stu_is_regular_income=fake.random.choice([True, False]),
                stu_is_tuition_fees=fake.random.choice([True, False]),
                stu_is_archives=fake.random.choice([True, False]),
                stu_is_superb=fake.random.choice([True, False]),
                stu_telephone=self.create_telephone(),
                stu_status=fake.random.choice([tag.name for tag in StatusChoice]),
                stu_class='信管1201',
                exemption=fake.random.choice([True, False]),
                adjust=fake.random.choice([True, False]),
                volunteer=fake.random.choice([True, False]),
            )
            student.user = student_list.pop()
            student.tutor = fake.random.choice(tutors_list)
            student.academy = fake.random.choice(academy_list)
            student.major = fake.random.choice(major_list)
            student.research = fake.random.choice(research_list)
            student.save()
        self.stdout.write(self.style.SUCCESS('用户相关数据生成完毕~~~~~~'))

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('begin import'))
        self.fake_data()
        self.stdout.write(self.style.SUCCESS('end import'))
