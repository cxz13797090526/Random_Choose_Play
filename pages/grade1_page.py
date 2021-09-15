# -*- coding: UTF-8 -*-
"""
@Project ：Random_Choose_Play 
@File    ：options.py
@Author  ：ChengXiaozhao
@Date    ：
@Desc    ：
"""

"""
参考：https://www.cnblogs.com/xuhongfei/p/14023230.html
"""

from tkinter import *
import webbrowser

from config import ALL_TASKS, grade_1_text, TASK_LINK
from utils import random_choose, get_optional_list


class ChooseMe:
    def __init__(self, window_name):
        self.window_name = window_name
        self.window = Tk()
        self.grade_1_key = None     # 任务字典第一级的key初始化
        self.grade_2_key = None     # 任务字典第二级的key初始化

    def set_window_contains(self):
        """设置窗口内包含的内容"""
        # 第一层级的选项按钮
        self.option_study = Button(self.window, text=grade_1_text["学习"])
        self.option_entertain = Button(self.window, text=grade_1_text["娱乐"])
        self.option_relax = Button(self.window, text=grade_1_text["放松"])

        # 结果展示
        self.result_text = Text(self.window)

        # 结果确认
        self.continue_narrow_range = Button(self.window, text="就这个吧，可以更具体一点吗？")
        self.result_confirm_yes = Button(self.window, text="好哒")
        self.result_confirm_no = Button(self.window, text="拒绝")

    def set_window_layout(self):
        """窗口布局基础设置"""
        self.window.title(self.window_name)
        self.window.geometry("600x480")     # 界面大小

        # 主题设置
        title_label = Label(self.window, text="那就限定个范围吧", font=("宋体", 20), fg="blue")
        title_label.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.1)     # 与全局画布的相对位置和相对大小

        # 选项格式设置
        self.option_study.place(relx=0.35, rely=0.15, relwidth=0.3, relheight=0.1)
        self.option_entertain.place(relx=0.35, rely=0.275, relwidth=0.3, relheight=0.1)
        self.option_relax.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.1)

        # 结果呈现格式设置
        result_label = Label(self.window, text="这个怎么样？", font=("宋体", 20), fg="orange")
        result_label.place(relx=0.35, rely=0.55, relwidth=0.3, relheight=0.1)
        self.result_text.place(relx=0.3, rely=0.65, relwidth=0.4, relheight=0.1)

        # 结果确认的设置
        self.continue_narrow_range.place(relx=0.32, rely=0.75, relwidth=0.36, relheight=0.08)
        self.result_confirm_yes.place(relx=0.37, rely=0.85, relwidth=0.12, relheight=0.08)
        self.result_confirm_no.place(relx=0.51, rely=0.85, relwidth=0.12, relheight=0.08)

    def item_response(self):
        """选项按钮事件响应"""
        self.option_study.bind('<Button-1>', self.event_study)     # 鼠标左键单击触发
        self.option_entertain.bind('<Button-1>', self.event_entertain)
        self.option_relax.bind('<Button-1>', self.event_relax)

        self.continue_narrow_range.bind('<Button-1>', self.event_continue_narrow_range)
        self.result_confirm_yes.bind('<Button-1>', self.event_result_confirm_yes)
        self.result_confirm_no.bind('<Button-1>', self.event_result_confirm_no)

    def event_study(self, event):
        """《学习》按钮触发的事件, event参数看似没有用到，但实际上必不可少，属于事件的标志"""
        self.button_click_process("学习")

    def event_entertain(self, event):
        """《娱乐》按钮触发的事件"""
        self.button_click_process("娱乐")

    def event_relax(self, event):
        """《休息》按钮触发的事件"""
        self.button_click_process("放松")

    def event_continue_narrow_range(self, event):
        """基于已选结果，进一步缩小范围"""
        if self.grade_1_key and self.grade_2_key:
            optional_list = get_optional_list(ALL_TASKS, 2, self.grade_1_key, self.grade_2_key)
            random_choice = random_choose(optional_list)
            self.result_text_process(random_choice)

            if random_choice in list(TASK_LINK.keys()):
                result_link = TASK_LINK[random_choice]
                webbrowser.open(url=result_link, new=1)

    def event_result_confirm_yes(self, event):
        """结果确认可行触发的事件"""
        self.result_text_process("去吧！皮卡丘")

        if self.random_choice in list(TASK_LINK.keys()):
            result_link = TASK_LINK[self.random_choice]
            webbrowser.open(url=result_link, new=1)

    def event_result_confirm_no(self, event):
        """结果确认拒绝触发的事件"""
        self.result_text_process("好吧，换一个")

    def result_text_process(self, insert_text):
        """结果展示框的处理：清理旧内容，按格式插入新文本

        :param insert_text:
        :return:
        """
        self.result_text.delete("1.0", "end")
        self.result_text.tag_config("tag_1", foreground="green", font=("楷体", 28), justify="center")
        self.result_text.insert("insert", insert_text, "tag_1")

    def button_click_process(self, event_key):
        """按钮触发后的处理

        :param event_key:
        :return:
        """
        optional_list = get_optional_list(ALL_TASKS, 1, event_key)     # 获取选择范围内的可选项
        self.random_choice = random_choose(optional_list)     # 从可选项中随机选择一个
        self.result_text_process(self.random_choice)

        # 重置任务字典中的两级key，用于后续获取更具体的任务
        self.grade_1_key = event_key
        self.grade_2_key = self.random_choice
