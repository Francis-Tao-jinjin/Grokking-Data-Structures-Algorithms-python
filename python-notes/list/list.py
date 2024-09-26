def f1():
    li = [i*2 for i in range(10)]
    print(li)

    # map is not a list comprehension, but it is a functional programming concept
    # map is not dict !!!!!!!!!
    li2 = list(map(lambda x: x*1.5, range(10)))
    print(li2)

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

f3()
