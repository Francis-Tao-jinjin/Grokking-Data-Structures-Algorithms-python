# `set` in Python

Python 中的 `set` 和 JavaScript 中的 `Set` 非常相似，都是用于存储唯一值的集合。以下是它们的常用方法和属性的对比。

### Python `set` vs JavaScript `Set`

| Python `set`                   | JavaScript `Set`               |
|--------------------------------|--------------------------------|
| `s = set()`                    | `s = new Set()`                |
| `s = {1, 2, 3}`                | `s = new Set([1, 2, 3])`       |
| `s.add(x)`                     | `s.add(x)`                     |
| `s.remove(x)`                  | `s.delete(x)`                  |
| `s.discard(x)`                 | `s.delete(x)`                  |
| `len(s)`                       | `s.size`                       |
| `x in s`                       | `s.has(x)`                     |
| `s.clear()`                    | `s.clear()`                    |
| `s1.union(s2)`                 | `new Set([...s1, ...s2])`      |
| `s1.intersection(s2)`          | `new Set([...s1].filter(x => s2.has(x)))` |
| `s1.difference(s2)`            | `new Set([...s1].filter(x => !s2.has(x)))` |
| `s1.symmetric_difference(s2)`  | `new Set([...s1].filter(x => !s2.has(x)).concat([...s2].filter(x => !s1.has(x))))` |
| `s1.issubset(s2)`              | `[...s1].every(x => s2.has(x))` |
| `s1.issuperset(s2)`            | `[...s2].every(x => s1.has(x))` |
| `for x in s`                   | `for (let x of s)`             |

下面是如何在 Python 和 JavaScript 中使用这些方法的示例：

### Python 示例

```python
# 创建集合
s = set([1, 2, 3])

# 添加元素
s.add(4)

# 移除元素
s.remove(2)  # 如果元素不存在会引发KeyError异常
s.discard(5)  # 如果元素不存在不会引发异常

# 检查元素是否存在
print(3 in s)  # True

# 获取集合的大小
print(len(s))  # 3

# 清空集合
s.clear()
print(s)  # set()

# 联合
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))  # {1, 2, 3, 4, 5}

# 交集
print(s1.intersection(s2))  # {3}

# 差集
print(s1.difference(s2))  # {1, 2}

# 对称差集
print(s1.symmetric_difference(s2))  # {1, 2, 4, 5}

# 子集
print(s1.issubset({1, 2, 3, 4}))  # True

# 超集
print(s1.issuperset({1, 2}))  # True

# 迭代
for x in s1:
    print(x)
```

### JavaScript 示例

```javascript
// 创建集合
let s = new Set([1, 2, 3]);

// 添加元素
s.add(4);

// 移除元素
s.delete(2);  // 如果元素不存在也不会报错

// 检查元素是否存在
console.log(s.has(3));  // True

// 获取集合的大小
console.log(s.size);  // 3

// 清空集合
s.clear();
console.log(s);  // Set {}

// 联合
let s1 = new Set([1, 2, 3]);
let s2 = new Set([3, 4, 5]);
let union = new Set([...s1, ...s2]);
console.log(union);  // Set {1, 2, 3, 4, 5}

// 交集
let intersection = new Set([...s1].filter(x => s2.has(x)));
console.log(intersection);  // Set {3}

// 差集
let difference = new Set([...s1].filter(x => !s2.has(x)));
console.log(difference);  // Set {1, 2}

// 对称差集
let symmetricDifference = new Set([...s1].filter(x => !s2.has(x)).concat([...s2].filter(x => !s1.has(x))));
console.log(symmetricDifference);  // Set {1, 2, 4, 5}

// 子集
console.log([...s1].every(x => s2.has(x)));  // False

// 超集
console.log([...s2].every(x => s1.has(x)));  // False

// 迭代
for (let x of s1) {
    console.log(x);
}
```

这两个集合的数据结构在许多方面是一致的，因此可以类似地进行操作。主要的区别在于语法和一些方法名的不同。