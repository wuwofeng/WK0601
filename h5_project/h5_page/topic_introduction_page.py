#-*- coding:utf-8 -*-

# ========================================================
# Description    : 话题介绍页面及页面元素操作
# Author         : Arthur
# Create Date    : 2017-05-10
# ========================================================


from h5_project.common.page_operation import PageOp
from selenium.webdriver.common.by import By


class TopicIntroductionPage(PageOp):

    #
    # 话题介绍页
    #

    push_notification_btn_loc = (By.XPATH, '//*[@id="topic-push"]') # 推送通知按钮位置
    my_invitation_card_btn_loc = (By.XPATH, '//*[@id="get-share-card"]/div[1]') # 我的邀请卡按钮位置
    voice_introduction_btn_loc = (By.XPATH, '//*[@id="intro-main"]/div[1]/div[1]/a') # 语音介绍按钮位置

    topic_name_loc = (By.XPATH, '//*[@id="intro-main"]/div[1]/div[2]/h1') # 话题名称位置
    live_time_loc = (By.XPATH, '//*[@id="intro-main"]/div[1]/div[2]/div/span[1]') # 直播时间位置
    number_of_preview_loc = (By.XPATH, '//*[@id="intro-main"]/div[1]/div[2]/div/span[2]') # 介绍页预览人数位置
    share_list_btn_loc = (By.XPATH, '//*[@id="intro-main"]/div[1]/a/footer/ul') # 进入分享榜按钮位置

    live_introduction_btn_loc = (By.XPATH, '//*[@id="intro-main"]/div[2]/header/h1/i[1]') # 直播简介按钮位置
    course_consult_btn_loc = (By.XPATH, '//*[@id="intro-main"]/div[2]/header/h1/i[2]') # 课程咨询按钮位置

    back_live_btn_loc = (By.XPATH, '//*[@id="intro-main"]/section[1]/div[2]/header/a/span[2]') # 直播间入口按钮位置

    setting_relay_btn_loc = (By.XPATH, '//*[@id="getRelayLink"]/div') # 设置转播按钮位置

    data_statistics_btn_loc = (By.XPATH, '//*[@id="intro-main"]/section[1]/a[2]/div') # 数据统计按钮位置

    more_live_btn_loc = (By.XPATH, '//*[@id="intro-main"]/section[1]/section/a/div') # 更多直播按钮位置

    edit_introduction_page_btn_loc = (By.XPATH, '//*[@id="intro-bottom"]/a[1]') # 编辑介绍页
    join_live_btn_loc = (By.XPATH, '//*[@id="intro-bottom"]/a[2]') #


    #
    # 编辑介绍页
    #

    edit_banner_btn_loc = (By.XPATH, '//*[@id="file"]') # 设置头图按钮位置
    edit_topic_name_btn_loc = (By.XPATH, '//*[@id="edit-pannel"]/div/ul[2]/li/span/a') # 主题名称按钮位置
    edit_speaker_name_btn_lco = (By.XPATH, '//*[@id="edit-pannel"]/div/ul[3]/li[1]/span/a') # 填写主讲人按钮位置
    edit_speaker_introduction_btn_loc =(By.XPATH, '//*[@id="edit-pannel"]/div/ul[3]/li[2]/span/a') # 主讲人介绍按钮位置
    edit_live_general_btn_loc = (By.XPATH, '//*[@id="link-to-image"]') # 直播概要按钮位置

    share_list_switch_btn_loc = (By.XPATH, '//*[@id="share-rank"]/i') # 分享榜开关按钮位置

    show_data_statistics_switch_btn_loc = (By.XPATH, '//*[@id="join-member"]/i') # 显示报名用户统计
    show_intruduction_page_switch_btn_loc = (By.XPATH, '//*[@id="intro-page"]/i') # 介绍页开关按钮位置

    edit_introduction_page_confirm_btn_loc = (By.XPATH, '//*[@id="edit-pannel"]/div/div/a') # 介绍页编辑页面确认按钮位置

    #
    # 编辑弹框
    #
    edit_topic_name_input_box_loc = (By.XPATH, '//*[@id="settings-modal"]/div[1]/div/div[2]/textarea')
    edit_topic_name_confirm_btn_loc = (By.XPATH, '//*[@id="settings-modal"]/div[1]/div/div[3]/span[2]/a')
    edit_topic_name_cancel_btn_loc = (By.XPATH, '//*[@id="settings-modal"]/div[1]/div/div[3]/span[1]/a')

    edit_speaker_name_input_box_loc = (By.XPATH, '//*[@id="settings-modal"]/div[2]/div/div[2]/textarea') # 主讲人名称输入框位置
    edit_speaker_name_confirm_btn_loc = (By.XPATH, '//*[@id="settings-modal"]/div[2]/div/div[3]/span[2]/a') # 填写主讲人弹框确认按钮位置
    edit_speaker_name_cancel_btn_loc = (By.XPATH, '//*[@id="settings-modal"]/div[2]/div/div[3]/span[1]/a') # 填写主讲人弹框取消按钮位置

    edit_speaker_introduction_input_box_loc = (By.XPATH, '//*[@id="settings-modal"]/div[3]/div/div[2]/textarea') # 主持人或嘉宾介绍输入框位置
    edit_speaker_introduction_confirm_btn_loc = (By.XPATH, '//*[@id="settings-modal"]/div[3]/div/div[3]/span[2]/a') # 填写主讲人介绍确认按钮位置
    edit_speaker_introduction_cancel_btn_loc = (By.XPATH, '//*[@id="settings-modal"]/div[3]/div/div[3]/span[1]/a')  # 填写主讲人介绍取消按钮位置



    # 编辑话题介绍
    def edit_topic_introduction(self):

        self.clear_cache()


        # 点击编辑介绍页按钮
        self.loc_element(*self.edit_introduction_page_btn_loc).click()
        # 设置头图
        #self.loc_element(*self.edit_banner_btn_loc).click()
        # 设置主题名称
        #self.loc_element(*self.edit_topic_name_btn_loc).click()
        # 填写主讲人名称
        self.loc_element(*self.edit_speaker_name_btn_lco).click()
        self.loc_element(*self.edit_speaker_name_input_box_loc).send_keys(u'草根大师')
        self.loc_element(*self.edit_speaker_name_confirm_btn_loc).click()

        # 填写主讲人介绍
        self.loc_element(*self.edit_speaker_introduction_btn_loc).click()
        self.loc_element(*self.edit_speaker_introduction_input_box_loc).send_keys(u'即太上老君。他是鸿钧老祖的大弟子，掌管人教。曾三次下山帮助阐教力退截教众仙。也曾一气化三清，战败过通天教主。《西游记》中，他住在离恨天中，是三清教教主之一的太清圣地混元教祖——太上道祖，也称太上老君。玄都大法师是太上老君唯一弟子。')
        self.loc_element(*self.edit_speaker_introduction_confirm_btn_loc).click()
        # 填写直播话题概要

        # 分享榜开关（默认是开）

        # 显示报名用户统计开关（默认是开）

        # 介绍页显示开关（默认是关）

        # 点击确认
        self.loc_element(*self.edit_introduction_page_confirm_btn_loc).click()


    def enter_topic_live(self):

        self.loc_element(*self.join_live_btn_loc).click()
        self.clear_cache()




