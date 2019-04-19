# _*_ encoding:utf-8 _*_
import time, random
import sys
"""
号码构成
1 地址码
　　（身份证前六位）表示编码对象常住户口所在县（市、镇、区）的行政区划代码。1-2位省、自治区、直辖市代码； 3-4位地级市、盟、自治州代码； 5-6位县、县级市、区代码；
2 生日期码
　　（身份证第七位到第十四位）表示编码对象出生的年、月、日，其中年份用四位数字表示，年、月、日之间不用分隔符。例如：1981年05月11日就用19810511表示。
3 顺序码
　　（身份证第十五位到十七位）地址码所标识的区域范围内，对同年、月、日出生的人员编定的顺序号。其中第十七位奇数分给男性，偶数分给女性。
4 校验码
　　（身份证最后一位）是根据前面十七位数字码，按照ISO 7064:1983.MOD 11-2校验码计算出来的检验码。作为尾号的校验码，是由号码编制单位按统一的公式计算出来的，
     如果某人的尾号是0-9，都不会出现X，但如果尾号是10，那么就得用X来代替，因为如果用10做尾号，那么此人的身份证就变成了19位，而19位的号码违反了国家标准，
     并且中国的计算机应用系统也不承认19位的身份证号码。Ⅹ是罗马数字的10，用X来代替10，可以保证公民的身份证符合国家标准。
"""
ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')

def makeNew():
    u''' 随机生成新的18为身份证号码 '''
    t = time.localtime()[0]

    x = '%02d%02d%02d%04d%02d%02d%03d' %(random.randint(10,99),
                                        random.randint(01,99),
                                        random.randint(01,99),
                                        random.randint(t - 80, t - 18),
                                        random.randint(1,12),
                                        random.randint(1,28),
                                        random.randint(1,999))
    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]

    return '%s%s' %(x, LAST[y % 11])

def isTrue(x1):
    u''' 验证身份证号码是否真实号码 '''
#    print u'请输入身份证号码'
#    x1 = raw_input('?')

    xlen = len(x1)
    if xlen != 18 and xlen != 15:
        return u'身份证号码长度错误'

    try:
        if xlen == 18:
            x2 = x1[6:14]
            x3 = time.strptime(x2, '%Y%m%d')
            if x2 < '19000101' or x3 > time.localtime():
                return u'时间错误，超过允许的时间范围'
        else:
            x2 = time.strptime(x1[6:12], '%y%m%d')
    except:
        return u'时间错误，非合法时间'

    if xlen == 18:
        y = 0
        for i in range(17):
            y += int(x1[i]) * ARR[i]

        if LAST[y % 11] != x1[-1].upper():
            return u'验证码错误'

    return u'YES'

def old2new():
    u''' 15位身份证号码转换为18位身份证号码 '''
    print u'请输入15位老身份证号码'
    x1 = raw_input('?')
    if len(x1) != 15:
        return u'身份证号码输入错误，身份证号码长度不为15位'

    oldcard = '%s19%s' %(x1[:6], x1[6:])
    y = 0
    for i in range(17):
        y += int(oldcard[i]) * ARR[i]

    return '%s%s' %(oldcard, LAST[y % 11])
#输入列表，下载到指定文件
def download(idlist):
    fl = open('list.txt', 'w')
    for i in idlist:
        fl.write(i)
        fl.write("\n")
    fl.close()

if __name__ == '__main__':
    idlist = []
 #   print u'请输入所需身份证数量'
#  num_need = int(input())
    num_need = int(sys.argv[1])
    i = 0
    while i< num_need:
        x = makeNew()
        if isTrue(x):
            idlist.append(x)
        i += 1
# 下载到指定的文件夹
    download(idlist)

