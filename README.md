# GenderGuesser

一个用python写的用于根据中文姓名识别其性别的模块.  
根据PHP版本改写而来。  

原作者：[Wudi博客](http://blog.wudilabs.org/tag/genderguesser/)


## 用法
```python
#! /usr/bin/python3
# -*- coding:utf-8 -*-

from GenderGuesser import genderGuesser

name = '艾佳林'

genderGuesser.load_pkl_file("gender_guesser.pkl") #载入字典

print('%s 为男性的概率%4.2f%%' % (name, genderGuesser.getMaleProbability(name)*100))
```

## 输出
```
艾佳林 为男性的概率64.23%
```

## 原理
1. 收集姓名性别样本
2. 建立模型
3. 查找最优权重参数
4. 完成
详情[查看原作者PDF说明]()