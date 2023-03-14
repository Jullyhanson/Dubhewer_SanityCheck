#coding=utf-8
import os,random,unittest,time,HTMLTestRunner_cn
from Common import File_Tool
from Testcase import Test_Mode0,Test_Mode1,Test_Mode2,Test_Mode3,Test_Implant,Test_Preview,Test_CheckVersion,Test_Upload,Test_Pano



# 判断文件夹是否存在，不存在就创建
dir_list=['report',
          'image_PD','image_PD/current','image_PD/diff','image_PD/侧位','image_PD/骨密度','image_PD/手动定点',
          'image_PD/current/1615','image_PD/current/1615ks','image_PD/current/1609','image_PD/current/0808','image_PD/current/pacs','image_PD/current/implants','image_PD/current/拍摄界面截图',
          'image_PD/current/版本号截图','image_PD/current/1615/新建患者截图',
          'image_PR/current/版本号截图',
          'image_PR/current/1615/预览截图/','image_PD/current/1615/预览截图/',
          'image_PR','image_PR/current','image_PR/diff','image_PR/侧位','image_PR/骨密度','image_PR/手动定点',
          'image_PR/current/1615','image_PR/current/1615ks','image_PR/current/1609','image_PR/current/0808','image_PR/current/pacs','image_PR/current/implants',
          'image_PR/current/下载截图','image_PR/current/上传截图',
          'cpu','gpu','result','图表','cpu总文档','性能']
File_Tool.File_Handle().File_exist(Dir_list=dir_list)

suite=unittest.TestSuite()

# 获取当前项目根路径
apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"."))
respath = apk_path+'\\report'
# 自动化执行脚本123

# 软件版本号截图
# Test_CheckVersion.Check_Version().test_1()

current_number = 1

# <=x：表示运行次数x次
while current_number <= 500:
    mode=random.randint(0,3)
    # mode=1
    if mode == 0:
        # 1615快扫
        suite.addTest(unittest.makeSuite(Test_Mode0.Test_Mode0))

    elif mode == 1:
        # 1615高清
        suite.addTest(unittest.makeSuite(Test_Mode1.Test_Mode1))
        # suite.addTest(unittest.makeSuite(Test_Implant.Sancheck_Implant_Test))
        # suite.addTest(unittest.makeSuite(Test_Upload.Upload_Download))

    elif mode == 2:
        # 1609
        suite.addTest(unittest.makeSuite(Test_Mode2.Test_Mode2))

    else :
        # 0808高清
        suite.addTest(unittest.makeSuite(Test_Mode3.Test_Mode3))
    current_number += 1
# 自动化执行脚本2021-04-20

if __name__ == '__main__':
    timestring = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    res =respath+"/Dubhe自动化测试报告%s.html"%(timestring)
    fp = open(res,'wb')
    # 打开一个文件，测llz试报告会写入到这个文件中
    # 生成一个HTMLTestRunner实例1615高清
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,  title="测试结果", description="自动化测试结果czy", retry=1,)
    # runner.run(discover)
    runner.run(suite)
    # 清空缓冲流，确保把所有数据都写到对应的文件中
    fp.flush()
    # 关闭流
    fp.close()


