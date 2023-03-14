#QXX  上传和下载
#上传，需要在设置里将PACS地址配好
import unittest
from unittest import TestCase
import os
from PIL import ImageGrab
import time
import autoit
from Common import Auto_Tool

current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目根路径
upload_path = current_path + '\image_PR/current/上传截图'
download_path = current_path + '\image_PR/current/下载截图'


class Upload_Download(unittest.TestCase):
    timestring = time.strftime('%Y-%m-%d-%H-%H-%S', time.localtime())

    def setUp(self):
        self.auto = Auto_Tool.auto()

    # #将PACS地址
    # def test_1(self):

    #上传
    # @unittest.skip("")
    def test_1(self):
        #点击患者为根下的第一个序列
        self.auto.auto_click("PACS.upload_button", times=2)
        #点击上传按钮
        self.auto.auto_click("patientList.fistaddress", times=2)

        # # #下载进度条中间位置
        # # self.auto.auto_click("PACS.upload_zloading", times=2)
        # # 点击上传进度条末端
        # self.auto.auto_click("PACS.upload_loading", times=2)
        # #获取上传进度条末端颜色
        # self.Auto_Tool.auto.auto_rgb("PACS.upload_loading")

        # 读取进度条(进度条rgb)
        self.auto.Timer(x=1194,y=617,rgb_des=(229, 231, 233),time_delay=2,direction=0)


        #在点击上传20S后再截图
        im = ImageGrab.grab(bbox=(630, 313, 1289, 725))  # 上传中途截图
        im.save(upload_path + '\上传患者图像-%s.png' %(self.timestring ))  # 将图片保存到指定路径


    #下载
    def test_2(self):
        # PACS地址链接https://192.168.11.8:30007/dcm4chee-arc/ui2/#/study/study
        # address = "https://192.168.11.8:30007/dcm4chee-arc/ui2/#/study/study"
        #在患者列表第一个患者的坐标（1150，226）右键点击弹出下载功能
        autoit.mouse_click("right", 1150, 226)
        time.sleep(3)
        #点击下载功能（1216，249）
        # autoit.mouse_click("left", 1216, 249)
        # time.sleep(20)
        self.auto.auto_click("PACS.download_button", times=2)
        #点击查询功能
        self.auto.auto_click("PACS.query_button", times=2)
        # 选择第一个患者（329，408）
        self.auto.auto_click("PACS.first_download", times=2)
        #截图，为了好根据患者ID查询下载的患者
        im = ImageGrab.grab(bbox=(251, 188, 1670, 848))  # 在选择第一个患者后截取PACS导入界面
        im.save(download_path + '\下载患者信息-%s.png' %(self.timestring))  # 将图片保存到指定路径
        time.sleep(1)
        #点击导入功能（483，341）
        self.auto.auto_click("PACS.download_input", times=2)

        # 读取进度条(进度条rgb)
        self.auto.Timer(x=1194, y=617, rgb_des=(229, 231, 233), time_delay=2, direction=0)

        #预估下载完成后截图
        im = ImageGrab.grab(bbox=(630, 313, 1289, 725))  # 在选择第一个患者后截取PACS导入界面
        im.save(download_path + '\下载过程-%s.png' %(self.timestring))  # 将图片保存到指定路径
        time.sleep(1)

        # 关闭下载界面
        autoit.mouse_click('left',1647,210)
        time.sleep(2)


    def tearDown(self):
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()

