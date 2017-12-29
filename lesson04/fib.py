print('请输入fib()')
def fib(num):
    lst =[]
    s1=1
    s2=0
    for i in range(1,101):
        s=s1+s2
        lst.append(s)           #将数列加进列表lst
        s1=s2
        s2=s
    print(lst[:num:])           #切片输出
