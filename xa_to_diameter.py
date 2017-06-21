def xa_to_diameter(xa):
    """
    Convert an array of cross-sectional areas
    to diameters with commensurate units.
    """
    import math
    
    # Compute diameter from area
    diameter = (math.pi * xa**2) / 4

    return diameter
