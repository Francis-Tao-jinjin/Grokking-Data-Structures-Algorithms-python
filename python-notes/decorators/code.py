from typing import Any
import time
import functools

def duration(func):
    '''Decorator that prints the duration of the function call'''
    @functools.wraps(func)
    def decorated(*args, **kwargs):
        st = time.time()
        value = func(*args, **kwargs)
        print(f'{func.__name__} took {time.time() - st} seconds')
        return value
    return decorated

def repeat(num_times):
    count = 0
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            nonlocal count # nonlocal is used to modify a variable in the enclosing scope
            count += 1
            for _ in range(num_times):  # 如果我们想修改 num_times 的值，我们依然需要使用 nonlocal 关键字
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat

@duration
@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

# will print 'Hello World' 3 times
greet('World')
print('# greet function name:', greet.__name__)

class MyDecorator:
    def __init__(self, func):
        self.func = func

    # Python 对某个对象是否能通过装饰器（@decorator）形式使用只有一个要求：
    # decorator 必须是一个“可被调用（callable）的对象。
    def __call__(self, *args, **kwargs):
        print('Something is happening before the function is called.')
        self.func(*args, **kwargs)
        print('Something is happening after the function is called.')

@MyDecorator
def say_hello(name):
    print(f'Hello {name}')

say_hello('Jane')

class DelayFunc:
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(f'Waiting {self.duration} seconds before calling {self.func.__name__}')
        time.sleep(self.duration)
        return self.func(*args, **kwds)
    
    def eager_call(self, *args, **kwds):
        print(f'Executing {self.func.__name__} without waiting')
        return self.func(*args, **kwds)
    
def delay_deco(duration):
    return lambda func: DelayFunc(duration, func)

@delay_deco(duration=2)
def farewell(name):
    print(f'?? Goodbye {name}')

farewell.eager_call('Thomas')

@duration
def byeJane():
    farewell('Jane')

byeJane()

print('# byeJane function name:', byeJane.__name__)