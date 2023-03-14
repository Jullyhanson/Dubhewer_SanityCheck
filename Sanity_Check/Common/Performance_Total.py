import os,time,pyautogui,psutil,GPUtil
from Common import File_Tool,Auto_Tool
from pyecharts import options as opts
from pyecharts.charts import Line

current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目根路径
per_path = current_path +'\\性能'

class Recon_Total():
    def Get_Performance(self):
        """
        yjj add CPU and GPU
        :return:
        """
        # 获取CPU占有率
        cpu_res = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent

        # 获取GPU性能
        Gpus = GPUtil.getGPUs()
        for gpu in Gpus:
            gpu_memoryTotal = round((gpu.memoryTotal) / 1024)
            gpu_memoryUsed = round((gpu.memoryUsed) / 1024, 2)
        time.sleep(1)
        gpu = round(gpu_memoryUsed / gpu_memoryTotal * 100, 2)
        a = [gpu_memoryUsed, gpu_memoryTotal, gpu, cpu_res, mem]

        return a

    def Performance_Save(self,perf_file):
        """
        yjj add origin
        :param perf_file: 性能记录文档（txt）
        :return:
        """
        performance_array=self.Get_Performance()
        current_time=time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        with open(perf_file,'a+') as file:
            gpu_memoryUsed = str(performance_array[0])
            gpu_memoryTotal = str(performance_array[1])
            gpu =str(performance_array[2])
            cpu_res =str(performance_array[3])
            mem = str(performance_array[4])
            file.writelines('%s 显存总消耗/显存占用/显存占用百分比/cpu百分比/内存百分比: '%current_time)
            file.writelines(('%s %s %s %s %s')%(gpu_memoryTotal,gpu_memoryUsed,gpu,cpu_res,mem))
            file.writelines('\n')

    def Performance_Html(self,txt_file,html_path):
        """
        yjj add origin
        :param txt_file: 形成的性能txt文档
        :return:
        """
        x=File_Tool.File_Handle().perf_txt_handle(txt_file)[0]
        y=File_Tool.File_Handle().perf_txt_handle(txt_file)[0]
        z=File_Tool.File_Handle().perf_txt_handle(txt_file)[0]
        m=File_Tool.File_Handle().perf_txt_handle(txt_file)[0]

        line = Line(init_opts=opts.InitOpts(width="1500"))
        # line()
        line.add_xaxis(x)
        # print (y)
        # line.add_yaxis("cpu占有率",y)
        line.add_yaxis(series_name="CPU占有率", y_axis=z,
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值"),
                                                               opts.MarkPointItem(type_="min", name="最小值"), ]))

        line.add_yaxis(series_name="内存占有率", y_axis=m,
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值"),
                                                               opts.MarkPointItem(type_="min", name="最小值"), ]))

        line.add_yaxis(series_name="GPU占有率", y_axis=y,
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值"),
                                                               opts.MarkPointItem(type_="min", name="最小值"), ]))

        line.set_global_opts(title_opts=opts.TitleOpts(title='性能监测表', ),
                             yaxis_opts=opts.AxisOpts(name="百分比%", type_="value", max_=100), )

        line.render(html_path)


if __name__ == '__main__':
    path =os.path.join(per_path,'jj.txt')
    # Recon_Total().Performance_Save(perf_file=path)
    timestring = time.strftime('%Y-%m-%d', time.localtime())
    html_path =os.path.join(current_path +'\\图表','性能监测总表%s.html'%timestring)
    Recon_Total().Performance_Html(txt_file=path,html_path=html_path)








