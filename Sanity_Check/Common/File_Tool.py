import os

# 获取当前项目根路径
apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

class File_Handle():

    # 判断文件夹列表中的文件夹是否存在，不存在则创建
    def File_exist(self,Dir_list):
        for dir in Dir_list:
            dir_path = os.path.join(apk_path,dir)
            if not os.path.exists(dir_path):
                print('---文件夹"%s"不存在，已创建---'%dir)
                os.makedirs(dir_path)
            else:
                print('---文件夹%s已存在---' % dir)

    def File_save(self,Save_file,Save_content):
        #保存到Save_file文件里
        with open(Save_file,'a+') as f:
            f.write('%s %s %s\n' %(Save_content))

    def perf_txt_handle(self,txt_file):
        """
        yjj_2022.10.14
        :param txt_file: 性能生成的txt文件
        :return:
        """
        x=[] # 时间
        y=[] # 显存占用
        z=[] # cpu
        m=[] # 内存
        with open(txt_file,'r') as file:
            for line in file.readlines():
                per_list=line.strip().split(' ')
                print(per_list)
                x.append(per_list[0])
                y.append(per_list[3])
                z.append(per_list[-2])
                m.append(per_list[-1])

        return x,y,z,m


    def Html_handle(self,txt_filename):
        with open(txt_filename,'r') as file:
            for line in file.readlines():
                performance_per = line.split('\n')
                print(performance_per)

if __name__ == '__main__':
    dir_list = ['report',
                'image_PD', 'image_PD/current', 'image_PD/diff', 'image_PD/侧位', 'image_PD/骨密度', 'image_PD/手动定点',
                'image_PD/current/1615', 'image_PD/current/1615ks', 'image_PD/current/1609', 'image_PD/current/0808',
                'image_PD/current/pacs', 'image_PD/current/implants',
                'image_PR', 'image_PR/current', 'image_PR/diff', 'image_PR/侧位', 'image_PR/骨密度', 'image_PR/手动定点',
                'image_PR/current/1615', 'image_PR/current/1615ks', 'image_PR/current/1609', 'image_PR/current/0808',
                'image_PR/current/pacs', 'image_PR/current/implants',
                'image_PR/current/下载截图', 'image_PR/current/上传截图',
                'cpu', 'gpu', 'result', '图表', 'cpu总文档', '性能']
    # per_path =  os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '\\性能'
    # path =os.path.join(per_path,'jj.txt')
    # File_Handle().perf_txt_handle(path)
    File_Handle().File_exist(dir_list)
