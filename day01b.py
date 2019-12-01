"""._.                        .__.__                  ._.
   | |    ____________   ____ |__|  |   ___________   | |
   | |   /  ___/\____ \ /  _ \|  |  | _/ __ \_  __ \  | |
    \|   \___ \ |  |_> >  <_> )  |  |_\  ___/|  | \/   \|
    __  /____  >|   __/ \____/|__|____/\___  >__|     ___
    \/       \/ |__|                       \/         """

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
masses = []
for mass in [(int(mass)/3)-2 for mass in open('day01input.txt', 'r')]:
    while mass > 0:
        masses.append(mass)
        mass = math.floor(mass/3) - 2
print(sum(masses))

