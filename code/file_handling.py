def _check_data_validity(x, dx, y, dy):
    """
    checks if the following lists are in the same length, and all the list items
    in dx,dy are positives
    :param x: list of the x data points
    :param dx: list of the x data uncertainties points
    :param y: list of the y data points
    :param dy: list of the y data uncertainties points
    """
    lengths = [len(_) for _ in [x, dx, y, dy]]

    if not all([_ == lengths[0] for _ in lengths]):
        print("Input file error: Data lists are not the same length.")
        raise Exception("Input file error: Data lists are not the same length.")

    if not all([_ > 0 for _ in dx]) or not all([_ > 0 for _ in dy]):
        print("Input file error: Not all uncertainties are positive.")
        raise Exception("Input file error: Data lists are not the same length.")


def handle_rows(file_path):
    """
    reads data from file and returns a tuple with:
        (x, dx, y, dy, x_axis_title, y_axis_title)
    :param file_path: path to the wanted file of the data
    :return: tuple containg lists of the data, the names of the axis
    """
    # creates a funtion that gets a string of dots and converts them to float
    convert_to_floats = lambda l: [float(f) for f in l.split(' ')[1:]]
    with open(file_path, 'r') as fil:
        lines = fil.readlines()
    x_dots = []
    y_dots = []
    x_uncertinties = []
    y_uncertinties = []
    x_name = ""
    y_name = ""
    for line in lines:
        if line.startswith("x "):
            x_dots = convert_to_floats(line)
        elif line.startswith("y "):
            y_dots = convert_to_floats(line)
        elif line.startswith("y "):
            x_uncertinties = convert_to_floats(line)
        elif line.startswith("y "):
            y_uncertinties = convert_to_floats(line)
        elif line.startswith("x axis"):
            x_name = line[line.index(":"):]
        elif line.startswith("y axis"):
            y_name = line[line.index(":"):]
        else:
            continue
    _check_data_validity(x_dots, y_dots, x_uncertinties, y_uncertinties)

    return x_dots, y_dots, x_uncertinties, y_uncertinties, x_name, y_name
