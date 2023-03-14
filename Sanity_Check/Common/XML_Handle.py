import os
import bs4
import time
import traceback

class XML_Handle():
    def __init__(self,config_path,png_path):
        self.file_path = config_path
        self.pngpath=png_path
        # 创建两个字典
        self.fileMap={}
        self.pngMap={}

    def getFile(self,key):
        keyFile,keyValue=key.split('.')
        keyPath=os.path.join(self.file_path,keyFile)+'.aml'
        if keyFile in self.fileMap:
            filename=self.fileMap[keyFile]
        else:
            filename=bs4.BeautifulSoup(open(keyPath,encoding='utf-8'))
            self.fileMap[keyFile]=filename
        return filename,keyValue

    def getPos(self,key_value):
        getfile=self.getFile(key_value)
        PosList=list(getfile[0].find(key=getfile[1]).strings)
        try:
            Posxy=PosList[0].split(',')
            Posx=Posxy[0]
            Posy=Posxy[1]
            return int(Posx),int(Posy)
        except:
            file=open("log.txt",'w')
            current_time=time.strftime("%Y-%m-%d, %H:%M:%S")
            file.write('[ERROR] %s key_value=%s数据读取为空,错误码：%s'%(current_time,key_value,traceback))

    def getValue(self,key_value):
        getFile=self.getFile(key_value)
        # print(getFile)
        # print(type(getFile[0].find(key=getFile[1])))
        account= list(getFile[0].find(key=getFile[1]).strings)[0]
        return account