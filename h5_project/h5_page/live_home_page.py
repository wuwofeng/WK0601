#-*- coding:utf-8 -*-

# ========================================================
# Description    : 直播间主页
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================


from h5_project.common.page_operation import PageOp
from selenium.webdriver.common.by import By


class LiveHomePage(PageOp):
    '''xxx'''

    # 已开启通知
    # 新建话题
    # 新建系列课

    # 话题分页列表
    switch_topic_list_btn_loc = (By.XPATH, '//*[@id="QLLiveRoom"]/div[2]/ul[2]/li[1]/span') # 话题分页按钮
    ## 话题省略图
    ## 话题免费标签

    ## 话题名称
    ## 话题状态
    ## 话题开播时间
    ## 话题预览人数
    ## 操作菜单
    ## ？


    # 系列课分页列表
    switch_channel_list_btn_loc = (By.XPATH, '//*[@id="QLLiveRoom"]/div[2]/ul[2]/li[2]/span') # 系列课分页按钮
    # 介绍分页

    # 直播间主页导航栏