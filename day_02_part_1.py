"""._.                        .__.__                  ._.
   | |    ____________   ____ |__|  |   ___________   | |
   | |   /  ___/\____ \ /  _ \|  |  | _/ __ \_  __ \  | |
    \|   \___ \ |  |_> >  <_> )  |  |_\  ___/|  | \/   \|
    __  /____  >|   __/ \____/|__|____/\___  >__|     ___
    \/       \/ |__|                       \/         """

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from day02input import data

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

print(data[0])
