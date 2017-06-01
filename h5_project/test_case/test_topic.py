#-*- coding:utf-8 -*-

# ========================================================
# Description    : Test case for new live room
# Author         : Arthur
# Create Date    : 2015-10-10
# ========================================================

import unittest
from h5_project.h5_page.oa_page import *
from h5_project.h5_page.weixin_page import *
from h5_project.common.app_driver import *
from h5_project.h5_page.new_topic_page import *
from h5_project.h5_page.topic_introduction_page import *
from h5_project.h5_page.topic_live_page import *

class TestTopic(unittest.TestCase):

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



    def test_1_new_topic(self):
        '''检查能否成功新建话题'''

        live = LiveRoomPage(self.driver)
        live.enter_my_live_room()  # 进到我的直播间页面

        newtopicpage = NewTopicPage(self.driver)
        newtopicpage.fill_topic_info() # 填写直播话题基本信息
        newtopicpage.finish_new_topic() # 完成直播话题新建


    def test_2_edit_topic_introduction(self):
        '''检查能否成功编辑话题介绍'''

        # 进入话题介绍页
        # 编辑话题介绍
        global topicintroductionpage
        topicintroductionpage = TopicIntroductionPage(self.driver)
        topicintroductionpage.edit_topic_introduction()



    def test_3_send_voice(self):
        '''检查能否发语音'''

        # 进入话题直播（话题详情页）
        #topicintroductionpage = TopicIntroductionPage(self.driver)
        topicintroductionpage.enter_topic_live()
        # 发送语音
        topiclivepage = TopicLivePage(self.driver)
        topiclivepage.send_voice()
        sleep(5)

    def test_4_send_word(self):
        '''检查能否发文字'''
        topiclivepage = TopicLivePage(self.driver)
        topiclivepage.send_word()


    def atest_5_topic_op_menu(self):
        '''检查是否能移动到系列课'''

        # 进到
        # 打开话题操作菜单
        # 点击移动到系列课

    def test_6_topic_op_menu(self):
        '''检查是否可以结束话题'''

        # 打开话题操作菜单
        # 点击移动到系列课

    def test_7_topic_op_menu(self):
        '''检查是否可以切换直播间类型'''





if __name__ == '__main__':
    unittest.main(verbosity=3)

