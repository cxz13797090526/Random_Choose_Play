# -*- coding: UTF-8 -*-
"""
@Project ：Random_Choose_Play 
@File    ：utils.py
@Author  ：ChengXiaozhao
@Date    ：2021/7/27 下午8:57 
@Desc    ：
"""
import random

from config import ALL_TASKS


def random_choose(optional_list):
    """随机选择列表中的一个元素

    :param optional_list: 提供的可选项列表
    :return:
    """
    your_choose = random.choice(optional_list)

    return your_choose


def get_optional_list(all_tasks=ALL_TASKS, grade=-1, *keys) -> list:
    """获取可选的任务列表

    :param keys: 缩小范围的关键字，不定长，定位第一级有一个键，要定位到第二级就应该有两个键
    :param all_tasks: dict，两级, 所有的任务
    :param grade: 字典层级 第0层即为最外层，依次向内层嵌套，默认值-1层获取所有最内层的汇总列表
    :return:
    """
    optional_list = []

    # 按照指定层级获取相应的可选任务列表
    if grade == -1:
        # 获取最内层所有的具体任务
        for key_grade_1 in all_tasks.keys():
            for key_grade_2 in all_tasks[key_grade_1].keys():
                optional_list.extend(all_tasks[key_grade_1][key_grade_2])
    elif grade == 0:
        # 获取最外层的宽泛任务
        optional_list.extend(all_tasks.keys())
    elif grade == 1:
        key_grade_1 = keys[0]     # 需取第一层级的值，就必须提供第0层的key
        optional_list.extend(all_tasks[key_grade_1].keys())
    elif grade == 2:
        key_grade_1, key_grade_2 = keys[0], keys[1]     # 需取第二层级的值，就必须提供第0层和第1层的key
        optional_list.extend(all_tasks[key_grade_1][key_grade_2])
    else:
        print("超出任务字典的层级范围了哦")

    return optional_list


if __name__ == '__main__':
    test_optional_list = get_optional_list(ALL_TASKS, -1, "放松", "闭目养神")
    print(test_optional_list)
    my_choose = random_choose(test_optional_list)
    print(my_choose)
