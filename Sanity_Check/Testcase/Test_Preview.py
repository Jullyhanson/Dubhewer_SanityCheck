import os,unittest,time,autoit
import random
from unittest import TestCase
from Common import Auto_Tool,File_Tool,Get_Image,Performance_Total

current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目根路径
xml_path = current_path +'\\config'

class Test_Preview(TestCase):
    def setUp(self) :
        self.auto = Auto_Tool.auto(xml_path)
        self.save_file = File_Tool.File_Handle()
        self.get_image = Get_Image.GetImage()

    def test_1(self):
        # 点击定位预览
        self.auto.auto_click('preview.pre_button')
        # 点击开始定位
        self.auto.auto_click('preview.pre_start', times=15)
        x = random.randint(1, 2)
        # x=2
        if x == 1:
            # 点击完成预览
            self.auto.auto_click('preview.pre_finish', times=10)
        if x == 2:
            # 点击重新预览
            self.auto.auto_click('preview.pre_again', times=2)
            # 点击开始定位
            self.auto.auto_click('preview.pre_start', times=15)
            # 点击完成预览
            self.auto.auto_click('preview.pre_finish', times=10)