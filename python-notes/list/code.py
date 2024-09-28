from functools import cmp_to_key

def f1():
    li = [i*2 for i in range(10)]
    print(li)

    # map is not a list comprehension, but it is a functional programming concept
    # map is not dict !!!!!!!!!
    li2 = list(map(lambda x: x*1.5, range(10)))
    print(li2)
    # li3 = list(map(lambda x: bool(x) == True, li))
    # or just use
    li3 = list(map(bool, li))
    print(li3)
    
    # remeber to call the lambda function
    result = next((x for x in li if (lambda _x : _x == 14)(x)), None)
    print('result:', result, li.index(result))

    # 必须要使用 enumerate 才能获取到 index，并且需要自己传入默认值
    # 或者使用  range(len(li)) ，但是需要手动获取 li[i] 的值
    # resultIndex = next((i for i in range(len(li)) if (lambda _x: _x == 200)(li[i])), -1)
    resultIndex = next((i for i, x in enumerate(li) if (lambda _x: _x ==200)(x)), -1)

    print('resultIndex:', resultIndex, 200 in li)

    li2 = [i * 2 +1 for i in range(10)]
    print(li2)
    li3 = li + li2
    print(li3)
    li.extend(li2)
    print(li, li3 == li, li3 is li) # True False



def f2():
    # input the list as string
    text = input("Enter elements (Space-Separated): ")

    # split the string into list
    li = text.split()
    print('The list is:', li)

def f3():
    n = int(input("Enter the number of elements: "))
    lst = list(map(int, input("Enter elements (Space-Separated): ").split()))[:n]
    print('The list is:', lst)

def f4():
    li = [53,56,6,3,8,9,2,45,67,7,84,4,12]
    # li.sort()
    li2 = sorted(li)
    print(li, li2)
    # zip 返回的是 zip object，需要转换为 list，不然只能遍历一次
    result = list(zip(li, li2))
    # print(list(result))
    print(sorted(result, key = lambda x: x[0]))
    print(result)

def f5():
    li = [1,2,3,4,5]
    # use slice to insert multiple elements
    li[2:2] = [100, 23]

    print(li)

def compare(x, y):
    if x < y:
        return -1
    elif x == y:
        return 0
    else:
        return 1

def f6():
    li = [53, 56, 6, 3, 8, 9, 2, 45, 67, 7, 84, 4, 12]
    # 从 Python 3 开始，cmp 参数被移除了，取而代之的是 key 参数。
    # 所以我们要使用 functools.cmp_to_key 将比较函数转换为 key 函数。
    sorted_li = sorted(li, key=cmp_to_key(compare))
    print(sorted_li)

f5()

f6()