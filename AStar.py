from pyamaze import maze,agent,textLabel, COLOR
from queue import PriorityQueue
from timeit import timeit

def h(cell1, cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)
def aStar(m):
    start=(m.rows, m.cols)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))

    open=PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    aPath={}
    while not open.empty():
        currentCell=open.get()[2]
        if currentCell ==(2,13):
            break
        for direction in 'ESNW':
            if m.maze_map[currentCell][direction]==True:
                if direction =='E':
                    nextCell=(currentCell[0], currentCell[1]+1)
                if direction =='W':
                    nextCell=(currentCell[0], currentCell[1]-1)
                if direction =='N':
                    nextCell=(currentCell[0]-1, currentCell[1])
                if direction =='S':
                    nextCell=(currentCell[0]+1, currentCell[1])

                temp_g_score=g_score[currentCell]+1
                temp_f_score=temp_g_score+h(nextCell,(1,1))

                if temp_f_score < f_score[nextCell]:
                    g_score[nextCell]= temp_g_score
                    f_score[nextCell]= temp_f_score
                    open.put((temp_f_score, h(nextCell,(1,1)),nextCell))
                    aPath[nextCell]= currentCell
    fwdPath={}
    cell=(2,13)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(25,25)
    m.CreateMaze(2,13,pattern='v',theme=COLOR.light,loopPercent=100)
    path=aStar(m)

    a=agent(m, footprints=True)
    m.tracePath({a:path})
    l=textLabel(m,'A Star Path Length', len(path)+1)
    t=timeit(stmt='aStar(m)',number=1000, globals=globals())
    textLabel(m,'A* EXECUTION Time',t)

    m.run()
