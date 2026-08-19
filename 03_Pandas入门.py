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
# # 1.生成10名同学，5门功课的成绩，成绩范围：40~100
# score_df = pd.DataFrame(np.random.randint(40,101,(10,5))) # 10行5列，包左不包右
#
# # 2.修改DataFrame对象的 列名 和 索引 列值
# column_names = ['语文','数学','英语','物理','体育']
# index_names = ['同学' + str(i) for i in range(score_df.shape[0])]
#
# # 3.具体的修改DataFrame对象 列名 和 索引值的动作
# score_df.columns = column_names
# score_df.index = index_names
#
# # 4.打印修改后的结果
# print(score_df)
# print('_'*30)
#
# dates = pd.DataFrame(['2024-09-01', '2024-09-02', '2024-09-03'],dtype='datetime64[ns]')
# print(dates)
# print('_'*30)
# print(dates.dtypes)
# print('_'*30)
#
# start_date = pd.to_datetime('2024-09-01')
# end_date = pd.to_datetime('2024-09-05')
# delta = end_date - start_date
# print(delta)
# print(type(delta))
# print('_'*30)
#
# categories = pd.Series(['apple', 'banana', 'apple', 'orange'], dtype='category')
# print(categories)

df = pd.read_csv('./stock_day.csv')
df.drop(columns=['ma5','ma10','ma20','v_ma5','v_ma10','v_ma20'],axis=0,inplace=True)
print(df)
print('_'*30)

# print(df['open']['2018-02-23'])
#
# print(df.loc['2018-02-27':'2018-02-14',['open','high']])
# print(df.iloc[0:5,0:2])

# df['high'] = 23
# print(df)
# df.open = 1
# print(df)

# # 基于开盘价格做 升序 排序
# print(df.sort_values(by='open',ascending=True))
#
# # 基于开盘价格降序排列，价格一样，基于 当日最高价格（high）降序排列
# print(df.sort_values(by=['open','high'],ascending=[False,False]))
#
# # 按照索引排序
# print(df.sort_index(ascending = True))
#
# # 演示series对象也有sort_index()排序方法
# print(df.open.sort_index(ascending=True))       # 索引升序
#
# print(df.open.sort_values(ascending=False))     # 价格降序

# # 针对于close列值 + 2 处理
# print(df.close.add(2))    # Series对象 和 数值运算，则Series中的每个数值都会和该数字进行运算.
# # df.close + 2        # 效果同上
# print('_'*30)
#
# # 需求1：筛选出 open列值 > 23的数据
# print(df[df.open > 23])
# print('_'*30)
#
# # 需求2：筛选出 open列值 > 23 且 < 24的数据
# print(df[(df.open > 23) & (df.open < 24)])      # 细节：多组判断记得加小括号
# print('_'*30)
# # print(df[(df['open'] > 23) & (df['open'] < 24)])    # 标准写法（有空格的）
# # print('_'*30)
#
# # 可以通过query()函数，优化上述的代码
# print(df.query('open > 23 & open < 24'))
# print('_'*30)
#
# # 固定值的筛选，isin
# # 需求：查询open价格为23.53，23.67价格数据
# # print(df[(df.open == 23.53) | (df.open == 23.67)])
# # print(df.query('open == 23.53 | open == 23.67'))
# print(df[df.open.isin([23.53,23.67])])
# print('_'*30)


# # 针对于 每列（DataFrame对象）进行求和
# print(df.sum())
# print('_'*30)
# # 针对于high列（Series对象）进行求和
# print(df.high.sum())
# print('_'*30)
#





















# 需求：同时获取到 多列的最大值和最小值的差值，列如：open列，close列
# 思路1：分解版
# 1.自定义函数 my_func,接受 某列的数据，计算该列的最大值
def my_func(col):
    return col.max() - col.min()

# 2.通过apply()函数，调用上述的自定义函数，作用到指定的
print(df[['open', 'close']].apply(my_func))
print('_'*30)

# 思路2：合并版，通过lanbda函数实现
print(df[['open', 'close']].apply(lambda col: col.max() - col.min()))
















