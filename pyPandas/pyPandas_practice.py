# FileName : pyPandas_practice.py
# Author   : Adil
# DateTime : 2018/7/27 16:20
# SoftWare : PyCharm

# 数据分析

import pandas as pd
import numpy as np

dates = pd.date_range('20170101',periods=7)
print(dates)
print('--'*16)
df = pd.DataFrame(np.random.rand(7,4),index=dates,columns=list('ABCD'))
print(df)





