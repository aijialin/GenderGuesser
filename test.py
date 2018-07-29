#! /usr/bin/python3
# -*- coding:utf-8 -*-

from GenderGuesser import genderGuesser

name = '艾佳林'

genderGuesser.load_pkl_file("gender_guesser.pkl") #载入字典

print('%s 为男性的概率%4.2f%%' % (name, genderGuesser.getMaleProbability(name)*100))