# -*- coding: utf-8 -*-
from time import sleep
from copy import deepcopy
 
WORLD_HIGH = 20 #世界长度
WORLD_WIDE = 40 #世界宽度
ALIVE_CON = 3 #复活条件
KEEP_CON = 2  #保有条件
 
class Cell(object):
    '''细胞对象'''
    def __init__(self, pos):
        '''自身坐标x,y, 已经是否还存活'''
        self.point, self.is_alive = pos, False
        self.x, self.y = self.point
    
    def setAlive(self):
        self.is_alive = True
        
    def setDied(self):
        self.is_alive = False
        
    def display(self):
        if self.is_alive:
            return '*'
        return ' '
        
    def displayLinux(self):
        '''在linux环境下可以打印黑白块'''
        if self.is_alive:
            return '\033[0;37;47m \033[0m'
        return '\033[0;30;40m \033[0m'
        
class GameManager(object):
    def __init__(self):
        self.world = self.initWorld()
        self.initAliveCell()
     
    def initWorld(self):
        world = []
        for pos_x in range(WORLD_WIDE):
            column = []
            for pos_y in range(WORLD_HIGH):
                column.append(Cell((pos_x, pos_y)))
            world.append(column)
        return world
    
    def initAliveCell(self):
        from random import choice
        for high in self.world:
            for cell in high:
                if choice((0, 1)) == 0:
                    continue
                cell.setAlive()
    
    def getNeighbours(self, cell_obj):
        alive_count = 0
        for x_of in range(-1, 2):
            for y_of in range(-1, 2):
                c_x, c_y = cell_obj.x + x_of, cell_obj.y + y_of
                if ((c_x, c_y) == cell_obj.point) or \
                   (c_x < 0 or c_x >= WORLD_WIDE) or \
                   (c_y < 0 or c_y >= WORLD_HIGH):
                    '''排除自身和越界的点'''
                    continue
                if self.world[c_x][c_y].is_alive:
                    alive_count += 1
        return alive_count
              
    def display(self):
        print('='*WORLD_WIDE) # 等号分割线
        for index in range(WORLD_HIGH):
            print(''.join([high[index].displayLinux() for high in self.world]))
        print('='*WORLD_WIDE)
 
    def gameStart(self):
        while True:
            self.display()
            new_world = deepcopy(self.world)
            for p_x, wide_list in enumerate(self.world):
                for p_y, _ in enumerate(wide_list):
                    current_cell = new_world[p_x][p_y]
                    nei_num = self.getNeighbours(current_cell)
                    if nei_num == ALIVE_CON:
                        current_cell.setAlive()
                    elif nei_num != KEEP_CON:
                        current_cell.setDied()              
            self.world = new_world
            sleep(0.2)
 
if __name__ == '__main__':
    world = GameManager()
    try:
        world.gameStart()
    except KeyboardInterrupt:
        '''防止ctrl+c退出报错'''
        pass