# Decorators

### Python 中的装饰器

装饰器（Decorators）是 Python 提供的一种简便工具，用于在不改变函数或类定义的情况下，增强或修改其功能。装饰器本质上是一个返回函数的高阶函数。

### 1. 基本的装饰器用法

一个简单的装饰器例子：

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

输出：

```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

### 2. 带参数的装饰器

处理带参数的函数：

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

输出：

```
Before the function call
Hello, Alice!
After the function call
```

### 3. 带参数的装饰器工厂

用来创建能够接受参数的装饰器：

```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

输出：

```
Hello, Alice!
Hello, Alice!
Hello, Alice!
```

### 4. 类装饰器

可以使用类来实现装饰器：

```python
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before the function call")
        result = self.func(*args, **kwargs)
        print("After the function call")
        return result

@MyDecorator
def say_hello():
    print("Hello!")

say_hello()
```

输出：

```
Before the function call
Hello!
After the function call
```

### 常用内置装饰器

1. **@staticmethod**

    将方法标记为静态方法，不需要类实例就可以调用。

    ```python
    class MyClass:
        @staticmethod
        def my_static_method():
            print("This is a static method.")

    MyClass.my_static_method()
    ```

2. **@classmethod**

    将方法标记为类方法，第一个参数是类本身。

    ```python
    class MyClass:
        @classmethod
        def my_class_method(cls):
            print(f"This is a class method of {cls}.")

    MyClass.my_class_method()
    ```

3. **@property**

    将方法转换为属性，可以访问方法而不需要调用它。

    ```python
    class MyClass:
        def __init__(self, value):
            self._value = value

        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, new_value):
            self._value = new_value

    obj = MyClass(10)
    print(obj.value)  # 10
    obj.value = 20
    print(obj.value)  # 20
    ```

4. **@functools.wraps**

    用于修饰一个装饰器函数，确保被装饰的函数保留原函数的元数据（如名称、注释文档等）。

    ```python
    from functools import wraps

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Before the function call")
            result = func(*args, **kwargs)
            print("After the function call")
            return result
        return wrapper

    @my_decorator
    def say_hello():
        """A simple greeting function."""
        print("Hello!")

    print(say_hello.__name__)  # say_hello
    print(say_hello.__doc__)   # A simple greeting function.
    ```

### 链式装饰器

你可以对同一个函数应用多个装饰器：

```python
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()
```

输出：

```
Decorator 1
Decorator 2
Hello!
```

### 小结

装饰器是一种强大且灵活的功能，用于增强函数和类的方法。通过适当使用，可以编写出更清晰、更简洁的代码。此外，Python 提供了一些常用的内置装饰器，如 `@staticmethod`、`@classmethod` 和 `@property`，这些装饰器极大地简化了面向对象编程的某些常见模式。


## 使用装饰器时需要注意的作用域问题：
在 Python 中，变量的作用域分为四种：局部作用域（Local）、嵌套作用域（Enclosing）、全局作用域（Global）和内置作用域（Built-in），简称为 LEGB 规则。

### 解释

1. **局部作用域（Local）**：函数内部定义的变量。
2. **嵌套作用域（Enclosing）**：嵌套函数的外部函数中定义的变量。
3. **全局作用域（Global）**：模块级别定义的变量。
4. **内置作用域（Built-in）**：Python 内置的名字，比如 `len`、`print` 等。

### 代码中的作用域

在你的代码中：

```python
def repeat(num_times):
    count = 0
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            nonlocal count  # nonlocal is used to modify a variable in the enclosing scope
            count += 1
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat
```

- `num_times` 是 `repeat` 函数的参数，属于 `repeat` 函数的局部作用域。
- `count` 是 `repeat` 函数内部定义的变量，属于 `repeat` 函数的局部作用域。
- `decorator_repeat` 和 `wrapper` 是嵌套函数。

### 为什么 `count` 需要 `nonlocal`

- `count` 变量在 `repeat` 函数中定义，并在 `wrapper` 函数中被修改。
- 如果不使用 `nonlocal` 关键字，`count` 在 `wrapper` 函数中会被认为是一个新的局部变量，而不是 `repeat` 函数中的那个 `count` 变量。
- 使用 `nonlocal` 关键字可以告诉 Python，`count` 变量是嵌套作用域中的变量，而不是局部变量。

### 为什么 `num_times` 不需要 `nonlocal`

- `num_times` 是 `repeat` 函数的参数，属于 `repeat` 函数的局部作用域。
- 在 `wrapper` 函数中访问 `num_times` 时，Python 会按照 LEGB 规则查找变量，首先在 `wrapper` 函数的局部作用域中查找，然后在 `decorator_repeat` 函数的局部作用域中查找，最后在 `repeat` 函数的局部作用域中查找。
- 因为 `num_times` 只是在 `wrapper` 函数中被访问，而不是被修改，所以不需要使用 `nonlocal` 关键字。

### 总结

- `count` 需要使用 `nonlocal` 关键字，因为它在嵌套函数中被修改。
- `num_times` 不需要使用 `nonlocal` 关键字，因为它只是被访问，而不是被修改。

### 示例代码

```python
def repeat(num_times):
    count = 0
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            nonlocal count  # nonlocal is used to modify a variable in the enclosing scope
            count += 1
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat
```

通过这种方式，你可以理解为什么 `count` 需要使用 `nonlocal` 关键字，而 `num_times` 不需要。