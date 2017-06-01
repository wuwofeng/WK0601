#-*- coding:utf-8 -*-

# ========================================================
# Description    : run test case
# Author         : Arthur
# Create Date    : xxxx-xx-xx
# ========================================================

import unittest
from h5_project.test_case.test_background_page import TestBackgroundPage
from h5_project.test_case.test_topic import TestTopic
from h5_project.test_case.test_channel import TestChannel

suite = unittest.TestSuite()
suite.addTest(TestBackgroundPage("test_background_page")) # 测试直播间管理后台
suite.addTest(TestTopic("test_1_new_topic")) # 测试新建话题
suite.addTest(TestTopic("test_2_edit_topic_introduction")) # 测试编辑介绍页
suite.addTest(TestTopic("test_3_send_voice")) # 测试话题发语音
suite.addTest(TestChannel("test_new_channel")) # 测试新建系列课

runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)



'''

a. B端：编辑、操作话题（新建已完成）
b. B端：编辑、操作系列课（新建已完成）
c. B端：新建直播间、管理后台页面检查（都已完成）
d. C端：话题、系列课报名
e. C端：课间操作（提问、发言）
f. 推送

'''