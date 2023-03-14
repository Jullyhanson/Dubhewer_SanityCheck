#coding=utf-8
import time,os

# 时间文件命名
timestring = time.strftime('%Y-%m-%d', time.localtime())
current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目根路径
time_file=current_path +'\\result'+'\\Time_total_%s.txt'%timestring

# 设备类型
machine_type='PR'

# 是否开启拍摄重建后的dubheviewer测试
# true:拍摄结束后，进行dubheviewer测试，False:查看后进行dubheviewer测试
close_dubheviewer=True

# 固定时间间隔拍摄（一般温度实验）
Temp_Is=False
Time_during=210

