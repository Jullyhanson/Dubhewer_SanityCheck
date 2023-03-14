import os,shutil
import time,datetime

class Data_handle():

    def data_clear(self,filepath):
        # 需要清空文件夹名称
        dele_dir=['cpu','gpu','image','report','总cpu文档']
        # 遍历脚本路径，获取文件夹名称
        for dirspath,dirsname,filename in os.walk(script_path):
            print('dirsname:',dirsname)
            for dirname in dirsname:
                if dirname in dele_dir:
                    filename=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(os.path.join(script_path,dirname))))
                    modify_time = datetime.datetime.strptime(filename,"%Y-%m-%d %H:%M:%S")
                    time_cha=datetime.datetime.now() - modify_time
                    print('最近修改时间：',modify_time,'时间间隔：%s天'%time_cha)
                    if time_cha.days >= 0:
                        print('清空文件夹%s，重新生成'%dirname)
                        shutil.rmtree(os.path.join(script_path,dirname))
                        os.system(f"attrib -r {os.path.join(script_path,dirname)}")
                        os.makedirs(os.path.join(script_path,dirname))

if __name__ == '__main__':
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    Data_handle().data_clear(filepath=script_path)