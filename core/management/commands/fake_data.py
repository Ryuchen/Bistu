#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time : 2019-04-03 22:18 
# @Author : ryuchen
# @Site :  
# @File : fake_data.py 
# @Desc : 
# ==================================================
import random

from contrib.academy.models import Academy, Major

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import init data for test'

    def fake_data(self):
        self.stdout.write(self.style.SUCCESS('delete last time fake data in database'))

        Academy.objects.all().delete()
        Major.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('create this time fake data in database'))

        # 学院和学科专业多对多
        # 先创建学科专业，然后创建学院
        # 生成50个学科专业，每【3-6】个对应一个学院，生成20个学院
        major_names = ["学科专业-{0}".format(x) for x in range(1, 50)]
        majors_dict = {}
        academy_names = ["研究生学院-{0}".format(x) for x in range(1, 20)]

        for major_name in major_names:
            major_code = random.randint(10000, 99999)
            major = Major.objects.create(maj_name=major_name, maj_code=major_code)
            majors_dict[major_name] = major

        for academy_name in academy_names:
            random_count = random.randint(3, 6)
            academy_code = random.randint(100, 999)
            academy = Academy.objects.create(aca_name=academy_name, aca_code=academy_code)

            for count_code in range(0, random_count):
                major = majors_dict[random.choice(list(majors_dict.keys()))]
                academy.major.add(major)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('begin import'))
        self.fake_data()
        self.stdout.write(self.style.SUCCESS('end import'))
