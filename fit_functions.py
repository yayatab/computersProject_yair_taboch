from math import sqrt
import file_handling as file_handling


def avg(z, dy):
    """
     gets the average of a list
    :param z: the list to make the average of
    :type z: list
    :param dy: the differential in y axis
    :type dy: list
    :return: the calculated average
    :rtype: double
    """
    return sum(a / b for a, b in zip(z, dy)) / sum([1 / dyi for dyi in dy])


# multiplies two lists.
mult = lambda x, y: [a * b for a, b in zip(x, y)]


def _gen_chi_square(x, y, dy, a, b):
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
    for xi, yi, dyi in zip(x, y, dy):
        counter = yi - (a * xi + b)
        denominator = dyi
        chi_squared += (counter / denominator)**2
    return chi_squared


def _get_linear_parameters(x, y, dy):
    x_avg = avg(x, dy)
    y_avg = avg(y, dy)
    xy_avg = avg(mult(x, y), dy)
    x_squered_avg = avg(mult(x, x), dy)
    dy_squered_avg = avg(mult(dy, dy), dy)

    N = len(x)

    a = (xy_avg - x_avg * y_avg) / (x_squered_avg - x_avg ** 2)
    da_squared = dy_squered_avg / N * (x_squered_avg - x_avg ** 2)
    b = y_avg - a * x_avg
    db_squared = da_squared * x_squered_avg

    return {'a': a, 'da': sqrt(da_squared), 'b': b, 'db': sqrt(db_squared)}


def fit_linear(results_dict):
    """
    generates the linear fit
    :param results_dict: dict with x_dots, y_dots,x_uncertainties,y_uncertainties,x_name,y_name
    :return: dict with linear parameters and chi_squered and reduced values
    :rtype: dict
    """

    x = results_dict['x_dots']
    y = results_dict['y_dots']
    dx = results_dict['x_uncertainties']
    dy = results_dict['y_uncertainties']

    N = len(x)
    ret_dict = {'linear_parameters': _get_linear_parameters(x, y, dy), 'chi_squared': 0.0, 'chi_squared_reduced': 0.0}
    a = ret_dict['linear_parameters']['a']
    b = ret_dict['linear_parameters']['b']
    ret_dict['chi_squared'] = _gen_chi_square(x, y, dy, a, b)
    ret_dict['chi_squared_reduced'] = ret_dict['chi_squared'] / (N - 2)
    return ret_dict


if __name__ == '__main__':
    print(fit_linear(file_handling.handle_columns(
        'C:\\Users\\user\\PycharmProjects\\computers_for_physicists\\inputOutputExamples\\workingCols\\input.txt')))
    print(fit_linear(file_handling.handle_rows(
        'C:\\Users\\user\\PycharmProjects\\computers_for_physicists\\inputOutputExamples\\workingRows\\input.txt')))
