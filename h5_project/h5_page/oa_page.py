#-*- coding:utf-8 -*-

# ========================================================
# Description    : Some operation for the oa page
# Author         : Arthur
# Create Date    : 2015-10-10
# ========================================================

from selenium.webdriver.common.by import By

from h5_project.common.page_operation import PageOp

# 公众号页面
class OaPage(PageOp):

    # 菜单栏按钮
    mine_btn_loc = (By.NAME, u'我的') # '我的'按钮位置
    live_btn_loc = (By.NAME, u'正在直播') # '正在直播'按钮位置
    week_hot_btn_loc = (By.NAME, u'本周最热') # '本周最热'按钮位置

    # '我的'子菜单
    learn_week_loc = (By.NAME, u'知识变现学习周') # '知识变现学习周'按钮位置
    my_live_room_loc = (By.NAME, u'我的直播间') # '我的直播间'按钮位置


    # '本周最热'子菜单
    free_zone_loc = (By.NAME, u'免费专区') # '免费专区'按钮位置

    ############################
    # 进入'我的直播间'
    ############################
    def enter_my_live_room(self):
        self.loc_element(*self.mine_btn_loc).click() # 点'我的'
        self.loc_element(*self.my_live_room_loc).click() # 点'我的直播间'


# 直播间页面
class LiveRoomPage(OaPage):

    # 创建直播间页面
    new_live_room_btn_loc = (By.XPATH, r'//*[@id="backPageBox"]/a') # '一键创建直播间'按钮位置

    # 直播间认证页面
    phone_num = '18024047279'
    wechat_num = 'mo_cha1973'
    sort_num = 1
    live_room_roles = ['speecher', 'institute', 'audience']
    phone_num_input_box_loc = (By.ID, 'phone') # '手机号'输入框位置
    get_code_btn_loc = (By.XPATH, r'//*[@id="get-code"]') # '获取验证码'按钮位置
    code_input_box_loc = (By.XPATH, r'//*[@id="code"]') # '验证码'输入框位置
    wechat_num_input_loc = (By.XPATH, r'//*[@id="wechat"]') # '微信号'输入框位置
    live_room_roles_loc = (By.XPATH, r'//*[@id="speecher"]') # 可选的'3个直播间身份'按钮位置
    select_live_room_sort_loc = (By.XPATH, r'//*[@id="tag-select"]') # '选择直播间分类'按钮位置
    live_room_sorts_loc = (By.XPATH, r'// *[@id="container"]/div/main/ul/li[2]') # 可选的'直播间分类'按钮位置
    live_romm_sort_confirm_btn_loc = (By.XPATH, r'//*[@id="tag-confirm"]') # 选择直播间分类弹窗上的'确认'按钮位置

    commit_btn_loc = (By.XPATH, r'//*[@id="info-confirm"]')


    ############################
    # 创建直播间
    ############################
    def new_live_room(self):

        self.switch_to_h5() # 切换到h5
        self.loc_element(*self.new_live_room_btn_loc).click() # 点'一键创建直播间'
        self.clear_cache()

        # 直播认证页面操作
        # 手机号
        self.loc_element(*self.phone_num_input_box_loc).send_keys(self.phone_num) # 输入手机号码
        self.loc_element(*self.get_code_btn_loc).click() # 点'获取验证码'

        # 验证码
        code = raw_input(u'请输入验证码 > ') # 手动输入验证码
        self.loc_element(*self.code_input_box_loc).send_keys(code) # 填入验证码

        # 微信号
        self.loc_element(*self.wechat_num_input_loc).send_keys(self.wechat_num) # 输入微信号

        # 选择您的身份
        self.loc_element(*self.live_room_roles_loc).click() # 选择直播间身份

        # 选择直播间分类（弹窗）
        self.loc_element(*self.select_live_room_sort_loc).click() # 点'选择直播间分类'，会弹出选择分类弹窗
        self.loc_element(*self.live_room_sorts_loc).click() # 选第一个分类
        self.loc_element(*self.live_romm_sort_confirm_btn_loc).click() # 点选择直播间分类弹窗上的'确认'按钮

        # 提交
        self.loc_element(*self.commit_btn_loc).click() # 点直播间认证页面底部的'提交'按钮



