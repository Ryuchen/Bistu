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

from contrib.academy.models import Academy, Major, Research

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import init data for test'

    def fake_data(self):
        self.stdout.write(self.style.SUCCESS('delete last time fake data in database'))

        Academy.objects.all().delete()
        Major.objects.all().delete()
        Research.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('create this time fake data in database'))

        # 学院和学科专业多对多，学科专业对研究方向多对多
        # 先创建研究方向，然后创建学科专业，然后创建学院
        # 生成100个研究方向，每【5-10】个对应一个学科专业，生成50个学科专业，每【3-6】个对应一个学院，生成20个学院
        research_names = ["研究方向-{0}".format(x) for x in range(1, 100)]
        researches_dict = {}
        major_names = ["学科专业-{0}".format(x) for x in range(1, 50)]
        majors_dict = {}
        academy_names = ["研究生学院-{0}".format(x) for x in range(1, 20)]
        for research_name in research_names:
            research = Research.objects.create(res_name=research_name)
            researches_dict[research_name] = research

        for major_name in major_names:
            random_count = random.randint(5, 10)
            major_code = random.randint(10000, 99999)
            major = Major.objects.create(maj_name=major_name, maj_code=major_code)
            majors_dict[major_name] = major

            for count_code in range(0, random_count):
                research = researches_dict[random.choice(list(researches_dict.keys()))]
                major.research.add(research)

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
