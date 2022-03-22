"""
 * Project name(项目名称)：Python_dict字典方法和格式化字符串
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 19:16
 * Version(版本): 1.0
 * Description(描述)：
 keys() 方法用于返回字典中的所有键（key）；
values() 方法用于返回字典中所有键对应的值（value）；
items() 用于返回字典中所有的键值对（key-value）。

copy() 方法所遵循的拷贝原理，既有深拷贝，也有浅拷贝。拿拷贝字典 a 为例，copy() 方法只会对最表层的键值对进行深拷贝，
也就是说，它会再申请一块内存用来存放 {'one': 1, 'two': 2, 'three': []}；
而对于某些列表类型的值来说，此方法对其做的是浅拷贝，也就是说，b 中的 [1,2,3] 的值不是自己独有，而是和 a 共有。

setdefault() 方法用来返回某个 key 对应的 value
dict name.setdefault(key, default value)
说明，dict name 表示字典名称，key 表示键，default value 表示默认值（可以不写，不写的话是 None）。

当指定的 key 不存在时，setdefault() 会先为这个不存在的 key 设置一个默认的 default value，然后再返回 default value。

也就是说，setdefault() 方法总能返回指定 key 对应的 value：
如果该 key 存在，那么直接返回该 key 对应的 value；
如果该 key 不存在，那么先为该 key 设置默认的 default value，然后再返回该 key 对应的 default value。

 """

if __name__ == '__main__':
    scores = {'数学': 95, '语文': 89, '英语': 90}
    print(scores)
    print(scores.keys())
    print(scores.values())
    print(scores.items())
    print(type(scores.keys()))
    print(type(scores.values()))
    print(type(scores.items()))
    scores_key = list(scores.keys())
    print(scores_key)
    print(type(scores_key))

    a = {'数学': 95, '语文': 89, '英语': 90}
    for k in a.keys():
        print(k, end=' ')
    print("\n---------------")
    for v in a.values():
        print(v, end=' ')
    print("\n---------------")
    for k, v in a.items():
        print("key:", k, " value:", v)

    b = a.copy()
    print(b)
    print(id(a), id(b))

    a = {'one': 1, 'two': 2, 'three': [1, 2, 3]}
    b = a.copy()
    # 向 a 中添加新键值对，由于b已经提前将 a 所有键值对都深拷贝过来，因此 a 添加新键值对，不会影响 b。
    a['four'] = 100
    print(a)
    print(b)
    # 由于 b 和 a 共享[1,2,3]（浅拷贝），因此移除 a 中列表中的元素，也会影响 b。
    a['three'].remove(1)
    print(a)
    print(b)

    # 在执行 update() 方法时，如果被更新的字典中己包含对应的键值对，那么原 value 会被覆盖；如果被更新的字典中不包含对应的键值对，则该键值对被添加进去。
    a = {'one': 1, 'two': 2, 'three': 3}
    a.update({'one': 4.5, 'four': 9.3})
    print(a)

    # pop() 和 popitem() 都用来删除字典中的键值对，不同的是，pop() 用来删除指定的键值对，而 popitem() 用来删除一个键值对
    a = {'数学': 95, '语文': 89, '英语': 90, '化学': 83, '生物': 98, '物理': 89}
    print(a)
    a.pop('化学')
    print(a)
    print(a)
    # 删除并返回一个（键，值）对作为 2 元组。
    # 对以 LIFO（后进先出）顺序返回。如果 dict 为空，则引发 KeyError。
    a.popitem()
    print(a)

    a = {'数学': 95, '语文': 89, '英语': 90}
    print(a)
    # key不存在，指定默认值
    a.setdefault('物理', 94)
    print(a)
    # key不存在，不指定默认值
    a.setdefault('化学')
    print(a)
    # key存在，指定默认值
    print(a.setdefault('数学', 100))
    print(a)

    input()
