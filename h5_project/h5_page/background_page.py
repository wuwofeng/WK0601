#-*- coding:utf-8 -*-

# ========================================================
# Description    : Some options for background page
# Author         : Arthur
# Create Date    : 2017-04-20
# ========================================================

from h5_project.common.page_operation import PageOp
from selenium.webdriver.common.by import By

class BackgroundPage(PageOp):

    # android:id / text1 # title 千聊
    # // *[ @ id = "backroomHeader"] / div[1] / span[1] / a / img # 直播间头像
    # // *[ @ id = "backroomHeader"] / div[1] / span[2] / a # 直播间名称
    # // *[ @ id = "backPageBox"] / ul / li[1] / b # 点击发起直播

    #
    # # 所有粉丝数
    # // *[ @ id = "backroomHeader"] / div[2] / a[1]
    # // *[ @ id = "backroomHeader"] / div[2] / a[1] / var
    # // *[ @ id = "backroomHeader"] / div[2] / a[1] / i
    #
    #
    # # 昨日直播间收益
    #
    # // *[ @ id = "backroomHeader"] / div[2] / a[2]
    # // *[ @ id = "backroomHeader"] / div[2] / a[2] / var
    #
    # // *[ @ id = "backroomHeader"] / div[2] / a[2] / i
    #
    #
    # # 管理 - 九宫格
    # // *[ @ id = "backPageBox"] / div[3] / div[2] / section[1] / h1
    # // *[ @ id = "backPageBox"] / div[3] / div[2] / section[1] / a[1~9] # 直播间主页
    #
    # # 营销 - 九宫格
    # // *[ @ id = "backPageBox"] / div[3] / div[2] / section[2] / h1
    # // *[ @ id = "backPageBox"] / div[3] / div[2] / section[2] / a[1~9]
    #
    # # 服务 - 九宫格
    # // *[ @ id = "backPageBox"] / div[3] / div[2] / section[3] / h1
    # // *[ @ id = "backPageBox"] / div[3] / div[2] / section[3] / a[1~9]

    new_topic_btn_loc = (By.XPATH, r'//*[@id="backPageBox"]/ul/li[1]/a')  # '新建话题'按钮位置
    new_channel_btn_loc = (By.XPATH, '//*[@id="backPageBox"]/ul/li[2]/a')  # 新建系列课按钮位置


    close_push_btn_loc = (By.XPATH, r'/html/body/div[5]/div/a')  # 新功能推送图片'关闭'按钮位置


    word_scroll_loc = (By.XPATH, r'//*[@id="backPageBox"]/div[1]')  # 管理后台页面顶部 '动态通知栏'位置
    change_live_room_btn_loc = (By.XPATH, r'//*[@id="backroomHeader"]/div[1]/a')  # 管理后台页面顶部 '切换直播间'按钮位置
    live_room_home_btn_loc = (By.XPATH, r'/html/body/div[2]/a[1]')  # 导航栏'直播间主页'按钮位置
    person_center_btn_loc = (By.XPATH, r'/html/body/div[2]/a[2]')  # 导航栏'个人中心'按钮位置

    def setup_operation(self):
        self.switch_to_h5()  # 切换到h5
        try:
            self.loc_element(*self.close_push_btn_loc).click()  # 点新功能推送图片'关闭'按钮
        except:
            pass

        #self.clear_cache()

    def page_all_element(self):

        element_contents = [
            #self.loc_element(*self.word_scroll_loc).text,
            self.loc_element(*self.change_live_room_btn_loc).text,
            self.loc_element(*self.live_room_home_btn_loc).text,
            self.loc_element(*self.person_center_btn_loc).text
        ]
        #print(element_contents)
        return element_contents

    def enter_new_topic_page(self):

        self.switch_to_h5()

        try:
            self.loc_element(*self.close_push_btn_loc).click() # 点新功能推送图片'关闭'按钮
        except:
            pass
        finally:
             self.loc_element(*self.new_topic_btn_loc).click() # 点'新建话题'按钮

        self.clear_cache()


    def enter_new_channel_page(self):

        self.switch_to_h5() # 切换到h5
        self.loc_element(*self.new_channel_btn_loc).click() # 点击新建直播间按钮
        self.clear_cache() # 清缓存


    def navigation_bar_home_page(self):
        self.loc_element(*self.live_room_home_btn_loc).click() # 点击导航栏'直播间主页'按钮，进到直播间主页

    def navigation_bar_person_page(self):
        self.loc_element(*self.person_center_btn_loc).click() # 点击导航栏'个人中心'按钮，进到个人中心

