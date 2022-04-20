"""
Random Walk scatterplot visualization

Original Random Walk visualization and code from the
Eric Matthes' book _Python 3 Crashkurs_, 2.
Auflage, No Starch Press (2020). www.dpunkt.plus

https://github.com/ehmatthes/pcc_2e/

"""
__credits__ = "Eric Matthes"

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    how_large = input("How many random steps do you want to draw? (to quit press 'q'): ")

    if how_large == 'q':
        break

    rw = RandomWalk(int(how_large))
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(27,15))
    point_numbers = range(rw.points)
    
    # ax.plot(0,0, linewidth=2, c='green')
    # ax.plot(rw.x_values[-1], rw.y_values[-1], linewidth=2)
    ax.plot(rw.x_values, rw.y_values, c='black', alpha=0.5)
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    plt.show()

