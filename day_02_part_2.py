"""._.                        .__.__                  ._.
   | |    ____________   ____ |__|  |   ___________   | |
   | |   /  ___/\____ \ /  _ \|  |  | _/ __ \_  __ \  | |
    \|   \___ \ |  |_> >  <_> )  |  |_\  ___/|  | \/   \|
    __  /____  >|   __/ \____/|__|____/\___  >__|     ___
    \/       \/ |__|                       \/         """

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from day02input import data

datalen = len(data)

def run(data, x, y):
    opdex = 0
    data[1] = x
    data[2] = y
    while data[opdex] != 99:
        if data[opdex] == 1:
            a = data[data[(opdex + 1)]]
            b = data[data[(opdex + 2)]]
            opdex_write = data[opdex + 3]
            if opdex_write > datalen:
                opdex_write = 0
            data[opdex_write] = a + b
        elif data[opdex] == 2:
            a = data[data[(opdex + 1)]]
            b = data[data[(opdex + 2)]]
            opdex_write = data[opdex + 3]
            if opdex_write > datalen:
                opdex_write = 0
            data[opdex_write] = a * b
        opdex += 4

    return data[0]

for x in range(0, 100):
    for y in range(0, 100):
        if run(data[:], x, y) == 19690720:
            print(100 * x + y)
