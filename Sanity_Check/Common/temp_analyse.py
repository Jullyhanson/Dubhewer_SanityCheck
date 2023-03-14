import csv

class Temp_Analyse():
    def temp_fenxi(self,log_path):
        with open('temp_result.csv','w',newline='') as tp:
            filednames=['时间','温度']
            csv_writer=csv.DictWriter(tp,fieldnames=filednames)
            csv_writer.writeheader()
            with open(log_path,'r',encoding='UTF-8',errors='ignore') as log:
                for line in log.readlines():
                    if '℃' in line:
                        print(line)
                        time_str=line[13:25]
                        x=line.find('℃')
                        temp_str=line[x-5:x+1]
                        print('时间：',time_str)
                        print('温度：',temp_str)
                        csv_writer.writerows([{'时间':time_str,'温度':temp_str}])

if __name__ == '__main__':
    # Temp_Analyse().temp_fenxi(log_path=r'C:\Users\yuanjiajia\Desktop\test.log')
    Temp_Analyse().temp_fenxi(log_path=r'C:\Users\yuanjiajia\Desktop\20221230.log')