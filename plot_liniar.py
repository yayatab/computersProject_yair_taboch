import matplotlib.pyplot as plt
import file_handling
import fit_functions


def plot_data(data):
    plt.figure(1)
    x = data['x_dots']
    y = data['y_dots']
    dx = data['x_uncertainties']
    dy = data['y_uncertainties']
    plt.xlabel(data['x_name'])
    plt.ylabel(data['y_name'])
    plt.errorbar(x, y, yerr=dy, xerr=dx, fmt='b+')


def plot_line(linear_params, data):
    x = data['x_dots']
    fy = [linear_params['a'] * xi + linear_params['b'] for xi in x]
    plt.plot(x, fy, 'r-')

def show():
    plt.show()

def save_fig(file_name='linear_fit', file_type='svg'):
    plt.savefig(fname=file_name + '.' + file_type, format=file_type)


if __name__ == '__main__':
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
    # plt.axis([0, 6, 0, 20])
    # plt.show()
    # plt.close()
    # .errorbar(x, y, yerr=None, xerr=None
    file_name = 'C:\\Users\\user\\PycharmProjects\\computers_for_physicists\\inputOutputExamples\\workingCols\\input.txt'
    data = file_handling.handle_columns(file_name)
    x = data['x_dots']
    y = data['y_dots']
    dx = data['x_uncertainties']
    dy = data['y_uncertainties']
    plt.xlabel(data['x_name'])
    plt.ylabel(data['y_name'])
    plt.errorbar(x, y, yerr=dy, xerr=dx, fmt='b+')
    linear_params = fit_functions.fit_params_to_linear(data)['linear_parameters']
    fy = [linear_params['a'] * xi + linear_params['b'] for xi in x]
    plt.plot(x, fy, 'r-')
    plt.savefig(fname='linear_fit.svg', format='svg')
    plt.show()
