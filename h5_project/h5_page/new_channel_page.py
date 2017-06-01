#-*- coding:utf-8 -*-

# ========================================================
# Description    : Something
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================


from h5_project.common.page_operation import PageOp
from selenium.webdriver.common.by import By
from h5_project.h5_page.background_page import BackgroundPage


class NewChannelPage(PageOp):

    uploader_btn_loc = (By.XPATH, '//*[@id="file"]') # 上传系列课海报按钮

    # List 1
    channel_name_btn_loc = (By.XPATH, '/html/body/div[1]/ul/li[1]/span[2]/a') # 系列课名称按钮位置
    channel_name_input_box_loc = (By.XPATH, '/html/body/div[5]/div/span/input') # 系列课名称输入框位置
    channel_name_confirm_btn_loc = (By.XPATH, '/html/body/div[5]/div/div[2]/a[2]') # 系列课名称确定按钮位置
    channel_name_cancel_btn_loc = (By.XPATH, '/html/body/div[5]/div/div[2]/a[1]') # 系列课名称取消按钮位置

    # List 2
    course_plan_btn_loc = (By.XPATH, '/html/body/div[1]/ul/li[2]/span[2]/a') # 排课计划按钮位置
    course_plan_input_box_loc = (By.XPATH, '/html/body/div[10]/div/span/input') # 开课节数输入框位置
    course_plan_confirm_btn_loc = (By.XPATH, '/html/body/div[10]/div/div[2]/a[2]') # 排课计划确定按钮位置
    course_plan_cancel_btn_loc = (By.XPATH, '/html/body/div[10]/div/div[2]/a[1]') # 排课计划取消按钮位置

    # List 3
    channel_type_btn_loc = (By.XPATH, '/html/body/div[1]/ul/li[3]/span[2]/a') # 系列课分类按钮位置

    # List 4
    charge_type_btn_loc = (By.XPATH, '/html/body/div[1]/ul/li[4]/span[2]/a') # 收费类型按钮位置

    #
    # List 4 - 固定收费
    #
    fixed_charge_btn_loc = (By.XPATH, '//*[@id="charge-type-modal-list"]/li[1]') # 固定收费按钮位置
    # List 4 - 固定收费 - 门票价格
    fixed_charge_input_box_loc = (By.XPATH, '//*[@id="charge-type-row-absolutely"]/span/input') # 门票价格输入框位置

    # List 4 - 固定收费 - 营销推广
    marketing_type_btn_loc = (By.XPATH, '//*[@id="channel-marketing-type-setting"]/span[2]/a') # 营销推广按钮位置
    # List 4 - 固定收费 - 营销推广 - 特价优惠
    sale_btn_loc = (By.XPATH, '//*[@id="marketing-type-modal-list"]/li[1]') # 营销推广-特价优惠按钮位置
    # List 4 - 固定收费 - 营销推广 - 特价优惠 - 优惠价格
    sale_price_input_box_loc = (By.XPATH, '//*[@id="channel-marketing-discount-input"]') # 优惠价格输入框位置


    # List 4 - 固定收费 - 营销推广 - 拼课
    fight_course_btn_loc = (By.XPATH, '//*[@id="marketing-type-modal-list"]/li[2]') # 营销推广-拼课按钮位置
    fight_course_number_of_people_btn_loc = (By.XPATH, '//*[@id="channel-marketing-group-setting"]') # 设置拼课人数按钮位置
    fight_course_number_of_people_input_box_loc = (By.XPATH, '//*[@id="group-member-modal"]/div/span/input') # 拼课人数输入框位置
    fight_course_number_of_people_confirm_btn_loc = (By.XPATH, '//*[@id="group-member-modal"]/div/div[2]/a[2]')
    fight_course_number_of_people_cancel_btn_loc = (By.XPATH, '//*[@id="group-member-modal"]/div/div[2]/a[1]')
    fight_course_price_input_box_loc = (By.XPATH, '//*[@id="channel-marketing-group-input"]') # 拼课价格输入框位置

    # List 4 - 固定收费 - 营销推广 - 暂不使用
    dont_use_btn_loc = (By.XPATH, '//*[@id="marketing-type-modal-list"]/li[3]') # 营销推广-暂不使用按钮位置


    #
    # List 4 - 按时收费
    #
    time_charge_btn_loc = (By.XPATH, '//*[@id="charge-type-modal-list"]/li[2]') # 按时收费按钮位置
    charge_standard__btn_loc = (By.XPATH, '') # 收费标准按钮位置

    number_of_month_input_box_loc = (By.XPATH, '/html/body/div[8]/div/div[2]/table/tbody/tr[1]/td[1]/input') # '月'输入框位置
    number_of_yuan_input_box_loc = (By.XPATH, '/html/body/div[8]/div/div[2]/table/tbody/tr[1]/td[3]/input') # '元'输入框位置

    # /html/body/div[8]/div/div[2]/table/tbody/tr[2]/td[1]/input

    charge_mode_delete_btn_loc = (By.XPATH, '/html/body/div[8]/div/div[2]/table/tbody/tr/td[5]/a') # 收费方式删除按钮位置

    charge_mode_adding_btn_loc = (By.XPATH, '/html/body/div[8]/div/a') # 添加一个收费类型按钮位置

    time_charge_cancel_btn_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/a[1]') # 设置按时收费取消按钮位置
    time_charge_confirm_btn_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/a[2]') # 设置按时收费确认按钮位置



    charge_type_confirm_btn_loc = (By.XPATH, '//*[@id="charge-type-modal"]/div[2]/div/a[2]') # 选择收费类型确定按钮
    charge_type_cancel_btn_loc = (By.XPATH, '//*[@id="charge-type-modal"]/div[2]/div/a[1]') # 选择收费类型取消按钮

    # Finishing new channel
    new_channel_confirm_btn_loc = (By.XPATH, '/html/body/div[1]/div[2]/a') # 新建系列课确定按钮位置


    def finish_new_channel(self):
        new = BackgroundPage(self.driver)
        new.enter_new_channel_page() # 点击直播间管理后台的 新建系列课按钮

        # 输入系列课名称
        self.loc_element(*self.channel_name_btn_loc).click() # 点击系列课名称按钮
        self.loc_element(*self.channel_name_input_box_loc).send_keys('Channel') # 输入系列课名称
        self.loc_element(*self.channel_name_confirm_btn_loc).click() # 点击确定
        # 输入计划排课节数
        self.loc_element(*self.course_plan_btn_loc).click() # 点击排课计划
        self.loc_element(*self.course_plan_input_box_loc).send_keys(5) # 输入排课节数
        self.loc_element(*self.course_plan_confirm_btn_loc).click() # 点击确定
        # 选择系列课分类
        # self.loc_element(*self.channel_type_btn_loc).click()
        # 选择收费类型（选择固定收费）
        self.loc_element(*self.charge_type_btn_loc).click() # 点击收费类型
        self.loc_element(*self.fixed_charge_btn_loc).click() # 选择固定收费
        self.loc_element(*self.charge_type_confirm_btn_loc).click() # 点击确定
        # 输入门票价格
        self.loc_element(*self.fixed_charge_input_box_loc).send_keys(10)  # 输入固定收费门票价格
        # 点击确定完成系列课新建
        self.loc_element(*self.new_channel_confirm_btn_loc).click() # 点击确定按钮







