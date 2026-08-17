import numpy as np


# arr1 = np.arange(15).reshape(3,5)
# print(arr1)
# print(type(arr1))
# print('-'*30)
#
# arr2 = np.array([2,3,4])
# print(f'arr2:{arr2}')
# print(f'type:{type(arr2)}')
# print('-'*30)
#
# arr3 = np.random.rand(3,5)
# print(arr3)
# print('-'*30)
#
# arr4 = np.random.randint(3,9,size=(3,4))
# print(arr4)
# print('-'*30)
#
# arr5 = np.random.uniform(3,9,size=(3,4))
# print(arr5)
# print('-'*30)
#
# print(arr1.dtype)
# arr6 = arr1.astype(np.int32)
# print(arr6.dtype)
# print('-'*30)
#
# arr7 = np.logspace(0,3,4)
# print(arr7)
# print('-'*30)
#
# arr8 = np.logspace(0,3,4,base=2)
# print(arr8)
# print('-'*30)
#
# arr9 = np.linspace(1,10,4,endpoint=False,dtype=np.int32)
# print(arr9)
# print('-'*30)
#
# arr10 = np.random.randn(3,5)
# print(arr10)
# print('-'*30)
# print(np.ceil(arr10))
# print('-'*30)
# print(np.floor(arr10))
# print('-'*30)
# print(np.rint(arr10))
# print('-'*30)
# print(np.isnan(arr10))
# print('-'*30)
# print(np.multiply(arr10,arr10))
# print('-'*30)
# print(np.divide(arr10,arr10))
# print('-'*30)
# print(np.where(arr10 > 0,1,-1))
# print('-'*30)
#
# arr11 = np.arange(12).reshape(3,4)
# print(arr11)
# print('-'*30)
# print(np.cumsum(arr11))         #返回一个一维数组，每个元素都是之前所有元素的累加和
# print('-'*30)
# print(np.sum(arr11))            #所有元素的和
# print('-'*30)
# print(np.sum(arr11,axis=0))     #数组的按列统计和
# print('-'*30)
# print(np.sum(arr11,axis=1))     #数组的按行统计和
# print('-'*30)
#
# arr12 = np.array([[1,2,1],[2,3,5]])
# print(arr12)
# print('-'*30)
# arr13 = np.unique(arr12)
# print(arr13)
# print('-'*30)
#
# arr14 = np.array([33,11,55,22,44])
# print(arr14)
# print('-'*30)
# arr15 = np.sort(arr14)
# print(arr15)
# print('-'*30)
# arr14.sort()
# print(arr14)


# 行列式一致
arr1 = np.array([[1,2,3],[1,2,3]])
arr2 = np.array([[1,2,3],[1,2,3]])
print(arr1 * arr2)
print('-'*30)
print(np.multiply(arr1,arr2))
print('-'*30)

# 行列式不一致
arr3 = np.array([[1,2,3],[4,5,6]])
arr4 = np.array([[9,8],[6,5],[3,2]])
print(arr3)
print('-'*30)
print(arr4)
print('-'*30)
print(np.dot(arr3,arr4))
print('-'*30)
print(arr3 @ arr4)              # 语法糖
print('-'*30)
print(arr3.dot(arr4))





































