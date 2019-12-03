"""._.                        .__.__                  ._.
   | |    ____________   ____ |__|  |   ___________   | |
   | |   /  ___/\____ \ /  _ \|  |  | _/ __ \_  __ \  | |
    \|   \___ \ |  |_> >  <_> )  |  |_\  ___/|  | \/   \|
    __  /____  >|   __/ \____/|__|____/\___  >__|     ___
    \/       \/ |__|                       \/         """

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from day03input import data

def get_moves(data):
    moves = []
    for entry in data:
        if entry[0] == 'L':
            moves.append((-int(entry[1:]), 0))
        if entry[0] == 'R':
            moves.append((int(entry[1:]), 0))
        if entry[0] == 'D':
            moves.append((0, -int(entry[1:])))
        if entry[0] == 'U':
            moves.append((0, int(entry[1:])))
    return moves

def move(pos, move, grid):
    for i in range(0,2):
        for h in range(0, move[i]) if move[i] > 0 else range(move[i], 0):
            pos[i] = pos[i] + int(move[i] / abs(move[i]))
            grid.append(tuple(pos))
    return (pos, grid)

posA, posB, gridA, gridB = [0,0], [0,0], [], []
for moveA in get_moves(data[0]):
    posA, gridA = move(posA, moveA, gridA) 
for moveB in get_moves(data[1]):
    posB, gridB = move(posB, moveB, gridB) 

intersections = list(set(gridA) & set(gridB))

shortest = []
for intersection in intersections:
    A = gridA.index(intersection)
    B = gridB.index(intersection)
    shortest.append(A + B + 2)

print(min(shortest))
