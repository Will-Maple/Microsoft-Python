def calculate_diameter_circle(radius: float) -> float:
    """
    Docstring for calculate_diameter_circle:
        Calculates a circle's diameter from a radius.
    
    :param radius: The radius of the circle you want a diameter for.
    :type radius: float
    returns diameter if radius is zero or greater, but returns -1 to indicate and error if radius is negative
    """
    if radius >= 0:
        diameter = radius*2
        return diameter
    else:
        return -1