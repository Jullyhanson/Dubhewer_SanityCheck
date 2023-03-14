# coding=utf-8
import os
import shutil
from PIL import ImageChops
from PIL import ImageGrab
from PIL import Image
from functools import reduce
import time

PATH = lambda p: os.path.abspath(p)

current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目根路径


class GetImage():
    def get_screenshot_by_custom_size(self,start_x,start_y,end_x,end_y,temp_current_image):
        TEMP_FILE_current = PATH(current_path  + temp_current_image)
        box = (start_x, start_y, end_x, end_y)
        TEMP_FILE= ImageGrab.grab(box)
        TEMP_FILE.save(TEMP_FILE_current)

        return self

    # 可判断文件夹是否存在，并保存图像
    def get_image_bysize(self, start_x, start_y, end_x, end_y, image_path, image_name):
        box = (start_x, start_y, end_x, end_y)
        File_path=PATH(current_path+image_path)
        TEMP_FILE = ImageGrab.grab(box)
        if not os.path.exists(File_path):
            print('---文件夹%s不存在，创建该文件夹---'%File_path)
            os.makedirs(File_path)
        TEMP_FILE_current = PATH(File_path+image_name)
        print(os.path.join(File_path+image_name))
        TEMP_FILE.save(TEMP_FILE_current)
        print('截图%s保存成功'%TEMP_FILE_current)


    # def get__custom_size(self, start_x, start_y, end_x, end_y, imagename):
    #     TEMP_FILE = PATH(TEMP_FILE1 + imagename)
    #     # 自定义截取范围
    #    # self.get_screenshot_as_file(TEMP_FILE)
    #     box = (start_x, start_y, end_x, end_y)
    #
    #     image = Image.open(TEMP_FILE)
    #     newImage = image.crop(box)
    #     newImage.save(TEMP_FILE)
    #
    #     return self


    # def write_to_file(self, dirPath, imageName, form="png"):
    #     # 将截屏文件复制到指定目录下
    #     if not os.path.isdir(dirPath):
    #         os.makedirs(dirPath)
    #     shutil.copyfile(TEMP_FILE, PATH(dirPath + "/" + imageName + "." + form))


    # def load_image(self, image_path):
    #     # 加载目标图片供对比用
    #     if os.path.isfile(image_path):
    #         load = Image.open(image_path)
    #         return load
    #     else:
    #         raise Exception("%s is not exist" % image_path)

        # http://testerhome.com/topics/202
    def same_as(self, temp_current,temp_right, temp_compare,percent):
        #对比图片，percent值设为0，则100%相似时返回True，设置的值越大，相差越大
        import math
        import operator

        image1 = Image.open(temp_current)
        image2 = Image.open(temp_right)

        #像素的宽和高
        width = image1.size[0]
        height = image1.size[1]

        histogram1 = image1.histogram()
        histogram2 = image2.histogram()

        differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, \
                                                         histogram1, histogram2)))/len(histogram1))
        # differ = abs((a -b)/a)
        pixNum = width*height
        diff = ImageChops.difference(image1, image2)
        if diff.getbbox() is None:
            print("图片一样")
        else:
            diff.save(temp_compare)
            print("图片不同")

        if differ <= percent*pixNum*0.001:
            return True
        else:
            return False



    # 比较图片
    def compare_images(self, temp_current, temp_right, temp_compare):
        '''
        :param temp_current: 当前运行的图片路径
        :param temp_right: 正确的图片路径
        :param temp_compare: 对比不同图的保存路径
        :return:
        '''
        image_one = Image.open(temp_current)
        image_two = Image.open(temp_right)
        try:
            diff = ImageChops.difference(image_one, image_two)
            if diff.getbbox() is None:
                print("图片一样，测试通过")
                return True
            else:
                diff.save(temp_compare)
                return False
        except ValueError as e:
            text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
                    "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
                    "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
                    "image must match the size of the region.使用2纬的box避免上述问题")
            print("【{0}】{1}".format(e, text))


