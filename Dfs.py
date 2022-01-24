from pyamaze import maze, agent, textLabel, COLOR
from timeit import timeit
def SEARCHDFS(m):
    start=(m.rows, m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    while len(frontier)>0:
        currentCell=frontier.pop()
        if currentCell==(2,13):
            break
        for direction in 'ESNW':
            if m.maze_map[currentCell][direction]==True:
                if direction=='E':
                    NextCell=(currentCell[0],currentCell[1]+1)
                elif direction=='W':
                    NextCell=(currentCell[0],currentCell[1]-1)
                elif direction=='S':
                    NextCell=(currentCell[0]+1, currentCell[1])
                elif direction=='N':
                    NextCell=(currentCell[0]-1, currentCell[1])
                if NextCell in explored:
                    continue
                explored.append(NextCell)
                frontier.append(NextCell)
                dfsPath[NextCell]=currentCell
    fwdPath={}
    cell=(2,13)
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return fwdPath


if __name__=='__main__':
    m=maze(25,25)
    m.CreateMaze(2,13, pattern='v',theme=COLOR.light, loopPercent=100)
    path=SEARCHDFS(m)
    a=agent(m, footprints=True, color= COLOR.red)
    m.tracePath({a:path})

    l=textLabel(m,'DFS Path Length',len(path)+1)
    t=timeit(stmt='SEARCHDFS(m)',number=1000, globals=globals())
    textLabel(m,'DFS EXECUTION Time',t)

    m.run()