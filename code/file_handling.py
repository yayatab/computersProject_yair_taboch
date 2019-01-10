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
        raise IOError("Input file error: Data lists are not the same length.")

    if not all([_ > 0 for _ in dx]) or not all([_ > 0 for _ in dy]):
        print("Input file error: Not all uncertainties are positive.")
        raise IOError("Input file error: Not all uncertainties are positive.")


def _convert_to_floats(line, start_index=0):
    """
    splits the line by spaces and converts the data to float
    :param line: the line to read the data from
    :param start_index: the first index of the data to convert from
    :return: list of floats
    """
    return [float(f) for f in line.strip().split(' ')[start_index:] if f != '']


def _extract_x_name(line):
    """
    gets the x title from the line if the line starts with the string "x axis"
    :param line:
    :return:
    """
    if line.startswith("x axis"):
        return line[line.index(": ") + 2:].strip()
    return ""


def _extract_y_name(line):
    """
    gets the y title from the line if the line starts with the string "y axis"
    :param line: the line to extract teh data from
    :return:
    """
    if line.startswith("y axis"):
        return line[line.index(": ") + 2:].strip()
    return ""


def handle_rows(file_path):
    """
    reads data from file and returns a tuple with:
        (x, dx, y, dy, x_axis_title, y_axis_title)
    :param file_path: path to the wanted file of the data
    :return: tuple containg lists of the data, the names of the axis
    """
    # creates a funtion that gets a string of dots and converts them to float
    with open(file_path, 'r') as fil:
        lines = fil.readlines()
    x_dots = []
    y_dots = []
    x_uncertainties = []
    y_uncertainties = []
    x_name = ""
    y_name = ""
    for line in lines:

        if line.lower().startswith("x axis"):
            if x_name == "":
                x_name = _extract_x_name(line)
        elif line.lower().startswith("y axis"):
            if y_name == "":
                y_name = _extract_y_name(line)
        elif line.lower().startswith("x "):
            x_dots = _convert_to_floats(line, 1)
        elif line.lower().startswith("y "):
            y_dots = _convert_to_floats(line, 1)
        elif line.lower().startswith("dx "):
            x_uncertainties = _convert_to_floats(line, 1)
        elif line.lower().startswith("dy "):
            y_uncertainties = _convert_to_floats(line, 1)
            continue
    _check_data_validity(x_dots, x_uncertainties, y_dots, y_uncertainties)

    return x_dots, y_dots, x_uncertainties, y_uncertainties, x_name, y_name


def handle_columns(file_path):
    """
    reads data from file and returns a tuple with:
        (x, dx, y, dy, x_axis_title, y_axis_title)
    :param file_path: path to the wanted file of the data
    :return: tuple containg lists of the data, the names of the axis
    """
    with open(file_path, 'r') as fil:
        lines = fil.readlines()

    x_dots = []
    y_dots = []
    x_uncertainties = []
    y_uncertainties = []
    x_name, y_name = "", ""
    line_index = 1
    for line in lines[1:]:
        line_index += 1

        if line == '' or line == '\n':
            break

        tmp = tuple(_convert_to_floats(line))
        if len(tmp) != 4:
            print("Input file error: Data lists are not the same length")
            raise IOError("Input file error: Data lists are not the same length.")
        x, dx, y, dy = tmp
        x_dots.append(x)
        y_dots.append(y)
        x_uncertainties.append(dx)
        y_uncertainties.append(dy)
    for line in lines[line_index:]:
        if x_name == "":
            x_name = _extract_x_name(line)
        if y_name == "":
            y_name = _extract_y_name(line)

    _check_data_validity(x_dots, y_dots, x_uncertainties, y_uncertainties)

    return x_dots, y_dots, x_uncertainties, y_uncertainties, x_name, y_name
