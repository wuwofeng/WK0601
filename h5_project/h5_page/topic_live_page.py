#-*- coding:utf-8 -*-

# ========================================================
# Description    : Something
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================


from h5_project.common.page_operation import PageOp
from selenium.webdriver.common.by import By
from time import sleep

# 话题直播页面（话题详情页）
class TopicLivePage(PageOp):

    wechat_page_more_btn_loc = (By.XPATH, '') # 微信页面右上角'...'（更多）按钮位置


    back_live_btn_loc = (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/div/img') # 返回直播间主页入口按钮位置

    question_area_btn_loc = (By.XPATH, '') # '问题区'按钮位置

    #
    # 语音业务
    #
    voice_btn_loc = (By.XPATH, '//*[@id="speakBottom"]/ul/li[1]') # '语音'按钮位置
    start_click_record_btn_loc = (By.XPATH, '//*[@id="btnStartRec"]') # '单击录音'，开始录音按钮位置
    stop_click_record_btn_loc = (By.XPATH, '//*[@id="btnStopRec"]') # '单击录音'，停止录音按钮位置
    send_click_record_btn_loc = (By.XPATH, '//*[@id="btnSentRec"]') # '点击发送'，发送录音按钮位置

    record_cancel_btn_loc = (By.XPATH, '//*[@id="btnCancelRec"]') # '取消'，取消录音按钮位置

    #
    # 文字业务
    #
    word_btn_loc = (By.XPATH, '//*[@id="speakBottom"]/ul/li[2]') # '文字'按钮位置
    word_input_box_loc = (By.XPATH, '/html/body/div[6]/div[1]/textarea') # '文字输入框'位置
    word_send_btn_loc = (By.XPATH, '/html/body/div[6]/div[2]/i[1]') # '发送'按钮位置
    word_send_cancel_btn_loc = (By.XPATH, '/html/body/div[6]/div[2]/i[2]') # '取消'按钮位置

    media_library_btn_loc = (By.XPATH, '') # '媒体库'按钮位置

    material_library_btn_loc = (By.XPATH, '') # '素材库'按钮位置


    def send_voice(self):

        # 点击'语音'按钮，打开录音菜单
        self.loc_element(*self.voice_btn_loc).click()
        # 点击录音按钮
        self.loc_element(*self.start_click_record_btn_loc).click()
        sleep(10) # 录音10seconds
        # 点击停止录音
        self.loc_element(*self.stop_click_record_btn_loc).click()
        # 点击发送录音
        self.loc_element(*self.send_click_record_btn_loc).click()
        # 点击'语音'按钮，关闭录音菜单
        self.loc_element(*self.voice_btn_loc).click()

    def send_word(self):

        # 点击'文字'按钮
        self.loc_element(*self.word_btn_loc).click()
        # 输入'字串'
        self.loc_element(*self.word_input_box_loc).send_keys('Hello, everybody!')
        # 点击'发送'
        self.loc_element(*self.word_send_btn_loc)




