# 单引号输出一行
print('Hello,Python')


# 如果要输出多行，可以这样'''
print('''Hello
Python,
I'm coming
''')

a = 100
if a > 0:
    print(a)
else:
    print(-a)

# 计算字符数
print(len('中国'))

# 计算字节数
print(len('中国'.encode('utf-8')))

# 格式化字符串，占位符的使用
print('hello %s,你%d月份的水费是 %.2f 元,比上个月提升了20%%' % ('李明', 7, 99.6))

# 数组
arr1 = ['a', 'b', 'c']
arr2 = ['a', 'b', 'c', ['1', 2, 3.1415926]]

for n in arr1:
    print(n, end='')  # 不换行打印

print()

arr1.insert(1, 100)  # 插入
arr1.pop(2)  # 删除
arr1.append('d')  # 附加

for n in arr1:
    print(n)  # 换行打印

# 九九乘法口诀表
for m in range(1, 10):
    for n in range(1, m+1):
        print(str(m)+'*'+str(n)+'='+str(m*n), end=' ')
    print()
