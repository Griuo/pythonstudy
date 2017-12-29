import os
import re
f=open('网页词.txt','r', encoding='UTF-8')
temp=f.read()


#统计函数
def statistic():
    dic={}
##    r='[’‑!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+' #用正值表达式过滤标点符号
##    words=re.sub(r,' ',temp)
##    for i1 in words.split(' '):
    for i in re.split('\W+',temp):
        if not i in dic:
            dic[i]=1
        else: dic[i]+=1
    return dic

#排序函数
def sortword(dic):
    items = dic.items()
    nitems = [(i[1], i) for i in items]
    nitems.sort(reverse=True)
    items = [i[1] for i in nitems]
    print(items[:10:])


sortword(statistic())
