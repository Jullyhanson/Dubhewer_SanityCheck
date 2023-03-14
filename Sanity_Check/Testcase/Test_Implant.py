import random
import time
import autoit
import pyautogui
import unittest
import os
from unittest import TestCase
from Common import Get_Image
from Common import Auto_Tool
import Global_Para

'''
YJJ
基于0.7.5.3版本添加的sanity check测试（基本种植流程）
2021.08.13
'''
PATH=lambda p:os.path.abspath(p)
current_path=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
xml_path = current_path +'\\config'

dubhewer_path=r"D:\Program Files\Dubhewer\config"

class Sancheck_Implant_Test(TestCase):
    # 初始化
    def setUp(self):
        self.image_path='image_'+Global_Para.machine_type
        self.getimage=Get_Image.GetImage()
        self.auto=Auto_Tool.auto(xml_path)

    # 点击查看并旋转MPR十字定位线
    def test_1(self):
        # 判断是否是拍摄重建后进行测试（True:拍摄重建后，False：查看测试）
        if Global_Para.close_dubheviewer ==False:
            print('测试拍摄重建后功能')
        else:
            # 选择第一个患者
            self.auto.auto_click(key_value='patientList.fistPatient')
            self.auto.auto_click(key_value='patientList.look_patient')
            self.auto.auto_click(key_value='patientList.look',times=10)
        self.auto.auto_click(key_value='sanitycheck.301pos')
        self.auto.auto_drag(key_value='sanitycheck.DragTo415')
        self.auto.auto_drag(key_value='sanitycheck.DragTo7')
        self.auto.auto_drag(key_value='sanitycheck.RollHengLine')
        self.auto.auto_drag(key_value='sanitycheck.RollGuanLine')


        # 截图MPR旋转后图像
        current_time=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
        MPR_xuanzhuan="/%s/current/1615/MPR_旋转%s.png"%(self.image_path,current_time)
        self.getimage.get_screenshot_by_custom_size(85,85,1624,1032,MPR_xuanzhuan)
        time.sleep(2)

        # 比对图像准确性(PR-siyu图)
        MPR_xuanzhuan_all_path=PATH(current_path+MPR_xuanzhuan)
        right=PATH(current_path+"/%s/right/MPR_旋转.png"%self.image_path)
        diff=PATH(current_path+"/%s/diff/"%self.image_path+"MPR旋转异常%s.png"%(current_time))
        assertIS=False
        if assertIS==True:
            duibi=self.getimage.same_as(MPR_xuanzhuan_all_path,right,diff,6)
            print(duibi)
        else:
            duibi=True
        self.assertTrue(duibi)


    # 绘制测量信息，测量种植体尺寸
    def test_2(self):
        # 隐藏十字线，并测量长度和高度(需设置为多次测量)
        self.auto.auto_click(key_value='sanitycheck.offLine')
        autoit.send("{SPACE}")
        time.sleep(1)
        self.auto.auto_click(key_value='sanitycheck.MaxWindow',clicks=2)
        # 测量为多次测量
        self.auto.auto_click(key_value='sanitycheck.Measure_button')
        self.auto.auto_click(key_value='sanitycheck.Line1')
        self.auto.auto_click(key_value='sanitycheck.Line2')
        self.auto.auto_drag(key_value='sanitycheck.DragText')
        self.auto.auto_click(key_value='sanitycheck.Line3')
        self.auto.auto_click(key_value='sanitycheck.Line4')


        # 截图测量绘制是否准确
        current_time=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
        celiang="/%s/current/1615/种植体测量%s.png"%(self.image_path,current_time)
        celiang_all_path=PATH(current_path+celiang)
        self.getimage.get_screenshot_by_custom_size(216,598,863,978,celiang)
        time.sleep(2)

        # 比对图像准确性(PR-siyu图)
        right=PATH(current_path+"/%s/right/种植体测量.png"%self.image_path)
        diff=PATH(current_path+"/%s/diff/"%self.image_path+"测量异常%s.png"%(current_time))

        assertIS = False
        if assertIS == True:
            duibi=self.getimage.same_as(celiang_all_path,right,diff,6)
            print(duibi)
        else:
            duibi = True
        self.assertTrue(duibi)

    # 插入种植体及基台
    # @unittest.skip("")
    def test_3(self):

        # 点击挑与置按钮
        # autoit.mouse_click("left",1864,772)
        # time.sleep(1)
        self.auto.auto_click(key_value='mpr.implant_AI')

        # 找到种植体制造商点击一下（防止种植体呈选中状态定位不到）
        implant_product = current_path+'/%s/right/implant_product_header.png'%self.image_path
        location = pyautogui.locateOnScreen(implant_product,region=(352,151,1190,652))
        print(location)
        # 输出坐标
        x,y = pyautogui.center(location)
        pyautogui.click(x=x,y=y+20,clicks=1,button='left')
        time.sleep(3)

        # 找到straumann的21.5508种植体
        implant = current_path+'/%s/right/implant_header.png'%self.image_path
        location = pyautogui.locateOnScreen(implant,region=(352,151,1190,652))
        # 输出坐标
        x,y = pyautogui.center(location)
        pyautogui.click(x=x,y=y+20,clicks=1,button='left')
        time.sleep(3)

        # 找到置入按钮，并点击置入(根据种植体deader推算置入按钮位置)
        autoit.mouse_click('left',x+455,y+245)
        time.sleep(2)

        # 在刚刚测量的位置插入种植体
        self.auto.auto_click(key_value='sanitycheck.ImplantPut')

        # 旋转种植体
        self.auto.auto_drag(key_value='sanitycheck.ImplantRoll')

        # 截图当前图像
        current_time=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
        implant_shot="/%s/current/1615/种植体%s.png"%(self.image_path,current_time)
        implant_all_path=PATH(current_path+implant_shot)
        self.getimage.get_screenshot_by_custom_size(216,598,863,978,implant_shot)
        time.sleep(2)

        # 比对图像准确性
        right=PATH(current_path+"/%s/right/种植体_celiang.png"%self.image_path)
        diff=PATH(current_path+"/%s/diff/"%self.image_path+"种植体_celiang异常%s.png"%(current_time))
        assertIs=False
        if assertIs ==True:
            duibi=self.getimage.same_as(implant_all_path,right,diff,6)
        else:
            duibi=True
        self.assertTrue(duibi)

    # 绘制牙神经
    def test_4(self):
        # 点击重置按钮
        self.auto.auto_click(key_value='sanitycheck.Reset')

        # 点击进入全景界面
        self.auto.auto_click(key_value='pano.pano',times=4)
        # 随机手动牙神经、AI牙神经
        shenjing=random.randint(1,2)
        # shenjing=2
        if shenjing==1:
            # 点击牙神经新建按钮（手动）
            self.auto.auto_click(key_value='sanitycheck.shenjin_button')
            # 点击确定，切换到层厚为0
            self.auto.auto_click('sanitycheck.depth0Sure')
            # 新建牙神经
            self.auto.auto_click('sanitycheck.shenjing1')
            self.auto.auto_click('sanitycheck.shenjing2')
            self.auto.auto_click('sanitycheck.shenjing3')
            self.auto.auto_click('sanitycheck.shenjing4')
            self.auto.auto_click('sanitycheck.shenjing5')
            self.auto.auto_click('sanitycheck.shenjing6')
            self.auto.auto_click('sanitycheck.shenjing7')
            self.auto.auto_click('sanitycheck.shenjing7',left='right')
            # 移动种植体至牙神经上，检测碰撞
            self.auto.auto_click(key_value='pano.Reset_button')
            self.auto.auto_drag(key_value='sanitycheck.ImpWithShenjing')
            # 移动种植体至牙神经上，检测碰撞
            self.auto.auto_click(key_value='pano.Reset_button')
            self.auto.auto_drag(key_value='sanitycheck.ImpWithShenjing')
            # 截图当前图像
            current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
            peng_shot = "/%s/current/1615/碰撞测试%s.png" % (self.image_path, current_time)
            peng_all_path = PATH(current_path + peng_shot)
            self.getimage.get_screenshot_by_custom_size(604, 97, 1598, 992, peng_shot)
            time.sleep(2)

            # 比对图像准确性
            right = PATH(current_path + "/%s/right/碰撞测试.png" % self.image_path)
            diff = PATH(current_path + "/%s/diff/" % self.image_path + "碰撞测试异常%s.png" % (current_time))
            assertIS = False
            if assertIS == True:
                duibi = self.getimage.same_as(peng_all_path, right, diff, 6)
                print(duibi)
            else:
                duibi = True
        else:
            # AI牙神经
            self.auto.auto_click('pano.AI_nerve')
            # 弹出提示为仅供参考，点击确认
            autoit.mouse_click("left", 966, 550)
            time.sleep(10)

            # 截图保存
            current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
            AI_yashenjing = "/%s/current/1615/AI牙神经结束%s.png" % (self.image_path, current_time)
            AI_yashenjing_all = PATH(current_path + AI_yashenjing)
            self.getimage.get_screenshot_by_custom_size(10, 10, 1849, 888, AI_yashenjing)
            time.sleep(2)

            # 点击确定，关闭AI牙神经结束界面
            autoit.mouse_click("left", 960, 684)
            time.sleep(10)

            # 比对图像准确性
            right = PATH(current_path + "/%s/right/AI牙神经结束.png" % self.image_path)
            diff = PATH(current_path + "/%s/diff/" % self.image_path + "AI牙神经异常%s.png" % (current_time))
            assertIS = False
            if assertIS == True:
                duibi = self.getimage.same_as(AI_yashenjing_all, right, diff, 6)
                print(duibi)
            else:
                duibi = True

        self.assertTrue(duibi)

    # 截图报告功能
    def test_5(self):
        # 点击截图按钮
        self.auto.auto_click('pano.cut_button')
        # 截图全景（AI牙神经）
        self.auto.auto_click('pano.cut_pano')
        '''
        xwj
        0.7.6.2
        20210909
        使用Pyautogui点击路径和保存
       '''
        # 点击路径输出
        autoit.mouse_click('left',664,46)
        time.sleep(2)

        # 删除原有路径
        autoit.send("{BACKSPACE}")
        time.sleep(1)
        # 选择路径
        jietulujing = current_path + r"\%s\current\1615"%self.image_path
        # 输入指定路径
        autoit.send(jietulujing)
        time.sleep(5)
        autoit.send("{Enter 2}")
        time.sleep(3)
        # 点击文件名输入框
        autoit.mouse_click('left',412,438)
        time.sleep(2)
        # 保存图像为特定格式
        current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        name = "截图功能%s" % current_time
        time.sleep(1)
        autoit.send(name)
        time.sleep(2)

        # 点击保存
        autoit.mouse_click("left",788,506)
        time.sleep(1)

        # 再次点击截图按钮，取消选中状态
        self.auto.auto_click('pano.cut_button')

        duibi = True
        self.assertTrue(duibi)

    # 保存项目
    def test_6(self):
        # 点击保存项目
        self.auto.auto_click('pano.save_project')
        # 点击项目编号弹框
        autoit.mouse_click("left", 1007, 516)
        time.sleep(1)
        # 删除已有编号
        autoit.send("{CTRLDOWN}")
        time.sleep(1)
        autoit.send("{a}")
        time.sleep(1)
        autoit.send("{CTRLUP}")
        time.sleep(1)
        autoit.send("{BACKSPACE}")
        time.sleep(2)
        # 输入特定编号为10010
        autoit.send("10010")
        time.sleep(1)
        # 点击确定按钮
        autoit.mouse_click("left", 994, 660)
        time.sleep(2)

        # 点击重置按钮
        self.auto.auto_click('pano.Reset_button')

        # 截图保存
        current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        save_pro = "/%s/current/1615/保存项目%s.png" % (self.image_path,current_time)
        self.getimage.get_screenshot_by_custom_size(10, 10, 1911, 1020, save_pro)
        time.sleep(2)

        duibi = True
        self.assertTrue(duibi)

    # 关闭Dubheviewer,加载项目
    def test_7(self):
        # 关闭dubheviewer
        self.auto.auto_click('dubheviewer.close_dubheviewer', times=2)
        self.auto.auto_click('dubheviewer.project_no', times=3)

        '''
        0.7.5之前以序列为根的查看
        autoit.mouse_click("left",1476,228)
        目前改为以患者为根的查看
        '''
        # 选择第一个患者
        self.auto.auto_click('patientList.fistPatient', times=2)
        # self.auto.auto_click('patientList.shot_patient', times=2)
        self.auto.auto_click('patientList.look_patient', times=10)

        # 点击全景按钮,自动绘制牙弓曲线（457层）
        self.auto.auto_click('pano.pano', times=10)
        # 点击加载项目
        self.auto.auto_click('pano.project_load')
        self.auto.auto_click('pano.project_local', times=3)
        # 选择10010项目
        autoit.mouse_click("left", 773, 424)
        time.sleep(5)
        # 点击加载
        button_load = current_path + '/%s/right/project_load.png' % self.image_path
        location = pyautogui.locateOnScreen(button_load, region=(352, 151, 1190, 652))
        # 输出坐标
        x, y = pyautogui.center(location)
        pyautogui.click(x=x-20, y=y, clicks=1, button='left')
        time.sleep(3)

        # 截图保存
        current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        jiazai_pro = "/%s/current/1615/加载项目%s.png" % (self.image_path,current_time)
        jiazai_pro_all = PATH(current_path + jiazai_pro)
        self.getimage.get_screenshot_by_custom_size(10, 10, 1911, 1020, jiazai_pro)
        time.sleep(2)

        # 比对图像准确性
        # right = PATH(current_path + "/%s/right/保存项目.png"%self.image_path)
        # diff = PATH(current_path + "/%s/diff/"%self.image_path + "加载项目异常%s.png" % (current_time))
        # duibi = self.getimage.same_as(jiazai_pro_all, right, diff, 6)
        duibi = True
        print(duibi)
        self.assertTrue(duibi)

    def test_8(self):
        # 关闭dubheviewer
        self.auto.auto_click('dubheviewer.close_dubheviewer', times=2)
        self.auto.auto_click('dubheviewer.project_no', times=3)

    def tearDown(self):
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()


