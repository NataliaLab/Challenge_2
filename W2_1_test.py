# Test to:
# 1. Write a program that as input accepts a string typed on keyboard and as output it will print this string reversed

x = 'Alice in wonderland'
def inc():
    n = len(x)
    res = ''
    for number in range(n):
        var = n - number - 1
        res = res + x[var]
    return res

def test_answer():
    assert inc() == 'dnalrednow ni ecilA'

