print('输出斐波那契数列的前100项')
s1=1
s2=0
for i in range(1,101):
    s=s1+s2
    print(s)
    s1=s2
    s2=s
