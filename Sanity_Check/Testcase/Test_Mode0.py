#QXX   1615快扫模式拍摄
import os,unittest,time,autoit
import random
from ddt import ddt,data,unpack
from unittest import TestCase
from Common import Auto_Tool,File_Tool,Get_Image,Performance_Total
from Testcase import Test_Preview
import Global_Para

current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目根路径
xml_path = current_path +'\\config'

dubheviewer_path=r"D:\Program Files\Dubheviewer\config"
dubhewer_path=r"D:\Program Files\Dubhewer\config"

class Test_Mode0(TestCase):
    def setUp(self):
        self.image_path='image_'+Global_Para.machine_type
        self.auto=Auto_Tool.auto(xml_path)
        self.save_file = File_Tool.File_Handle()
        self.get_image=Get_Image.GetImage()
        time_file=current_path +'\\result'+'\\Time_total.txt'
        self.tf=open(time_file,'a+')

    # 新建拍摄
    def test_1(self):
        """
        yjj: 新建拍摄+识别放线时间+识别重建时间，将时间记录在txt中
        :return:
        """
        # 获取拍摄前性能
        timestring = time.strftime('%Y-%m-%d', time.localtime())
        per_file= current_path + '\\性能'+timestring+'.txt'
        Performance_Total.Recon_Total().Performance_Save(per_file)
        time.sleep(5)


        # 点击新建拍摄按钮
        self.auto.auto_click("patientList.newPatient")
        # 点击用户名
        self.auto.auto_click("patientList.PatientName")
        # 输入用户名
        time_str=time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        name="1615快扫" +time_str
        autoit.send(name)
        time.sleep(1)
        # 记录用户名
        self.tf.writelines('用户名：'+name+'\n')
        # 输入检查医生1615快扫
        self.auto.auto_click("patientList.DoctorName", times=2)
        autoit.send(name)
        time.sleep(1)

        # 截取拍摄前患者信息
        patient_info = "/%s/current/拍摄界面截图/新建患者-1615快扫-%s.png" % (self.image_path,time_str)
        print('path:',patient_info)
        self.get_image.get_screenshot_by_custom_size(2, 22, 1909, 1025, patient_info)


        # 点击确定
        self.auto.auto_click("patientList.Enter", times=15)

        # 定位预览相关操作
        # dingwei = random.randint(1,2)
        dingwei = 2
        if dingwei == 1:
            Test_Preview.Test_Preview().test_1()
        if dingwei == 2:

            # 选取1615快扫模式
            autoit.mouse_click("left", 1618, 482)
            time.sleep(2)

            # 按下准备拍摄按钮
            self.auto.auto_click('FOV.start_shot', times=5)


        # 按下启动拍摄按钮
        self.auto.auto_click('FOV.start_shot')


        # 截取高清拍摄中预览图
        gry_current_image = "/%s/current/1615ks/高清拍摄中预览图%s.png" % (self.image_path,time_str)
        self.get_image.get_screenshot_by_custom_size(5, 13, 1909, 1025, gry_current_image)

        # 判断放线时间（进度条从红色变为蓝色）
        self.ray_time=Auto_Tool.auto().Timer(x=1588,y=107,rgb_des=(34,105,148),time_delay=2,direction=0)
        print('放线时间：%s s'%self.ray_time)
        self.tf.writelines('放线时间：%s s \n'%str(self.ray_time))


        # 判断重建时间（从弹出dubheviewer开始计算）
        time.sleep(3)
        self.recon_time = Auto_Tool.auto().Timer(x=54, y=963, rgb_des=(255, 255, 255), time_delay=2)+3
        print('重建时间：%s s' % self.recon_time)
        self.tf.writelines('重建时间：%s s \n' %str(self.recon_time))

        # 关闭dubheviewer
        if Global_Para.close_dubheviewer == False:
            time.sleep(20)
        else:
            # 关闭dubheviewer
            time.sleep(6)
            self.auto.auto_click('dubheviewer.close_dubheviewer')
            save_time = Auto_Tool.auto().Timer(x=1588, y=107, rgb_des=(34, 105, 148), time_delay=2, direction=0) + 10
            self.tf.writelines('保存文件时间：%s s \n' % str(save_time))
            print('保存文件时间：%s s \n' % str(save_time))
            self.tf.writelines('总时间：%s s \n' % str(self.ray_time + self.recon_time + save_time))

            # 若开启固定时间运行，则固定时间间隔跑第二组
            if Global_Para.Temp_Is == True:
                time_during = Global_Para.Time_during

                # time_during:配置文件中固定间隔，35：前期准备时间（新建患者~准备拍摄）
                # self.ray_time：放线时间 ，self.recon_time：重建时间，save_time：保存文件时间,10:最后等待时间
                time_sleep = time_during - 35 - self.ray_time - self.recon_time - save_time - 10
                print('等待时间：', time_sleep)
                time.sleep(abs(time_sleep))
            else:
                print('拍摄间隔随机')
        self.tf.writelines('\n')


    def tearDown(self):
        pass


if __name__ == "__main__":
    print("test")
    unittest.main()
