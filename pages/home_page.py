# -*- coding: UTF-8 -*-
"""
@Project ：Random_Choose_Play 
@File    ：main.py
@Author  ：ChengXiaozhao
@Date    ：
@Desc    ：首页
"""

"""
参考：https://www.jb51.net/article/133978.htm
"""

from tkinter import *
import webbrowser

from utils import random_choose, get_optional_list
from .grade1_page import ChooseMe
from config import TASK_LINK


class Main:
    def __init__(self, window_name):
        self.window_name = window_name
        self.window = Tk()

    def set_window_contains(self):
        """设置窗口内包含的内容"""
        # 选项按钮
        self.option_random_choose = Button(self.window, text="随机选一个")
        self.option_narrow_range = Button(self.window, text="缩小选择范围")

        # 结果展示框
        self.result_text = Text(self.window)

        # 结果确认按钮
        self.result_confirm_yes = Button(self.window, text="好哒")
        self.result_confirm_no = Button(self.window, text="拒绝")

    def set_window_layout(self):
        """设置窗口布局设置"""
        self.window.title(self.window_name)
        self.window.geometry("600x480")     # 界面大小

        # 主题设置
        title_label = Label(self.window, text="好无聊啊，现在做啥子好呢？", font=("宋体", 20), fg="blue")
        title_label.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.1)     # 与全局画布的相对位置和相对大小

        # 选项格式设置
        self.option_random_choose.place(relx=0.35, rely=0.2, relwidth=0.3, relheight=0.1)
        self.option_narrow_range.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.1)

        # 结果呈现格式设置
        result_label = Label(self.window, text="这个怎么样？", font=("宋体", 20), fg="orange")
        result_label.place(relx=0.35, rely=0.65, relwidth=0.3, relheight=0.1)
        self.result_text.place(relx=0.3, rely=0.75, relwidth=0.4, relheight=0.1)

        # 结果确认的设置
        self.result_confirm_yes.place(relx=0.37, rely=0.85, relwidth=0.12, relheight=0.08)
        self.result_confirm_no.place(relx=0.51, rely=0.85, relwidth=0.12, relheight=0.08)

    def item_response(self):
        """选项按钮事件响应"""
        self.option_random_choose.bind('<Button-1>', self.event_random_choose)     # 鼠标左键单击触发
        self.option_narrow_range.bind('<Button-1>', self.event_narrow_range)

        self.result_confirm_yes.bind('<Button-1>', self.event_result_confirm_yes)
        self.result_confirm_no.bind('<Button-1>', self.event_random_choose)

    def event_random_choose(self, event):
        """随机选一个按钮触发的事件, event参数看似没有用到，但实际上必不可少，属于事件的标志"""
        optional_list = get_optional_list(grade=-1)
        self.random_choice = random_choose(optional_list)
        self.result_text.delete("1.0", "end")     # 清空文本框内原有的内容
        self.result_text.tag_config("tag_1", foreground="green", font=("楷体", 28), justify="center")     # 文本格式设置
        self.result_text.insert("insert", self.random_choice, "tag_1")

    def event_narrow_range(self, event):
        """缩小选择范围按钮触发的事件"""
        self.result_text.delete("1.0", "end")

        self.window.destroy()
        choose_me = ChooseMe("选择困难症拯救者")
        choose_me.set_window_contains()
        choose_me.set_window_layout()
        choose_me.item_response()
        choose_me.window.mainloop()

    def event_result_confirm_yes(self, event):
        """结果确认可行触发的事件"""
        self.result_text.delete("1.0", "end")
        self.result_text.tag_config("tag_1", foreground="green", font=("楷体", 28), justify="center")
        self.result_text.insert("insert", "去吧！皮卡丘", "tag_1")

        if self.random_choice in list(TASK_LINK.keys()):
            result_link = TASK_LINK[self.random_choice]
            webbrowser.open(url=result_link, new=1)


def create_main_window():
    give_you_a_choice = Main("选择困难症拯救者")
    give_you_a_choice.set_window_contains()
    give_you_a_choice.set_window_layout()
    give_you_a_choice.item_response()
    give_you_a_choice.window.mainloop()
