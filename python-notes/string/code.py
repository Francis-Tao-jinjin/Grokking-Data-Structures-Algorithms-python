import typing

# 因为使用了 Iterable 作为参数的类型，所以可以支持文件对象、列表、元组等，而不是只支持列表
def add_ellopsis_gen(comments: typing.Iterable[str], max_length: int = 12):
    for comment in comments:
        if len(comment) > max_length:
            yield comment[:max_length] + '...'
        else:
            yield comment

def f1():
    comments = [
        'This is a very long comment',
        'This is a short comment',
        'This is a comment that is just right'
    ]
    for comment in add_ellopsis_gen(comments):
        print(comment)
    
    print('\n'.join(add_ellopsis_gen(comments)))

def f2():
    with open('comments.txt', 'r') as fp:
        for comment in add_ellopsis_gen(fp):
            print(comment)

f2()