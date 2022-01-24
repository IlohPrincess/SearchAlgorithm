#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 01:38:09 2021
BFS ALGORITHM
@author:B1397468
"""

from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit

def SEARCHBFS(m):
    start=(m.rows,m.cols)
    frontier=[start]
    explored=[start]
    bfsPath={}
    while len(frontier)>0:
        currentCell=frontier.pop(0)
        if currentCell==(2,13):
            break
        for d in 'ESNW':
            if m.maze_map[currentCell][d]==True:
                if d=='E':
                    NextCell=(currentCell[0],currentCell[1]+1)
                elif d=='W':
                    NextCell=(currentCell[0],currentCell[1]-1)
                elif d=='N':
                    NextCell=(currentCell[0]-1,currentCell[1])
                elif d=='S':
                    NextCell=(currentCell[0]+1,currentCell[1])
                if NextCell in explored:
                    continue
                frontier.append(NextCell)
                explored.append(NextCell)
                bfsPath[NextCell]=currentCell
    fwdPath={}
    cell=(2,13)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(25,25)
    m.CreateMaze(2,13,pattern='v',theme=COLOR.light,loopPercent=100)
    path=SEARCHBFS(m)

    a=agent(m,footprints=True,color= COLOR.blue)
    m.tracePath({a:path})
    l=textLabel(m,'BFS Path ',len(path)+1)
    t=timeit(stmt='SEARCHBFS(m)',number=1000, globals=globals())
    textLabel(m,'BFS EXECUTION Time',t)
    
    
    m.run()