#-*- coding:utf-8 -*-

# ========================================================
# Description    : Some operation for the wechat page
# Author         : Arthur
# Create Date    : 2015-10-10
# ========================================================


from selenium.webdriver.common.by import By
from h5_project.common.page_operation import PageOp



'''
# 通过微信搜索打开一个公众号(Official Account )
def open_oa():
    search_btn_loc = (By.NAME, u'搜索') # Wechat右上角搜索按钮的位置
    search_input_box_loc = (By.ID, r'com.tencent.mm:id/gr') # 搜索输入框
    searched_oa_loc = (By.ID, r'com.tencent.mm:id/j2') # 搜索到的OA位置
    #oa_page_title_loc = (By.ID, r'com.tencent.mm:id/gh') # 公众号页面title位置

    driver = PageOp()

    driver.loc_element(*search_btn_loc).click() # 点击搜索按钮
    driver.loc_element(*search_input_box_loc).send_keys(u'千聊Live') # 输入公众号名称
    driver.loc_element(*searched_oa_loc).click() # 点击搜索到的公众号，进入公众号页面

    #title = loc_element(*oa_page_title_loc).text # 获取title内容
'''

class OpenOA(PageOp):

    # 通过微信搜索打开一个公众号(Official Account )
    def open_oa(self):

        search_btn_loc = (By.NAME, u'搜索')  # Wechat右上角搜索按钮的位置
        search_input_box_loc = (By.ID, r'com.tencent.mm:id/gr')  # 搜索输入框
        searched_oa_loc = (By.ID, r'com.tencent.mm:id/j2')  # 搜索到的OA位置
        # oa_page_title_loc = (By.ID, r'com.tencent.mm:id/gh') # 公众号页面title位置

        self.loc_element(*search_btn_loc).click()  # 点击搜索按钮
        self.loc_element(*search_input_box_loc).send_keys(u'千聊Live')  # 输入公众号名称
        self.loc_element(*searched_oa_loc).click()  # 点击搜索到的公众号，进入公众号页面

