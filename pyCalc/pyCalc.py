# FileName : pyCalc.py
# Author   : Adil
# DateTime : 2018/8/6 16:49
# SoftWare : PyCharm


# 年龄分布
# addList = [24568736,3404680,32836153,42744103,20825054,9510042,2036980,371273]
# 求和所得： 136297021

# addList = [24568736,3404680,32836153,42744103,20825054,9510042,2036980,467484]
# 求和所得： 136393232


# 注册时长分布
# addList = [35,10638464,13970761,16485896,45304421,33558581,16338863]
# 求和所得： 136297021

# 骑行时长分布
# addList = [49767650,22056750,6456038,5070883,4485527,3969424,44490749]
# 求和所得： 136297021

# 去除异常数据

addList = [22056750,6456038,5070883,4485527,3969424,44490749]



def getSum(addendRegister):
    sum = 0
    for addend in addendRegister:
        sum += addend
    print("求和所得：",sum)
    return sum



def getPercent(memberRegister,denominator):   # 分子、分母

    percentList = []
    for member in memberRegister:
        # 方式1  格式化为float ，然后 处理成%格式， 需要对分子/分母 * 100如下，
        percentList.append('{:.2f}%'.format(member/denominator*100))

    print("所求百分比为：",percentList)


if __name__=='__main__':

    # 求和
    sum = getSum(addList)

    # 求百分比
    getPercent(addList,sum)















