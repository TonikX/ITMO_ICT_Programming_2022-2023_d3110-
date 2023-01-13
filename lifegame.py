import tkinter as tk
import tkinter.messagebox
import threading
import copy

ROWS = 40  # 设置网格行数
COLS = 40  # 设置网格列数
SPACE = 10  # 设置格子边长
root = tk.Tk()
root.title('生命游戏')
root.geometry('{}{}{}'.format(ROWS * 10, 'x', COLS * 10))
list_live = [[0 for i in range(ROWS)] for j in range(COLS)]  # 设置初始生命体存活情况
isSetOver = False  # 当点击(0,0)格子 就开启元胞自动机
a1 = tk.Canvas(root, width=ROWS * 10, height=COLS * 10)


def drawMap():  # 根据元胞的状态进行绘图 用数组状态表示存活状态 1为存活 2为死亡
    global list_live
    global a1
    for i in range(ROWS):
        for j in range(COLS):
            if list_live[i][j] == 0:
                a1.create_rectangle(i * SPACE, j * SPACE, i * SPACE + SPACE, j * SPACE + SPACE, fill='black',
                                    outline='grey', width=3)
            else:
                a1.create_rectangle(i * SPACE, j * SPACE, i * SPACE + SPACE, j * SPACE + SPACE, fill='white',
                                    outline='grey', width=3)


def callback(event):  # 回调函数 用于实时捕捉鼠标左键状态 获取鼠标所在的坐标
    global isSetOver
    global list_live
    x = event.x / SPACE
    y = event.y / SPACE
    i = int(x)
    j = int(y)
    # print (i,j)
    if isSetOver == False:  # isSetOver为false 说明还没有设置完成 将继续设置
        list_live[i][j] = 1
        a1.create_rectangle(i * SPACE, j * SPACE, i * SPACE + SPACE, j * SPACE + SPACE, fill='white', outline='grey',
                            width=3)
        if i == 0 and j == 0:
            isSetOver = True


a1.bind("<Button-1>", callback)  # 将鼠标左键与回调函数绑定


drawMap()  # 初始化细胞存活图
tk.messagebox.showinfo('提示', "规则1：如果细胞周围有3个存活的细胞 存活\n规则2：如果细胞周围有2个存活的细胞 维持不变\n规则3：其他情况 死亡\n点击(0,0)坐标结束设置并开启自动机")

a1.pack()


def getRoundLive(i, j):  # 获取该坐标细胞周围八个位置的邻居存活状态
    num = 0
    global list_live

    if i > 0 and j > 0 and list_live[i - 1][j - 1] == 1: num += 1
    if i > 0 and list_live[i - 1][j] == 1: num += 1
    if i > 0 and j < COLS - 1 and list_live[i - 1][j + 1] == 1: num += 1
    if j > 0 and list_live[i][j - 1] == 1: num += 1
    if j < COLS - 1 and list_live[i][j + 1] == 1: num += 1
    if j > 0 and i < ROWS - 1 and list_live[i + 1][j - 1] == 1: num += 1
    if i < ROWS - 1 and list_live[i + 1][j] == 1: num += 1
    if i < ROWS - 1 and j < COLS - 1 and list_live[i + 1][j + 1] == 1: num += 1

    return num  # 返回存活邻居数量


def life_week():
    num = 0
    global list_live
    list_now = [[0 for i in range(ROWS)] for j in range(COLS)]
    for i in range(ROWS):
        for j in range(COLS):
            num = getRoundLive(i, j)  # 获取邻居存活个数 以判断自身下一时刻的状态
            if 3 == num:
                list_now[i][j] = 1
            elif 2 == num:
                list_now[i][j] = list_live[i][j]
            else:
                list_now[i][j] = 0

    list_live = copy.deepcopy(list_now)  # 将下一时刻的存活状态进行复制


def my_mainloop():
    root.after(1000, my_mainloop)
    if isSetOver:
        life_week()  # 获取下一时刻的元胞存货状态
        drawMap()  # 绘图


root.after(100, my_mainloop())  # 注册回调函数
root.mainloop()
