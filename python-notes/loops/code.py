from itertools import accumulate, chain, product
import operator

def f1():    
    # Accumulate the numbers in the list
    numbers = [1, 2, 3, 4, 5]
    accumulated_numbers = list(accumulate(numbers))
    print(accumulated_numbers)

    # the accumulate function can be implemented as such:
    def my_accumulate(iterable, func=operator.add):
        it = iter(iterable)
        total = next(it)
        yield total
        # 由于已经迭代了第一个元素，所以 element 会从第二个元素开始迭代
        for element in it:
            print(f"element: {element}")
            total = func(total, element)
            yield total

    print(list(my_accumulate(numbers)))

    print(list(chain("ABC", [4, 5, 6])))  # ['A', 'B', 'C', 4, 5, 6]

def f2():
    # Cartesian product
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    print(tshirts)

    # for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    #     print(tshirt)

    print(list(product(colors, sizes)))
    for color, size in product(colors, sizes):
        if (color, size) == ('black', 'M'):
            print('Bingo:', color, size)

def f3():
    def even_only(numbers):
        for num in numbers:
            if num % 2 == 0:
                yield num

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(sum(even_only(numbers)))  # 20
    print(list(accumulate(even_only(numbers)))) # [2, 6, 12, 20]


    def get_points(x, y):
        for i in range(x):
            for j in range(y):
                yield i, j

    for point in get_points(3, 4):
        print(point, end=';')
    else:
        print()


class MyIterator:
    def __init__(self, data_sequence):
        self.data_sequence = data_sequence
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data_sequence):
            raise StopIteration
        value = self.data_sequence[self.index]
        self.index += 1
        return value
    
def f4():
    for i in MyIterator([1,2,3,4,5]):
        print(i, end=';')
    else:
        print()

f4()