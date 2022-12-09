#!/usr/bin/python3
# coding=utf-8
# Author : Fan Liu
import numpy as np
import time
def col_hang(mat,i,el):
    '''
    判断一行是否重复
    '''
    if el in mat[i,:]:
        return False
    return True
def col_lie(mat,j,el):
    '''
    判断一列是否重复
    '''
    if el in mat[:,j]:
        return False
    return True
def col_fang(mat,i,j,el):
    '''
    判断一个３×３的矩阵是否重复
    '''
    i_start=i-i%3
    j_start=j-j%3
    fang=[]
    for m in range(i_start,i_start+3):
        for n in range(j_start,j_start+3):
            fang.append(mat[m,n])
    if el in fang:
        return False
    return True
def init():
    '''
    初始化数据
    建立第一个副本
    '''
    mat=np.array([[0,0,2,7,0,0,0,0,0],
                  [0,0,0,0,1,0,8,0,9],
                  [0,5,0,0,0,2,0,6,0],
                  [0,6,0,8,0,0,9,0,4],
                  [1,0,0,0,0,0,0,0,0],
                  [0,3,0,6,0,0,7,0,1],
                  [0,1,0,0,0,3,0,7,0],
                  [0,0,0,0,7,0,5,0,6],
                  [0,0,8,9,0,0,0,0,0]])
    copy={}
    copy[0]=mat.copy()
    return mat,copy
def pos_zero(mat):
    '''
    计算当前数独空缺位置坐标
    '''
    li=[]
    for i in range(9):
        for j in range(9):
            if mat[i,j]==0:
                li.append((i,j))
    return li
def pos_value(li,mat):
    '''
    计算每个空缺位置的可填的数据
    储存为一个列表
    '''
    el={}
    for pos in li:
        i,j=pos
        el[pos]=[]
        for num in range(1,10):
            if col_hang(mat,i,num) & col_lie(mat,j,num) & col_fang(mat,i,j,num):
                el[pos].append(num)
            else:
                pass
    return el
def sort_value(el):
    '''
    对空缺位置的数据长度进行排序
    返回长度最小的位置和数据列表
    '''
    li_value=[]
    pos_value=[]
    for pos in el:
        li_value.append(len(el[pos]))
        pos_value.append(pos)
    index=li_value.index(min(li_value))
    return pos_value[index],el[pos_value[index]]
def main():
    mat,copy=init()
    back_value={}   #储存每个空缺位置填过的数据
    max_index=pos_zero(mat)
    for pos in max_index:
        back_value[pos]=[]
    index=0 #结束的索引，当其等于空缺位置的个数时结束
    n=0     #循环次数
    while index < len(max_index):   
        m=copy[index].copy()
        li=pos_zero(m)
        el=pos_value(li,m)
        pos,value=sort_value(el)
        value=list(set(value)-set(back_value[pos]))
        if len(value)>0:    #可填数据非空时，继续下一个坐标填值
            m[pos]=value[0]
            print(pos,'set:',value[0])
            back_value[pos].append(value[0])
            index+=1
            n+=1
            copy[index]=m
        elif len(value)==0: #可填数据为空时，回溯到上一个坐标
            del copy[index]
            print('return')
            back_value[pos]=[]
            index-=1
            n+=1
        else:   #当index<0时，该数独不正确
            print(mat,'is not right!')
    print(copy[index],n)
if __name__=="__main__":
    begin=time.time()
    main()
    end=time.time()
    print(end-begin)
————————————————
版权声明：本文为CSDN博主「py-d」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_44707179/article/details/103504451