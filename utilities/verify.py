__author__ = 'Andrew'


def is_name_valid(name):
    """
    This method checks whether or not the characters inserted are valid and returns the reason why
    :param name:
    :return:
    """
    if name == "":
        return [False, "No input"]
    else:
        return [True, None]
