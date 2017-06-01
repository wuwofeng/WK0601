#-*- coding:utf-8 -*-

# ========================================================
# Description    : Test case for new live room
# Author         : Arthur
# Create Date    : 2015-10-10
# ========================================================

import unittest
from h5_project.common.app_driver import *
from h5_project.h5_page.weixin_page import OpenOA
from h5_project.h5_page.oa_page import *

class TestNewLiveRoom(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = get_app_driver()
        open_oa = OpenOA(cls.driver)
        open_oa.open_oa() # 打开微信公众号

    @classmethod
    def tearDownClass(cls):
        close_app_driver()

    # 一键创建直播间
    def test_new_live_room(self):

        live = LiveRoomPage(self.driver)
        live.enter_my_live_room() # 进到我的直播间页面
        live.new_live_room() # 新建直播间

        # assert_page_check

if __name__ == '__main__':
    unittest.main(verbosity=3)



