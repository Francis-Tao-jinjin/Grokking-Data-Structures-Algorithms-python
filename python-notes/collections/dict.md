# `dict` in Python 

Python 中的 `dict`（字典）和 JavaScript 中的 `Map` 以及普通对象（Object）虽然都是用来存储键值对的结构，但在使用时有一些差异。下表列出了 Python 中 `dict` 与 JavaScript 中 `Map` 和对象的常用方法的对比。

### Python `dict` vs JavaScript `Map`

| Python `dict`               | JavaScript `Map`            |
|-----------------------------|-----------------------------|
| `d = {key: value}`          | `m = new Map()`             |
| `d[key] = value`            | `m.set(key, value)`         |
| `value = d[key]`            | `value = m.get(key)`        |
| `key in d`                  | `m.has(key)`                |
| `del d[key]` or `d.pop(key[, default])` | `m.delete(key)`             |
| `len(d)`                    | `m.size`                    |
| `d.keys()`                  | `m.keys()`                  |
| `d.values()`                | `m.values()`                |
| `d.items()`                 | `m.entries()`               |
| `d.clear()`                 | `m.clear()`                 |
| `d.update(other_dict)`      | `m = new Map([...m, ...otherMap])`  |

### Python `dict` vs JavaScript `Object`

| Python `dict`               | JavaScript `Object`         |
|-----------------------------|-----------------------------|
| `d = {key: value}`          | `o = {key: value}`          |
| `d[key] = value`            | `o[key] = value`            |
| `value = d[key]`            | `value = o[key]`            |
| `key in d`                  | `key in o`                  |
| `del d[key]`                | `delete o[key]`             |
| `len(d)`                    | `Object.keys(o).length`     |
| `d.keys()`                  | `Object.keys(o)`            |
| `d.values()`                | `Object.values(o)`          |
| `d.items()`                 | `Object.entries(o)`         |
| `d.clear()`                 | `for (let key in o) delete o[key];` |
| `d.update(other_dict)`      | `Object.assign(o, otherObj)`|

以下是一些如何在 Python 和 JavaScript 中使用这些方法的示例：

### Python 示例

```python
# 创建字典
d = {'a': 1, 'b': 2}

# 添加元素
d['c'] = 3

# 访问元素
print(d['a'])  # 1

# 检查键是否存在
print('b' in d)  # True

# 删除元素
del d['b']

# 获取字典的长度
print(len(d))  # 2

# 获取所有键
print(d.keys())  # dict_keys(['a', 'c'])

# 获取所有值
print(d.values())  # dict_values([1, 3])

# 获取所有项
print(d.items())  # dict_items([('a', 1), ('c', 3)])

# 清空字典
d.clear()
print(d)  # {}
```

### JavaScript Map 示例

```javascript
// 创建 Map
let m = new Map();

// 添加元素
m.set('a', 1);
m.set('b', 2);

// 访问元素
console.log(m.get('a'));  // 1

// 检查键是否存在
console.log(m.has('b'));  // true

// 删除元素
m.delete('b');

// 获取 Map 的大小
console.log(m.size);  // 1

// 获取所有键
console.log(Array.from(m.keys()));  // ['a']

// 获取所有值
console.log(Array.from(m.values()));  // [1]

// 获取所有项
console.log(Array.from(m.entries()));  // [['a', 1]]

// 清空 Map
m.clear();
console.log(m);  // Map {}
```

### JavaScript Object 示例

```javascript
// 创建对象
let o = {a: 1, b: 2};

// 添加元素
o['c'] = 3;

// 访问元素
console.log(o['a']);  // 1

// 检查键是否存在
console.log('b' in o);  // true

// 删除元素
delete o['b'];

// 获取对象的属性个数
console.log(Object.keys(o).length);  // 2

// 获取所有键
console.log(Object.keys(o));  // ['a', 'c']

// 获取所有值
console.log(Object.values(o));  // [1, 3]

// 获取所有项
console.log(Object.entries(o));  // [['a', 1], ['c', 3]]

// 清空对象
for (let key in o) delete o[key];
console.log(o);  // {}
```

通过这些示例可以看到，虽然语法和方法名不同，但 `dict`、`Map` 和 `Object` 都可以完成类似的功能。