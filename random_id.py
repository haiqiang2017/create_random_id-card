# _*_ encoding:utf-8 _*_
import time, random
import sys
from datetime import date
import os
from datetime import timedelta
from datetime import datetime

def gennerator(num):

    id = str(state_need)


    id = id + year
    s_day = year + "-01-01"
    date_time = datetime.strptime(s_day, '%Y-%m-%d')
    da = date_time+timedelta(days=num)#月份和日期项
    id = id + da.strftime('%m%d')
    str_tmp = '';
    i = 0
    for i in range(100,301):
        str_tmp = id+ str(i)#，顺序号简单处理
        i = 0
        count = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                     '10': '2'}  # 校验码映射
        result = ''
        for i in range(0, len(str_tmp)):
            count = count + int(str_tmp[i]) * weight[i]
            result = str_tmp + checkcode[str(count % 11)]  # 算出校验码
        download(result,year)


#输入列表，下载到指定文件
def download(result,year):
#    print result;
    path = os.getcwd()+"/"+state_need+"/"+year+"/"
    if not os.path.exists(path):
        os.makedirs(path)
    filename = path+result[10:12]+".txt"
    fl = open(filename, 'a+')
    fl.write(result)
    fl.write("\n")
    fl.close()


if __name__ == '__main__':

 #   print u'请输入所需身份证数量'
#  num_need = int(input())
    idlist = []
    state_need = str(sys.argv[1])
#区号合理化
    if (len(state_need) <6|len(state_need)>6)|state_need.isalpha():
        print "请输入六位区号"
        sys.exit(0)
    age_need = int(sys.argv[2])
#年龄合理化
    year = str(int(datetime.now().year) - int(age_need))
    if (age_need<1|age_need>150):
        print "你输入的年龄太大或者太小"
        sys.exit(0)
    i = 0
    while i<366:
        gennerator(i)
        i+=1;
#    download(idlist,year)
