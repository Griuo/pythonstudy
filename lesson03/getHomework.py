import os
def gitclone():
    f=open('namelist.txt')
    address=f.readlines()
    #print(address)
    f.close()
    for i in address:
        block=i.split('/')
        print(block[-2])
        if os.path.exists(block[-2])==False:#判断文件是否重复 
            os .mkdir(block[-2])
        os.system('git clone %s %s'%(i[:-1],block[-2])) #clone 至相应文件夹
        f.close()
        watcher(block[-2])
#time为遍历次数 同时对应几个————
def watcher(rootdir,time=0):
    time +=1 #运行一次加1
    list = os.listdir(rootdir)
    for i in range(0,len(list)):
         path = os.path.join(rootdir,list[i])
         if list[i]=='.git'or list[i]=='.gitignore':#过滤无用文件
             continue
         print('----'*time+list[i])  #输出rootdir里的文件及文件夹名
         if os.path.isdir(path):
             watcher(path,time)
#watcher('pythonstudy')
gitclone()
