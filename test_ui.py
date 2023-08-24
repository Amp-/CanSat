# import numpy as np
import random

import pyqtgraph as pg

class Test():
    t = list(range(0,1000))
    print(random.sample(t,10))

    plt = pg.plot(random.sample(t, 500), title="Simplest possible plotting example")


