# -*- coding: UTF-8 -*-
"""
@Project ：Random_Choose_Play 
@File    ：config.py
@Author  ：ChengXiaozhao
@Date    ：2021/7/27 下午8:38 
@Desc    ：
"""

ALL_TASKS = {
    "学习": {
        "看书": ["《计算机系统》", "《C++ Primer》", "《机器学习》"],
        "看课程视频": ["李宏毅-强化学习课程", "机器学习课程", "Web前端开发"],
    },
    "娱乐": {
        "逛B站": ["欣赏舞蹈视频", "看音乐视频", "看搞笑视频"],
        "逛知乎": ["知乎推荐页-随机刷", "知乎热榜", "整理知乎收藏夹", "知乎搜索开心内容"],
    },
    "放松": {
        "闭目养神": ["躺着休息", "靠着休息"],
        "远眺": ["轻声哼歌", "发呆瞎想"]
    }
}


TASK_LINK = {
    "看课程视频": "https://www.icourse163.org/",
    "李宏毅-强化学习课程":
        "https://www.bilibili.com/video/BV1UE411G78S?from=search&seid=14424175449318245082&spm_id_from=333.337.0.0",
    "机器学习课程": "https://www.bilibili.com/video/BV18D4y127f1",
    "Web前端开发":
        "https://www.icourse163.org/learn/BFU-1003382003?tid=1461899443#/learn/content?type=detail&id=1238840217&cid"
        "=1259664510 ",

    "逛B站": "https://www.bilibili.com/?spm_id_from=333.788.b_696e7465726e6174696f6e616c486561646572.1",
    "欣赏舞蹈视频": "https://www.bilibili.com/video/BV1Uo4y1k77b",
    "看音乐视频": "https://www.bilibili.com/video/BV1HJ411F7cB",
    "看搞笑视频": "https://www.bilibili.com/video/BV1za411w7ui",

    "逛知乎": "https://www.zhihu.com/hot",
    "知乎推荐页-随机刷": "https://www.zhihu.com/",
    "知乎热榜": "https://www.zhihu.com/hot",
    "整理知乎收藏夹": "https://www.zhihu.com/people/cheng-xiao-zhao-24/collections",
    "知乎搜索开心内容": "https://www.zhihu.com/search?type=content&q=%E6%90%9E%E7%AC%91"
}


# 第一级范围的内容文案
grade_1_text = {"学习": "学习吧，少年", "娱乐": "emmm...玩会儿吧", "放松": "休息一下咯"}
