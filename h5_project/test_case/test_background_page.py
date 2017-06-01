#-*- coding:utf-8 -*-

# ========================================================
# Description    : Something
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================

from h5_project.h5_page.oa_page import *
from h5_project.h5_page.weixin_page import *
from h5_project.h5_page.background_page import *
import unittest
import time

from h5_project.common.app_driver import *

class TestBackgroundPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = get_app_driver()
        open_oa = OpenOA(cls.driver)
        open_oa.open_oa()  # 通过搜索千聊微信公众号，打开微信公众号

        live = LiveRoomPage(cls.driver)
        live.enter_my_live_room()  # 点微信公众号菜单列表上的'我的直播间'，进到我的直播间页面（直播间管理后台页面）

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        close_app_driver()


    def test_background_page(self):
        '''检查后台管理页面元素是否都存在'''

        backgroundpage = BackgroundPage(self.driver)
        backgroundpage.setup_operation() # 处理新功能推送 弹出的图片
        #page.page_all_element() # 打印所有元素内容

        page_element_contents = [u'切换直播间',u'直播间主页',u'个人中心']

        self.assertEqual(page_element_contents,backgroundpage.page_all_element())

if __name__ == '__main__':
    unittest.main(verbosity=3)