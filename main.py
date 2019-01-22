import matplotlib.pyplot as plt
import file_handling
import fit_functions
import plot_liniar


def fit_linear(file_name):
    data = file_handling.extract_data(file_name)
    plot_liniar.plot_data(data)
    linear_params = fit_functions.fit_params_to_linear(data)['linear_parameters']
    plot_liniar.plot_line(linear_params, data)
    plot_liniar.save_fig()
    plt.show()


if __name__ == '__main__':
    fit_linear(
    'C:\\Users\\user\\PycharmProjects\\computers_for_physicists\\inputOutputExamples\\workingCols\\input.txt')
    fit_linear(
    'C:\\Users\\user\\PycharmProjects\\computers_for_physicists\\inputOutputExamples\\workingRows\\input.txt')
