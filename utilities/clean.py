__author__ = 'Andrew'


def clean(name):
    """
    Makes the name lowercase and removes the spaces as well
    :param name:
    :return:
    """

    name = name.lower()
    name = name.replace(" ", "")
    return name
