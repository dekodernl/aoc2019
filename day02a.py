"""._.                        .__.__                  ._.
   | |    ____________   ____ |__|  |   ___________   | |
   | |   /  ___/\____ \ /  _ \|  |  | _/ __ \_  __ \  | |
    \|   \___ \ |  |_> >  <_> )  |  |_\  ___/|  | \/   \|
    __  /____  >|   __/ \____/|__|____/\___  >__|     ___
    \/       \/ |__|                       \/         """

#!/usr/bin/env python
# -*- coding: utf-8 -*-
data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,6,23,27,1,5,27,31,1,10,31,35,2,10,35,39,1,39,5,43,2,43,6,47,2,9,47,51,1,51,5,55,1,5,55,59,2,10,59,63,1,5,63,67,1,67,10,71,2,6,71,75,2,6,75,79,1,5,79,83,2,6,83,87,2,13,87,91,1,91,6,95,2,13,95,99,1,99,5,103,2,103,10,107,1,9,107,111,1,111,6,115,1,115,2,119,1,119,10,0,99,2,14,0,0]
data[1] = 12
data[2] = 2
datalen = len(data)
opdex = 0
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

print(">", data)
