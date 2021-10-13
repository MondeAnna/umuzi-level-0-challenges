def area_of_a_triangle(a, b, c):
    """area of a triangle calculated
    using Heron's formula
    """
    s = (a + b + c) * 0.5
    radicand = s * (s - a) * (s - b) * (s - c)
    return radicand ** (1 / 2)
