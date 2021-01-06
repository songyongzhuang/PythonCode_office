# --*-- coding : utf-8 --*--
# Project      : Python_ketangpai
# Current file : job_datas.py
# Author       : 大壮
# Create time  : 2020-12-26 18:36
# IDE          : PyCharm
# TODO 成长很苦，进步很甜，加油！
"""
存放 传作业、作业留言、查看作业提交状态 需要用的数据
"""
import os
from common2.dir_path import DirPath


class JobDatas:
    # 作业留言
    job_leave_word_data = '支持各类文档、图片、代码、压缩包格式'
    # 上传文件
    uploading_file_data = os.path.join(DirPath.base_dir, 'main.py')
    # 第一个断言 更新提交 文字
    hint_data = '更新提交'
    # 断言 查看作业提交状态
    submit_state_data = '已提交'
