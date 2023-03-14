import os,time,datetime

class Time_tool():

    def Time_cha(self,time1,time2):
        time_1 =datetime.datetime.strptime(time1,"%Y-%m-%d %H:%M:%S")
        time_2 =datetime.datetime.strptime(time2,"%Y-%m-%d %H:%M:%S")
        time_cha = time_2-time_1
        return time_cha

