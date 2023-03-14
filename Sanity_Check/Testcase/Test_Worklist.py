import os,time
from unittest import TestCase
from Common import Auto_Tool,File_Tool,Get_Image

current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目根路径
xml_path = current_path +'\\config'

'''
yjj,2022.12.06
前提条件：1. 手动配置好worklist的环境
        2. 手动创建患者数据可供worklist导入
'''
class Test_Worklist(TestCase):
    def setUp(self):
        self.auto = Auto_Tool.auto(xml_path)
        self.save_file = File_Tool.File_Handle()
        self.get_image = Get_Image.GetImage()

    def test_1(self):
        # 点击worklist按钮
        self.auto.auto_click('patientList.Worklist_button')
        # 点击查询按钮
        self.auto.auto_click('patientList.Worklist_query')
        

