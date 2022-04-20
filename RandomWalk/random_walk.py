"""
Random Walk scatterplot visualization

Original Random Walk visualization and code from the
Eric Matthes' book _Python 3 Crashkurs_, 2.
Auflage, No Starch Press (2020). www.dpunkt.plus

https://github.com/ehmatthes/pcc_2e/

"""
__credits__ = "Eric Matthes"

from random import choice
from timeit import timeit

class RandomWalk:
    """RandomWalk constructor"""

    def __init__(self, points=5000):
        """Initilizes the RandomWalk"""

        self.points = points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculates the Walk"""

        while len(self.x_values) < self.points:

            x_direction = choice([1])
            x_distance = choice([1])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice(range(0,100))
            y_step = y_direction * (y_distance / 100)

            # If no forward step, then abandon
            if x_step == 0 and y_step == 0:
                continue

            # Add new step to last point in series
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

