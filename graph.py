import math

import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)


def plot_graph(x, y, mul,  y2, x_label):


    fig, ax = plt.subplots(figsize=(14, 6))
    # Change major ticks to show every 10.
    ax.xaxis.set_major_locator(MultipleLocator(1.0 * mul))


    # Change minor ticks to show every 5. (10/5 = 2)
    ax.xaxis.set_minor_locator(AutoMinorLocator(5))

    # Turn grid on for both major and minor ticks and style minor slightly
    # differently.
    ax.grid(which='major', color='#454a52', linestyle='--')
    ax.grid(which='minor', color='#818fa6', linestyle=':')



    # plotting the points
    ax.plot(x, y, drawstyle="steps-mid", color='g')
    ax.set_ylabel('COVID result', color='g')
    # plt.plot(x, y2)

    ax2 = ax.twinx()
    ax2.plot(x, y2, color='r')
    ax2.set_ylabel('Confidence', color='r')

    ax2.yaxis.set_major_locator(MultipleLocator(0.1))
    ax2.yaxis.set_minor_locator(AutoMinorLocator(5))
    ax2.grid(which='major', color='#454a52', linestyle='--')
    ax2.grid(which='minor', color='#818fa6', linestyle=':')

    # naming the x axis
    ax.set_xlabel(x_label)
    # naming the y axis

    # giving a title to my graph
    plt.title('Covid result prediction!')

    # plt.grid(axis='x')

    # function to show the plot
    plt.show()


# import matplotlib.pyplot as plt
# from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
#
# fig, ax = plt.subplots(figsize=(10, 8))
#
# # Set axis ranges; by default this will put major ticks every 25.
# ax.set_xlim(0, 200)
# ax.set_ylim(0, 200)
#
# # Change major ticks to show every 20.
# ax.xaxis.set_major_locator(MultipleLocator(20))
# ax.yaxis.set_major_locator(MultipleLocator(20))
#
# # Change minor ticks to show every 5. (20/4 = 5)
# ax.xaxis.set_minor_locator(AutoMinorLocator(4))
# ax.yaxis.set_minor_locator(AutoMinorLocator(4))
#
# # Turn grid on for both major and minor ticks and style minor slightly
# # differently.
# ax.grid(which='major', color='#CCCCCC', linestyle='--')
# ax.grid(which='minor', color='#CCCCCC', linestyle=':')
# plt.show()