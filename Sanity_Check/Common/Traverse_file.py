'''
QXX  2022.11.18
遍历文件文件夹并读取文件个数
'''

import os

class file_count():

    def file_count(self,file_path,common_path=r"D:\data\raw"):
        lists = os.listdir(common_path)#遍历common_path
        # print("未经处理的文件夹列表：\n %s \n" %lists)
        #按照key的关键字进行生序排列，lambda入参x作为lists列表的元素，获取文件最后的修改日期
        #最后对lists以文件时间从小到大排列
        lists.sort(key= lambda  x:os.path.getmtime((common_path + "\\"+ x)))
        #获取最新文件的绝对路径，列表中最后一个值，文件夹+文件名
        file_new = os.path.join(common_path, lists[-1])
        # path_list = next(os.walk(raw_path))
        # print("最新文件路径:\n%s"  %file_new)
        #遍历file_new下文件夹
        bottom_document = os.listdir(file_new )
        #将file_new文件夹下的文件名放在列表里，并取列表中[0]的值
        raw_new = os.path.join(file_new, bottom_document[0])

        count=len(os.listdir(raw_new))

        # print('文件张数：',count)
        #打开txt文件
        file_handle = open(file_path,mode = "a+")
        if 'raw' in common_path:
            file_handle.writelines('raw文件张数：%d张 \n' %count)
            file_handle.writelines('\n' )
        else:
            file_handle.writelines('dicom文件张数：%d张\n' % count)
            file_handle.writelines('\n')

        file_handle.close()

        return count


if __name__ == '__main__':
    raw = r"D:\data\raw"
    dicom = r"D:\data\dicom"
    a = file_count().file_count(raw)
    b = file_count().file_count(dicom)
    # print('返回值',a)
    # print(a)
    # print(b)
