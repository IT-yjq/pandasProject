import random

import pandas as pd
import numpy as np

# s1 = pd.Series([1,2,3,4,5])
# print(s1)
# print('_'*30)
#
# s2 = pd.Series([1,2,3,4,5],index=['A','B','C','D','E'])
# print(s2)
# print('_'*30)
#
# s3 = pd.Series((11,22,33,44))
# print(s3)
# print('_'*30)
#
# s4 = pd.Series({'a':1,'b':2,'c':3})
# print(s4)
# print('_'*30)
#
# s5 = pd.Series(np.arange(5))
# print(s5)
# print('_'*30)

# s6 = pd.Series(data=[0,1,2,3,4,5],index=['A','B','C','D','E','F'])
# s6 = pd.Series(data=[i for i in range(6)],index=[i for i in 'ABCDEF'])
# print(s6)
#
#
#
#
# print('_'*30)
# print(s6.index)
#
# print('_'*30)
# print(s6.values)
#
 # print('_'*30)
# print(s6['D'])
#
# s6['D'] = 9
# print(s6)

# # 场景1：通过字典 + 列表的方式实现
# # 1.准备数据集,每个键值对 = 1列数据
# data = {
#     'name':['杨昊','李健','王燕丁'],
#     'gender':['male','male','male'],
#     'age':[10,20,30]
# }
#
# # 2.把上述的数据集，封装成DataFrame对象
# df1 = pd.DataFrame(data=data)
#
# # 3.打印
# print(df1)
# print('_'*30)
#
#
# # 场景2：通过列表 + 元组/列表的方式实现
# # 1.准备数据集,每个元组 = 1行数据
# info = [
#     ('刘亦菲','女',39),
#     ('张三','男',99),
#     ('李四','女',88),
# ]
#
# # 2.把上述的数据集，封装成DataFrame对象
# df2 = pd.DataFrame(data=info,columns=['name','gender','age'])
#
# # 3.打印
# print(df2)
# print('_'*30)
#
# # 场景3：通过Numpy的ndarray -> pandas DATaFrame的方式实现
# # 1.创建numpy的ndarray对象
# arr1 = np.arange(12).reshape(3,4)
# print(arr1)
#
# # 2.把上述的数据集，封装成DataFrame对象
# df3 = pd.DataFrame(data=arr1,columns=['a','b','c','d'])
# print(df3)
# print('_'*30)
#
#
#
# 1.生成10名同学，5门功课的成绩，成绩范围：40~100
score_df = pd.DataFrame(np.random.randint(40,101,(10,5))) # 10行5列，包左不包右

# 2.修改DataFrame对象的 列名 和 索引 列值
column_names = ['语文','数学','英语','物理','体育']
index_names = ['同学' + str(i) for i in range(score_df.shape[0])]

# 3.具体的修改DataFrame对象 列名 和 索引值的动作
score_df.columns = column_names
score_df.index = index_names

# 4.打印修改后的结果
print(score_df)
print('_'*30)

dates = pd.DataFrame(['2024-09-01', '2024-09-02', '2024-09-03'],dtype='datetime64[ns]')
print(dates)
print('_'*30)
print(dates.dtypes)
print('_'*30)

start_date = pd.to_datetime('2024-09-01')
end_date = pd.to_datetime('2024-09-05')
delta = end_date - start_date
print(delta)
print(type(delta))
print('_'*30)

categories = pd.Series(['apple', 'banana', 'apple', 'orange'], dtype='category')
print(categories)













