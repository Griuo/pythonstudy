print('输出1到100内的所有质数：')
for i in range(1,101):
    s = 1       #s为判断是否为质数的标志
    if i>3 :
        for j in range(2,i):
            if i%j==0 :
                s=0
        if s==1:
            print(i)
    else :
        print(i)
