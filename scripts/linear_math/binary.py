from .spec import VectorDict


def add(a: VectorDict, b: VectorDict) -> VectorDict:
    """
    Add two vectors.

    :param a: The first vector.
    :param b: The second vector.
    :return: The resulting vector from the addition.
    """
    return {"x": a["x"] + b["x"], "y": a["y"] + b["y"]}


def subtract(a: VectorDict, b: VectorDict) -> VectorDict:
    """
    Subtract vector b from vector a.

    :param a: The first vector.
    :param b: The second vector.
    :return: The resulting vector from the subtraction.
    """
    return {"x": a["x"] - b["x"], "y": a["y"] - b["y"]}


def multiply(a: VectorDict, b: VectorDict) -> VectorDict:
    """
    Multiply two vectors component-wise.

    :param a: The first vector.
    :param b: The second vector.
    :return: The resulting vector from the multiplication.
    """
    return {"x": a["x"] * b["x"], "y": a["y"] * b["y"]}


def divide(a: VectorDict, b: VectorDict) -> VectorDict:
    """
    Divide vector a by vector b component-wise.

    :param a: The first vector.
    :param b: The second vector.
    :return: The resulting vector from the division.
    :raises ZeroDivisionError: If any component of b is zero.
    """
    if b["x"] == 0 or b["y"] == 0:
        raise ZeroDivisionError("Cannot divide by a vector with zero components")

    return {"x": a["x"] / b["x"], "y": a["y"] / b["y"]}


def scale(a: VectorDict, ratio: float) -> VectorDict:
    """
    Scale vector a by a given ratio.

    :param a: The vector to scale.
    :param ratio: The ratio to scale the vector by.
    :return: The resulting scaled vector.
    """
    return {"x": a["x"] * ratio, "y": a["y"] * ratio}


def cross(a: VectorDict, b: VectorDict) -> float:
    """
    Calculate the cross product of vectors a and b.

    :param a: The first vector.
    :param b: The second vector.
    :return: The cross product as a scalar.
    """
    return a["x"] * b["y"] - a["y"] * b["x"]


def dot(a: VectorDict, b: VectorDict) -> float:
    """
    Calculate the dot product of vectors a and b.

    :param a: The first vector.
    :param b: The second vector.
    :return: The dot product as a scalar.
    """
    return a["x"] * b["x"] + a["y"] * b["y"]
