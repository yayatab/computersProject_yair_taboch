from math import sqrt
import file_handling as file_handling

# gets the average of a list
avg = lambda x: sum(x) / len(x)

# multiplies two lists.
mult = lambda x, y: [a * b for a, b in zip(x, y)]


def _gen_chi_square(x, y, dxi, dy, a, b):
    """
    generate the chi square value of the data and the liniar fit.
    let's say that the liniar fit is ax+b.
    :param x: list of x values.
    :type x: list
    :param y: list of y valus
    :type y: list
    :param dx: list of error differential on x axis
    :type dx: list
    :param dy: list of error differential on y axis
    :type dy: list
    :param a:  the coefficient of the linear function
    :type a: float
    :param b:  the constant of the linear fit
    :type b: float
    :return:the chi square value of the data
    :rtype: float
    """
    chi_squared = 0
    for xi, yi,dyi in zip(x, y, dy):
        counter = yi - (a * xi + b)
        denominator = dyi
        chi_squared += (counter / denominator)
    return chi_squared


def _get_linear_parameters(x, y, dy):
    x_avg = avg(x)
    y_avg = avg(y)
    xy_avg = avg(mult(x, y))
    x_squered_avg = avg(mult(x, x))
    y_squered_avg = avg(mult(dy, dy))

    N = len(x)

    a = (xy_avg - x_avg * y_avg) / (x_squered_avg - x_avg ** 2)
    da_squared = y_squered_avg / N * (x_squered_avg - x_avg ** 2)
    b = y_avg - a * x_avg
    db_squared = da_squared * x_squered_avg

    return a, sqrt(da_squared), b, db_squared


def fit_linear(x, y, dx, dy, xname='', yname=''):
    """
    generates the linear fit
    :param x: list of x values.
    :type x: list
    :param y: list of y values
    :type y: list
    :param dx: list of error differential on x axis
    :type dx: list
    :param dy: list of error differential on y axis
    :type dy: list
    :return:
    :rtype:
    """

    N = len(x)
    linear_parameters = _get_linear_parameters(x, y, dy)
    a = linear_parameters[0]
    b = linear_parameters[2]
    chi_squared = _gen_chi_square(x, y, dx, dy, a, b)
    chi_squared_reduced = chi_squared / (N - 2)
    return chi_squared, chi_squared_reduced, linear_parameters


if __name__ == '__main__':
    print(fit_linear(*file_handling.handle_columns(
        'C:\\Users\\user\\PycharmProjects\\computers_for_physicists\\inputOutputExamples\\workingCols\\input.txt')))
    print(fit_linear(*file_handling.handle_rows(
        'C:\\Users\\user\\PycharmProjects\\computers_for_physicists\\inputOutputExamples\\workingRows\\input.txt')))
