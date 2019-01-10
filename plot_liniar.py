import matplotlib.pyplot as plt


def plot(x, y, dx, dy, a, b):

    plt.figure(1)
    plt.plot(x, y, 'r')

    plt.subplot(212)
    plt.errorbar(x, y, xerr=0.2, yerr=0.4)
    plt.title("Simplest errorbars, 0.2 in x, 0.4 in y")
    
    pass


if __name__ == '__main__':
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
    plt.axis([0, 6, 0, 20])
    plt.show()
