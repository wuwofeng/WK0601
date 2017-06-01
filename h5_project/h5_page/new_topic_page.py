#-*- coding:utf-8 -*-

# ========================================================
# Description    : Something
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================

from h5_project.common.page_operation import PageOp
from selenium.webdriver.common.by import By
from h5_project.h5_page.background_page import BackgroundPage

# 新建话题页面
class NewTopicPage(PageOp):



        # 基本信息页面 - 主题/时间/形式
        def fill_topic_info(self):


            topic_name_input_box_loc = (By.XPATH, r'// *[ @ id = "topic-title-edit"]')  # '直播主题输入框'位置
            start_time_select_btn_loc = (By.XPATH, r'/html/body/div[1]/div[1]/ul[1]/li[2]/span')  # '开始时间'选择按钮位置

            time_confirm_btn_loc = (By.XPATH, r'/html/body/div[7]/div/div[2]/div/div[4]/div[2]/div')  # 时间'确定'按钮位置
            # /html/body/div[7]/div/div[2]/div/div[4]/div[2]/div

            time_cancel_btn_loc = (By.XPATH, r'/html/body/div[7]/div/div[2]/div/div[4]/div[1]/div')  # 时间'取消'按钮位置

            topic_form_select_btn_loc = (By.XPATH, r'// *[ @ id = "live-type-list"] / li[1]')  # 1：讲座形式 2：幻灯片形式

            topic_info_next_btn_loc = (By.XPATH, r'/html/body/div[1]/div[1]/div/a')  # 直播信息页面'下一步'按钮位置

            new = BackgroundPage(self.driver)
            new.enter_new_topic_page()

            self.loc_element(*topic_name_input_box_loc).send_keys(u'自动化测试') # 输入直播主题
            self.loc_element(*start_time_select_btn_loc).click() # 点击'开始时间'按钮
            self.loc_element(*time_confirm_btn_loc).click() # 点击 时间'确定'按钮
            self.loc_element(*topic_form_select_btn_loc).click() # 点击'讲座形式'按钮
            self.loc_element(*topic_info_next_btn_loc).click() # 点击'下一步'按钮


        # 基本信息页面 - 选择直播类型
        def finish_new_topic(self):


            free_topic_btn_loc = (By.XPATH, r'/html/body/div[1]/div[2]/dl/dt/span[1]') # '公开直播'按钮位置
            encrypt_topic_btn_loc = (By.XPATH, r'/html/body/div[1]/div[2]/dl/dt/span[2]') # '加密直播'按钮位置
            charge_topic_btn_loc = (By.XPATH, r'/html/body/div[1]/div[2]/dl/dt/span[3]') # '收费直播'按钮位置

            topic_present_page_switch_btn_loc = (By.XPATH, r'/html/body/div[1]/div[2]/dl/dd/div[1]/div[2]/span[1]/span') # '介绍页开关'位置

            encrypt_input_box_loc = (By.XPATH, r'/html/body/div[1]/div[2]/dl/dd/div[2]/div/input') # 加密直播'密码输入框'位置

            charge_input_box_loc = (By.XPATH, r'/html/body/div[1]/div[2]/dl/dd/div[3]/div/span[2]/input') # 收费直播'票价输入框'位置

            new_topic_finish_btn_loc = (By.XPATH, r'/html/body/div[1]/div[2]/div/a[2]') # 新建话题'完成'按钮位置

            new_topic_previous_btn_loc = (By.XPATH, r'/html/body/div[1]/div[2]/div/a[1]') # 新建话题'上一步'按钮位置


            self.loc_element(*free_topic_btn_loc).click() # 点击'公开直播'按钮
            self.loc_element(*topic_present_page_switch_btn_loc).click() # 点击'介绍页开关'
            self.loc_element(*new_topic_finish_btn_loc).click() # 点击'完成'按钮



















