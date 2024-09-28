from constant import Color
from textwrap import dedent

print(Color.BLACK)  # Output: Color.BLACK

def f1(delta_seconds):
    if delta_seconds < 11 * 24 * 3600:
        return
    
# import dis
# dis.dis(f1)

def f2():
    l = [1, 2, 4, 5, 7]
    print(sum(i % 2 == 0 for i in l))
    print(sum((lambda i: 1 if i % 2 == 0 else 0)(i) for i in l))

    # 类似的三元表达式："Javascript" if 2 > 1 else "Python"
    print(["Python", "Javascript"][2 > 1])

def f3():
    s = (
    "There is something really bad happened during the process. "
    "Please contact your administrator."
    )
    print(s)

    s2 = dedent("""\
    Welcome, today's movie list:
      - Jaw (1975)
      - The Shining (1980)
      - Saw (2004)""")
    print(s2)

    log_line = '"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36" 47632'
    log_line.rsplit(None, 1)

    maxint = float('inf')
    minint = float('-inf')

    # Output: inf -inf <class 'float'> <class 'float'>
    print(maxint, minint, type(maxint), type(minint))
