#-*- coding:utf-8 -*-

# ========================================================
# Description    : Something
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================

import unittest
from h5_project.h5_page.oa_page import *
from h5_project.h5_page.weixin_page import *
from h5_project.common.app_driver import *
from h5_project.h5_page.new_channel_page import *

class TestChannel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        #create = raw_input(u'是否已经开通直播间[y/n] > ')

        cls.driver = get_app_driver()
        open_oa = OpenOA(cls.driver)
        open_oa.open_oa()  # 打开微信公众号


        # if create == 'y':
        #     print('You have been the live room!')
        # else:
        #     live = LiveRoomPage(cls.driver)
        #     live.enter_my_live_room()  # 进到我的直播间页面
        #     live.new_live_room()  # 新建直播间

    @classmethod
    def tearDownClass(cls):
        close_app_driver()



    def test_new_channel(self):
        '''检查能否成功新建系列课'''

        live_room_page = LiveRoomPage(self.driver)
        live_room_page.enter_my_live_room()  # 进到我的直播间页面

        new = NewChannelPage(self.driver)
        new.finish_new_channel()




if __name__ == '__main__':
    unittest.main(verbosity=3)