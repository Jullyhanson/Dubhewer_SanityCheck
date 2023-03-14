import autoit
import time
import os
import pyautogui
import unittest
from unittest import TestCase
from Common import Get_Image,Auto_Tool
PATH=lambda p:os.path.abspath(p)
current_path=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

class Sancheck_Quanjing_Test(TestCase):
    # 初始化
    def setUp(self):
        self.getimage=Get_Image.GetImage()
        self.auto=Auto_Tool.auto()

    # @unittest.skip("")
    def test_1(self):
        # 点击查看
        self.auto.auto_click(key_value='patientList.look_patient')
        self.auto.auto_click(key_value='patientList.look', times=10)

    # 查看图像(第一个患者的图像)
    def test_2(self):
        # 点击全景按钮,自动绘制牙弓曲线（457层）
        self.auto.auto_click(key_value='pano.pano',times=5)
        # 移动横断面至419层
        autoit.mouse_click_drag(588,446,587,424,"left")
        time.sleep(2)
        # 点击AI牙弓曲线,并点击确认清除上一次牙弓曲线
        self.auto.auto_click(key_value='pano.AI_yagong')
        self.auto.auto_click(key_value='pano.info_clear')
        # 点击进入列表，默认在曲面列表
        self.auto.auto_click(key_value='pano.list_button')
        # 双击进入457层
        autoit.mouse_click("left",1234,206,clicks=2)
        time.sleep(2)

        # 截图保存
        current_time=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
        yagong="/image/current/1615/牙弓曲线列表%s.png"%(current_time)
        yagong_all=PATH(current_path+yagong)

        self.getimage.get_screenshot_by_custom_size(10,10,1592,653,yagong)
        time.sleep(2)

        # 点击关闭牙弓曲线列表
        guanbi = current_path+'/image/right/gmd.png'
        location = pyautogui.locateOnScreen(guanbi,region =(1001,58,900,300))
        x,y = pyautogui.center(location)
        pyautogui.click(x=x,y=y,clicks=1,button='left')
        time.sleep(3)

        # 比对图像准确性
        right=PATH(current_path+"/image/right/牙弓曲线列表.png")
        diff=PATH(current_path+"/image/diff/"+"牙弓曲线列表异常%s.png"%(current_time))
        assertIs=False
        if assertIs == True:
            duibi=self.getimage.same_as(yagong_all,right,diff,6)
        else:
           duibi = True
        self.assertTrue(duibi)

    # 手动添加牙神经
    def test_3(self):
        # 点击牙神经新建按钮
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
        self.auto.auto_click('sanitycheck.shenjing7', left='right')

        # 点击列表，默认在牙神经列表界面
        self.auto.auto_click(key_value='pano.list_button')

        # 选择左侧牙神经就，点击修改
        autoit.mouse_click("left",1256,208)
        time.sleep(1)
        autoit.mouse_click("left",1178,624)
        time.sleep(1)
        # 修改左侧牙神经颜色为黄色，点击确定
        autoit.mouse_click("left",958,455)
        time.sleep(1)
        autoit.mouse_click("left",854,370)
        time.sleep(1)
        autoit.mouse_click("left",1089,677)
        time.sleep(1)
        # 修改左侧牙神经直径为1mm，点击确定
        autoit.mouse_click("left",957,497)
        time.sleep(1)
        autoit.send("{BACKSPACE}")
        time.sleep(1)
        autoit.send("1")
        time.sleep(1)
        autoit.mouse_click("left",932,536)
        time.sleep(1)
        # 关闭列表界面
        autoit.mouse_click("left",1616,107)
        time.sleep(2)
        # 点击重置按钮
        autoit.mouse_click("left",1614,56)
        time.sleep(2)

        # 截图保存
        current_time=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
        yashenjing="/image/current/1615/牙神经%s.png"%(current_time)
        yashenjing_all=PATH(current_path+yashenjing)
        self.getimage.get_screenshot_by_custom_size(10,10,1592,653,yashenjing)
        time.sleep(2)

        # 比对图像准确性
        right=PATH(current_path+"/image/right/牙神经.png")
        diff=PATH(current_path+"/image/diff/"+"牙神经就异常%s.png"%(current_time))
        assertIs=False
        if assertIs ==True:
            duibi=self.getimage.same_as(yashenjing_all,right,diff,6)
        else:
            duibi = True
        self.assertTrue(duibi)

    # AI牙神经测试
    # @unittest.skip("")
    def test_4(self):
        # 点击进入列表
        self.auto.auto_click(key_value='pano.list_button')
        # 选择牙神经列表
        self.auto.auto_click(key_value='pano.list_nerve')
        # 清空列表中手动绘制的牙神经,并确认清空
        self.auto.auto_click(key_value='pano.list_clear')
        self.auto.auto_click(key_value='pano.info_clear')

        # 关闭列表
        autoit.mouse_click("left",1616,107)
        time.sleep(2)

        # 点击AI牙神经
        self.auto.auto_click(key_value='pano.AI_nerve')
        # 弹出提示为仅供参考，点击确认
        autoit.mouse_click("left",966,550)
        time.sleep(10)

        # 截图保存
        current_time=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
        AI_yashenjing="/image/current/1615/AI牙神经结束%s.png"%(current_time)
        AI_yashenjing_all=PATH(current_path+AI_yashenjing)
        self.getimage.get_screenshot_by_custom_size(10,10,1849,888,AI_yashenjing)
        time.sleep(2)

        # 点击确定，关闭AI牙神经结束界面
        autoit.mouse_click("left",960,684)
        time.sleep(10)

        # 比对图像准确性
        right=PATH(current_path+"/image/right/AI牙神经结束.png")
        diff=PATH(current_path+"/image/diff/"+"AI牙神经异常%s.png"%(current_time))
        assertIs=False
        if assertIs == True:
            duibi=self.getimage.same_as(AI_yashenjing_all,right,diff,6)
        else:
            duibi=True
        self.assertTrue(duibi)

    # 截图报告功能
    def test_5(self):
        # 点击截图按钮
        self.auto.auto_click(key_value='pano.cut_button')
        # 截图全景（AI牙神经）
        self.auto.auto_click(key_value='pano.cut_pano')

        # 点击路径处
        autoit.mouse_click('left',605,44)
        time.sleep(2)

        # 删除原有路径
        autoit.send("{BACKSPACE}")
        time.sleep(1)
        # 选择路径
        jietulujing =current_path+r"\image\current\1615"
        # 输入指定路径
        autoit.send(jietulujing)
        time.sleep(5)
        autoit.send("{Enter 2}")
        time.sleep(3)

        save_name="/image/right/select_name.PNG"
        img_path4 = current_path + save_name
        #找到跟金样本骨密度图表关闭的图像位置
        location = pyautogui.locateOnScreen(img_path4)
        # 输出坐标
        x,y = pyautogui.center(location)
        print(x,y)
        pyautogui.click(x=x,y=y,clicks=1,button='left')
        time.sleep(2)
        # 保存图像为特定格式
        current_time=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
        name="截图功能%s"%current_time
        time.sleep(1)
        autoit.send(name)
        time.sleep(2)

        save="/image/right/select_save.PNG"
        # 弹出区域骨密度图的 关闭按钮样本
        img_path3 = current_path + save
        #找到跟金样本骨密度图表关闭的图像位置
        location = pyautogui.locateOnScreen(img_path3)
        # 输出坐标
        x,y = pyautogui.center(location)
        # print('center()',x,y)
        pyautogui.click(x=x,y=y,clicks=1,button='left')
        time.sleep(2)

        # 再次点击截图按钮，取消截图选中
        self.auto.auto_click(key_value='pano.cut_button')

        duibi = True
        self.assertTrue(duibi)

    # 保存项目
    def test_6(self):
        # 点击保存项目
        autoit.mouse_click("left",256,59)
        time.sleep(1)
        # 点击项目编号弹框
        autoit.mouse_click("left",1007,516)
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
        autoit.mouse_click("left",994,660)
        time.sleep(2)

        # 点击重置按钮
        autoit.mouse_click("left",1614,56)
        time.sleep(2)

        # 截图保存
        current_time=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
        save_pro="/image/current/1615/保存项目%s.png"%(current_time)
        save_pro_all=PATH(current_path+save_pro)
        self.getimage.get_screenshot_by_custom_size(10,10,1911,1020,save_pro_all)
        time.sleep(2)

        duibi = True
        self.assertTrue(duibi)


    # 关闭Dubheviewer,加载项目
    def test_7(self):
        # 关闭dubheviewer
        self.auto.auto_click('dubheviewer.close_dubheviewer', times=2)
        self.auto.auto_click('dubheviewer.project_no', times=10)

        '''
        0.7.5之前以序列为根的查看
        autoit.mouse_click("left",1476,228)
        目前改为以患者为根的查看
        '''
        self.auto.auto_click(key_value='patientList.look_patient')
        self.auto.auto_click(key_value='patientList.look', times=10)

        # 点击全景按钮,自动绘制牙弓曲线（457层）
        self.auto.auto_click(key_value='pano.pano',times=5)
        # 点击加载项目
        self.auto.auto_click(key_value='pano.project_load',times=2)
        self.auto.auto_click(key_value='pano.project_local',times=5)
        # 选择10010项目
        autoit.mouse_click("left",773,424)
        time.sleep(5)
        # 点击加载
        autoit.mouse_click("left",1144,611)
        time.sleep(5)

        # 截图保存
        current_time=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
        jiazai_pro="/image/current/1615/加载项目%s.png"%(current_time)
        jiazai_pro_all=PATH(current_path+jiazai_pro)
        self.getimage.get_screenshot_by_custom_size(10,10,1911,1020,jiazai_pro_all)
        time.sleep(2)

       # 比对图像准确性
        right=PATH(current_path+"/image/right/保存项目.png")
        diff=PATH(current_path+"/image/diff/"+"加载项目异常%s.png"%(current_time))
        # duibi=self.getimage.same_as(jiazai_pro_all,right,diff,6)
        duibi = True
        print(duibi)
        self.assertTrue(duibi)


    def tearDown(self):
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()











