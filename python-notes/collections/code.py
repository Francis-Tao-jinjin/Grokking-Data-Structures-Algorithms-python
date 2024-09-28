from collections import *
import bisect
from itertools import tee

def f1():
    c = Counter()

    # since Counter is a subclass of dict, isinstance(c, dict) returns True
    print(c, type(c),
          isinstance(c, Counter),
          isinstance(c, dict))  # Output: Counter() <class 'collections.Counter'> True True


# 使用元组改善分支代码, 可以避免使用过多的 if-elif-else
# BREAKPOINTS 必须是已经排好序的，不然无法进行二分查找
BREAKPOINTS = (1, 60, 3600, 3600 * 24)
TMPLS = ( # unit, template
    (1, "less than 1 second ago"),
    (1, "{units} seconds ago"),
    (60, "{units} minutes ago"),
    (3600, "{units} hours ago"),
    (3600 * 24, "{units} days ago"),)

def from_now(ts):
    """接收一个过去的时间戳，返回距离当前时间的相对时间文字描述
    """
    if ts < 0:
        raise ValueError("timestamp must be non-negative")
    idx = bisect.bisect(BREAKPOINTS, ts)
    unit, tmpl = TMPLS[idx]
    return tmpl.format(units=ts // unit)

def f2():
    print(from_now(0.5))  # Output: less than 1 second ago
    print(from_now(1))  # Output: 1 seconds ago
    print(from_now(59))  # Output: 59 seconds ago
    print(from_now(60))  # Output: 1 minutes ago
    print(from_now(3600))  # Output: 1 hours ago
    print(from_now(3600 * 24))  # Output: 1 days ago
    print(from_now(3600 * 24 * 2))  # Output: 2 days ago
    print(from_now(3600 * 24 * 365))  # Output: 365 days ago


def f3():
    def old_merge_dict(d1, d2):
        # 因为字典是可被修改的对象，为了避免修改原对象，此处需要复制一个 d1 的浅拷贝
        result = d1.copy()
        result.update(d2)
        return result
    
    user = old_merge_dict({'name': 'Tom', 'age': 20}, {'age': 25, 'gender': 'male'})
    print(user) 
    
    user2 = {**{ 'name': 'Tom', 'age': 20 }, **{ 'age': 23, 'gender': 'male'}}
    print(user2)

    l = [10, 2, 3, 21, 10, 3]
    # 去重但是丢失了顺序
    print(set(l))  # Output: {3, 10, 2, 21}

    ordered_set = OrderedDict.fromkeys(l).keys()
    print(ordered_set, type(ordered_set))  # Output: odict_keys([10, 2, 3, 21]) <class 'odict_keys'>
    print(list(ordered_set))  # Output: [10, 2, 3, 21]

def f4():
    numbers = [1,2,3,4,5]
    numbers = (i*2 for i in numbers)

    numbers_iter1, numbers_iter2 = tee(numbers)

    # for num in numbers:
    #     print(num)
    
    # print('-- 1 --')
    # # 这次循环什么都不会输出，因为迭代器已经枯竭了
    # for num in numbers:
    #     print(num)
    _i = 0
    print('-- 2 --')
    for num in numbers_iter1:
        print(num)
        _i += 1
        if _i == 2:
            break

    # numbers_iter1 会从上次停止的地方继续迭代，所以这里会输出 6，8，10
    print('-- 2.2 --')
    for num in numbers_iter1:
        print(num)

    print('-- 3 --')
    for num in numbers_iter2:
        print(num)

    # tee 对一个 iterator 只能进行两次分裂，产生的两个副本迭代完之后，原 iterator 就会被清空
    # 所以这里的 numbers_iter3 和 numbers_iter4 都是空的，不会输出任何内容
    numbers_iter3, numbers_iter4 = tee(numbers)
    print('-- 4 --')
    for num in numbers_iter3:
        print(num)

    
def f5():
    d = {'a': 1, 'b': 2, 'c': 3}
    del d['a']
    d.pop('a', None)  # 提供 defaultValue 之后不会报错
    print(d)  # Output: {'b': 2, 'c': 3}
    d.update({k:v for k,v in zip(['x','y','z'], [32,54,14])})
    print(d) # Output: {'b': 2, 'c': 3, 'x': 32, 'y': 54, 'z': 14}

    d2 = {k:v for k,v in zip(['i','j','k'], [23,6,90])}
    d2.update(d.fromkeys(['x','y','z'], 0)) # Output: {'i': 23, 'j': 6, 'k': 90, 'x': 0, 'y': 0, 'z': 0}
    print(d2)

    d_l = list((k, v) for k, v in d.items())
    print(d_l, type(d_l))  # [('b', 2), ('c', 3), ('x', 32), ('y', 54), ('z', 14)] <class 'list'>

    d_t = tuple((f'{k}-{v}', v) for k, v in d.items())
    print(d_t, type(d_t))  # (('b-2', 2), ('c-3', 3), ('x-32', 32), ('y-54', 54), ('z-14', 14)) <class 'tuple'>


def f6():
    s = set([1,2,3])
    s.add(4)
    s.update([5,6])
    print(s)  # Output: {1, 2, 3, 4, 5, 6}

    s.remove(3)
    s.discard(3)  # discard 会忽略不存在的元素，remove 会抛出异常
    print(s)  # Output: {1, 2, 4, 5, 6}

    print(4 in s)
    s2 = { 5, 6, 7, 8 }
    print(s2.issubset(s))  # Output: False

    s3 = s.union(s2)
    ss3 = s | s2
    print(s3, ss3, s3 == ss3, s3 is ss3)  # Output: {1, 2, 4, 5, 6, 7, 8}
    s4 = s.intersection(s2)
    print(s4)  # Output: {5, 6}

    s5 = s3.difference(s4)
    s6 = s3 - s4
    print(s5, s6)  # Output: {1, 2, 4, 7, 8} {1, 2, 4, 7, 8}

f6()