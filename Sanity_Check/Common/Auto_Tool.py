import os
import time
import autoit
import pyautogui
from Common import XML_Handle
import random
import PIL.ImageGrab
from Common import Get_Image

current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目根路径
xml_path = current_path +'\\config'

class auto(object):
    def __init__(self,config_path=xml_path,png_path=""):
        self.Value = XML_Handle.XML_Handle(config_path,png_path)
        # self.png_Value = xml_handle.XML_Handle(png_path=png_path)

    def auto_click(self,key_value="",left="left",clicks=1,times=1):
        pos = self.Value.getPos(key_value)
        autoit.mouse_click(left,pos[0],pos[1],clicks= clicks)
        time.sleep(times)
       #  '''
       #  0783版本增加MONKEY测试
       #  xwj
       #  每次点击按钮后，都随机点击其他区域，并截图保存
       # '''
       #  random_x = random.randint(13,1902)
       #  random_y = random.randint(68,1028)
       #  random_click = random.randint(1,2)
       #  random_left = random.choice(['left', 'right'])
       #  print(random_left)
       #  autoit.mouse_click(random_left,random_x,random_y,clicks=random_click)
       #  time.sleep(1)
       #
       #  timestring = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
       #  self.getimage = get_image.GetImage()
       #  monkey_current_image = "/image/current/MONKEY图%s.png"%(timestring)
       #  self.getimage.get_screenshot_by_custom_size(5,13,1909,1025,monkey_current_image)


    def auto_send(self,key_value,times = 1):
        content = self.Value.getValue(key_value)
        autoit.send("{LSHIFT}")
        time.sleep(1)
        autoit.send(content)
        time.sleep(1)
        autoit.send("{LSHIFT}")
        time.sleep(times)

    def auto_move(self,key_value,times=2):
        pos = self.Value.getPos(key_value)
        autoit.mouse_move(pos[0],pos[1])
        time.sleep(times)

    def auto_mouse_key(self,key_value,times =2):
        autoit.send(key_value)
        time.sleep(times)

    def auto_drag(self,key_value="",left="left",times=1):
        value = self.Value.getValue(key_value)
        area=list(value.split(','))
        print(area)
        print(type(area))
        autoit.mouse_click_drag(int(area[0]),int(area[1]),int(area[2]),int(area[3]),left)
        print(int(area[0]),int(area[1]))
        print(int(area[2]),int(area[3]))
        time.sleep(times)

    def auto_send_(self,key_value,times=2):
        autoit.send("{LSHIFT}")
        time.sleep(1)
        autoit.send(key_value)
        time.sleep(1)
        autoit.send("{LSHIFT}")
        time.sleep(times)

    def auto_rgb(self,x,y):
        autoit.mouse_move(x,y)
        rgb=PIL.ImageGrab.grab().load()[x,y]
        print('rgb:',rgb)
        return rgb

    def Timer(self,x,y,rgb_des,time_delay,direction=1):
        """
        :param x: x坐标
        :param y: y坐标
        :param rgb_des:目标rgb
        :param time_delay: 隔多久读一次rgb
        :param direction: 1表示！=就一直循环，0表示==就一直循环
        :return:
        """
        time_total=0
        rgb_xy = self.auto_rgb(x,y)
        if direction==1:
            while rgb_xy != rgb_des:
                time_total +=time_delay
                time.sleep(time_delay)
                rgb_xy=self.auto_rgb(x,y)
                print('---计时中:%s s……---'%time_total)
        else:
            while rgb_xy == rgb_des:
                time_total +=time_delay
                time.sleep(time_delay)
                rgb_xy=self.auto_rgb(x,y)
                print('---计时中:%s s……---'%time_total)
        return time_total

if __name__ == '__main__':
    auto().auto_rgb(x=1588,y=107)



