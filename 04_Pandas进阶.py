import pandas as pd
import numpy as np


# 1.读取cSV文件，获取数据.
#参数解释：参1：文件路径，参2：分隔符，参3：读取的列名.
# df = pd.read_csv('./stock_day.csv',usecols=['open','high','close','low'])
# print(df)

# 2.把读取到的数据，写入文件中
# df[:10].to_csv('./my_file1.csv',sep=',',index=False)
# print("succee1")

# 3.特殊的csv文件 -> tsv文件
# df[:5].to_csv('./my_file2.tsv',sep='\t',index=True)
# print("succee1")

# 4.读取tsv文件
# 参1：文件路径，参2：分隔符，参3：把索引为0的列（第1列）设置为索引。
# df2 = pd.read_csv('./my_file2.tsv',sep='\t',index_col=0)
# print(df2)



# # 1.读取json文件
# # 参1：文件路径，参2：读取的格式，参3：是否按行读取
# json_df = pd.read_json('./test.json',orient='records',lines=True)
# print(json_df)
#
# # 2.把上述的数据，写道json文件张
# # json_df.to_json('./my_file3.json',orient = 'records')                # 结果为：[{},{},.....]
# json_df.to_json('./my_file3.json',orient = 'records',lines = True)   # 结果为：{} {} {}....逐行形式
# print('写入成功')

df = pd.read_csv('./1960-2019全球GDP数据.csv',encoding='gbk')
print(df)
print('_'*50)

# df2 = df[:5].copy()
# print(df2)
# print('_'*50)
#
# # 新增列
# # 思路1：通过直接 赋值 的方式 新增1列      column,列
# df2['c1'] = 23          # 写法1：固定值
# df2['c2'] = ['lyf','zs','ls','ww','ly']     # 写法2：传入参数
# df2['c3'] = df2.year * 2        # 写法3：通过已有的列（Series）来计算新列的值
# def my_fun1():
#     return 2500
# df2['c4'] = my_fun1()           # 写法4：通过函数来计算新列的值
# print(df2)
# print('_'*50)
#
# # 思路2：通过 assign（）的方式 新增1列
# df3 = df[:5].copy()
#
# # 写法1：通过 assign()函数 -> 新增1列
# # df3.assign(c1 = 23)
# # 写法2：通过assign()函数 -> 新增n列
# df3.assign(
#     c1 = 23,
#     c2 = ['lyf','zs','ls','ww','ly'],
#     c3 = df3.year * 2,
#     c4 = my_fun1()
# )

# df4 = df[:10].copy()
# print(df4)
# print('_'*50)

# # 1.删除行 drop()函数，除非额指定inplace = True，否则不会修改原始数据
# print(df4.drop(index=[0, 2, 4]))                # 不会求改原始数据
# # print(df4.drop(index=[0, 2, 4]),inplace = True) # 会修改原始数据
# print('_'*50)

# # 2.删除列 -> del关键字，会直接修改原始数据
# # del df4['year']
# df4.drop(columns=['country'], inplace=True)
# print(df4)

# # 3.去重
# # 场景1：DataFrame去重 -> 以行做单位比较
# df5 = df[:5].copy()
#
# # 拼接df5 和df5 -> 组合成 有重复数据的DateFrame
# df6 = pd.concat([df5,df5])
# print(df6)
# print('_'*50)
# # DateFrame去重
# print(df6.drop_duplicates())    # 如果设置inplace = True,则会修改原始数据

# # 场景2：Series去重 -> 以 列 做单位比较
# print(df6.country.drop_duplicates())

# df7 = df[:5].copy()
# print(df7)
# print('_'*50)

# # 修改GDP列值
# df7['GDP'] = [1,2,1,66666666,-234]  # 直接修改原数据
# print(df7)

# # 采用replace()替换
# df7.country.replace('美国','USA',inplace=True)
# print(df7)

# # 获取前5条数据
# print(df.head())
# print('_'*50)
#
# # 获取后3条数据
# print(df.tail(3))
# print('_'*50)
#
# # 根据列名获取数据
# print(df['year'])   # 获取year列 -> Series对象
# print('_'*50)
#
# print(df.year)  # 效果同上
# print('_'*50)
#
# print(df[['year', 'country']])  # 获取year和country列 -> DataFrame对象
# print('_'*50)
#
# # 根据 行索引值来获取数据
# print(df[1:5:2])
# print('_'*50)

# # 通过query()函数,结合条件获取
# # 需求：查询中美日三国2015~2019年的数据
# print(df.query('country in ["中共","美国","日本"] and year in [2015,2016,2017,2018,2019]'))
# print('_'*50)
#
# print(df.query('country in ["中共","美国","日本"] and (year >= 2015 and year <= 2019)'))
# print('_'*50)
#
# # 排序
# # 根据 行索引值排序，降序
# print(df.sort_index(ascending=False))
# print('_'*50)
#
# # 根据内容，例如：year降序，一致就根据 GDP降序
# print(df.sort_values(['year', 'GDP'], ascending=False))
# print('_'*50)










