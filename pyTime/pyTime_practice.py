# FileName : pyTime_practice.py
# Author   : Adil
# DateTime : 2018/7/27 16:17
# SoftWare : PyCharm



import time


# python中时间日期格式化符号：
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
#
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

# 获取时间戳
time1  = time.time()
print(time1)

# 获取本地时间
localTime = time.localtime(time.time())

# 格式化本地时间
localTimeStrs = time.strftime("%Y-%m-%d %H:%M:%S",localTime)

print(localTime)
print(localTimeStrs)


# 计算时间差

import datetime

day1 = datetime.datetime(2018,6,2)
day2 = datetime.datetime(2018,4,16)

# 计算指定时间的间隔
print((day1-day2).days)

# 获取当前时间
nowTime = datetime.datetime.now()
print("nowTime: ",nowTime)

# 当前指定时间
# 获取当前年份
print(nowTime.year)
print(nowTime.day)
print(nowTime.month)
print(nowTime.hour)
print(nowTime.minute)
print(nowTime.second)

# 当前时间往前推29天计算日期,也就是近30天的其实范围
beforeTime = day1 - datetime.timedelta(days=30)

# 往后推就使用 + 号，当然还可以使用 hours（小时） 、minutes(分钟)、seconds(秒）等单位运算。

print("beforeTime: ",beforeTime)

# 结果输出

# 1526451775.666749
# time.struct_time(tm_year=2018, tm_mon=5, tm_mday=16, tm_hour=14, tm_min=22, tm_sec=55, tm_wday=2, tm_yday=136, tm_isdst=0)
# 2018-05-16 14:22:55
# 30
# nowTime:  2018-05-16 14:22:55.670309
# beforeTime:  2018-04-17 14:22:55.670309


import calendar

cal = calendar.month(2018,2)
print(cal)



# 获取当前时间

curTime = datetime.date(2018,7,9)
print("设置当前时间")
print(curTime)


# 获取 前一周 的时间

beforeone = curTime - datetime.timedelta(7)

print("前一周：")
print(beforeone)

beforetwo = beforeone - datetime.timedelta(7)

print("前两周：")
print(beforetwo)

beforethr = beforetwo - datetime.timedelta(7)
print("前三周：")
print(beforethr)

beforefour = beforethr - datetime.timedelta(7)
print("前四周：")
print(beforefour)

beforefive = beforefour - datetime.timedelta(7)
print("前五周：")
print(beforefive)

# beforetwo = curTime - datetime.timedelta(6)
# print("前一周：")
# print(beforeone)


# 计算时间差

curTime1 = datetime.date(2018,5,15)

oldTime = datetime.date(2018,5,14)


print("时间差：")
print((curTime1-oldTime).days)





