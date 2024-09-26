在 JavaScript 中，`Math` 模块提供了一些常用的方法和属性。在 Python 中，这些功能主要由 `math` 模块提供。下表列出了常用的 JavaScript `Math` 方法和属性以及它们在 Python 中的对应项。

| JavaScript Math    | Python math        |
|--------------------|--------------------|
| `Math.abs(x)`      | `abs(x)`           |
| `Math.acos(x)`     | `math.acos(x)`     |
| `Math.asin(x)`     | `math.asin(x)`     |
| `Math.atan(x)`     | `math.atan(x)`     |
| `Math.atan2(y, x)` | `math.atan2(y, x)` |
| `Math.ceil(x)`     | `math.ceil(x)`     |
| `Math.cos(x)`      | `math.cos(x)`      |
| `Math.exp(x)`      | `math.exp(x)`      |
| `Math.floor(x)`    | `math.floor(x)`    |
| `Math.log(x)`      | `math.log(x)`      |
| `Math.max(a, b, ...)` | `max(a, b, ...)` |
| `Math.min(a, b, ...)` | `min(a, b, ...)` |
| `Math.pow(x, y)`     | `math.pow(x, y)` |
| `Math.random()`      | `random.random()` (需要导入 `random` 模块) |
| `Math.round(x)`      | `round(x)`        |
| `Math.sin(x)`        | `math.sin(x)`     |
| `Math.sqrt(x)`       | `math.sqrt(x)`    |
| `Math.tan(x)`        | `math.tan(x)`     |
| `Math.E`             | `math.e`          |
| `Math.LN2`           | `math.log(2)`     |
| `Math.LN10`          | `math.log(10)`    |
| `Math.LOG2E`         | `math.log(math.e, 2)` |
| `Math.LOG10E`        | `math.log(math.e, 10)` |
| `Math.PI`            | `math.pi`         |
| `Math.SQRT1_2`       | `math.sqrt(1/2)`  |
| `Math.SQRT2`         | `math.sqrt(2)`    |

以下是一些如何在 Python 中使用这些方法和属性的示例：

```python
import math
import random

# 使用 abs() 获取绝对值
print(abs(-5))  # 5

# 使用 math.cos() 计算余弦值
print(math.cos(math.pi / 3))  # 0.5

# 生成一个随机数
print(random.random())  # 介于0和1之间的随机小数

# 使用 math.pow() 计算幂
print(math.pow(2, 3))  # 8.0

# 获取圆周率
print(math.pi)  # 3.141592653589793
```

通过导入 `math` 和 `random` 模块，你可以在 Python 中方便地使用这些与 JavaScript 中 `Math` 对应的功能。