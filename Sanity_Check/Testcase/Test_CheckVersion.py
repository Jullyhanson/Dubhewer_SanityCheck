#QXX   2022.10.28检查版本号
import autoit
import unittest
import os
from PIL import ImageGrab
import time

#后期加一个判断脚本所在路径下是否有版本号截图的文件
import Global_Para

current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目根路径

save_path = current_path + '\image_%s/current/版本号截图'%(Global_Para.machine_type)

class Check_Version(unittest.TestCase):

    def setup(self):
        pass

    def test_1(self):

        #检查软件版本号，算法版本号和下位机版本号
        #点击admin
        autoit.mouse_click("left",1735, 40)
        time.sleep(1)
        #点击关于软件
        autoit.mouse_click("left", 1678, 146)
        time.sleep(1)
        #在关于软件界面连续点击5次
        autoit.mouse_click("left", 1092, 399,5)
        time.sleep(1)
        #截取软件版本号信息（后期需要加一个自动创建文件夹）
        im = ImageGrab.grab(bbox=(628,315,1289,724))  # 截取dubhe版本号
        im.save(save_path+'\dubhe版本号.png')  # 将图片保存到指定路径,此路径为拼接路径，让脚本可转移性增强
        time.sleep(1)
        #点击版本号信息界面的确定按钮
        autoit.mouse_click("left", 951, 697)
        time.sleep(1)
        #关闭关于软件界面
        autoit.mouse_click("left", 1269, 319)
        time.sleep(1)


        #查看dubheviewer版本号
        #先选中一个患者，这里选择第四个患者
        autoit.mouse_click("left", 1209, 447)
        time.sleep(1)
        #点击查看功能按钮
        autoit.mouse_click("left", 1817, 399)
        time.sleep(15)
        # 在dubheviewer界面连续点击10次
        autoit.mouse_click("left", 902, 43,10)
        time.sleep(1)
        # 截取dubheviewer版本号信息（后期需要加一个自动创建文件夹）
        im = ImageGrab.grab(bbox=(750, 384, 1147, 574))#截取dubheviewer版本号
        im.save(save_path+'\dubheviewer版本号.png')  # 将图片保存到指定路径
        time.sleep(1)
        # 点击版本号信息界面的确定按钮
        autoit.mouse_click("left", 1076, 551)
        time.sleep(1)
        # 关闭dubheviewer界面
        autoit.mouse_click("left", 1891, 15)
        time.sleep(1)

    def tearDown(self):
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()








