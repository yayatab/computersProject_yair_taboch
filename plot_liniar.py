import matplotlib.pyplot as plt
import file_handling
import fit_functions


def plot_data(x, y, dx, dy, x_name, y_name):
    # x = bars['x_dots']
    # y = bars['y_dots']
    # dx = bars['x_uncertainties']
    # dy = bars['y_uncertainties']
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.errorbar(x, y, yerr=dy, xerr=dx, fmt='b+')


def plot_line(a, b, x):
    fy = [a * xi + b for xi in x]
    plt.plot(x, fy, 'r-')


def save_fig(file_name='linear_fit', file_type='svg'):
    plt.savefig(fname=file_name + '.' + file_type, format='file_type')


if __name__ == '__main__':
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
    # plt.axis([0, 6, 0, 20])
    # plt.show()
    # plt.close()
    # .errorbar(x, y, yerr=None, xerr=None
    file_name = 'C:\\Users\\user\\PycharmProjects\\computers_for_physicists\\inputOutputExamples\\workingCols\\input.txt'
    bars = file_handling.handle_columns(file_name)
    x = bars['x_dots']
    y = bars['y_dots']
    dx = bars['x_uncertainties']
    dy = bars['y_uncertainties']
    plt.xlabel(bars['x_name'])
    plt.ylabel(bars['y_name'])
    linear_params = fit_functions.fit_linear(bars)['linear_parameters']
    plt.errorbar(x, y, yerr=dy, xerr=dx, fmt='b+')
    fy = [linear_params['a'] * xi + linear_params['b'] for xi in x]
    plt.plot(x, fy, 'r-')
    plt.savefig(fname='linear_fit.svg', format='svg')
    plt.show()
