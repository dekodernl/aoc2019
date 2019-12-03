"""._.                        .__.__                  ._.
   | |    ____________   ____ |__|  |   ___________   | |
   | |   /  ___/\____ \ /  _ \|  |  | _/ __ \_  __ \  | |
    \|   \___ \ |  |_> >  <_> )  |  |_\  ___/|  | \/   \|
    __  /____  >|   __/ \____/|__|____/\___  >__|     ___
    \/       \/ |__|                       \/         """

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from day01data import data
import math

total_mass = 0
for mass in [math.floor(int(mass) / 3) - 2 for mass in data]:
    while mass > 0:
        total_mass += mass
        mass = math.floor(mass / 3) - 2
print(total_mass)
