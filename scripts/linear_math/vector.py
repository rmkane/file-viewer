#!/usr/bin/env python3

from typing import Union

from .binary import add, cross, divide, dot, multiply, scale, subtract
from .spec import VectorDict
from .unary import angle, magnitude, normalize


def vector_from_dict(data: VectorDict) -> "Vector2D":
    """
    Convert a dictionary to a Vector2D object.

    :param data: A dictionary with 'x' and 'y' keys representing the vector components.
    :return: A Vector2D object.
    """
    return Vector2D(data["x"], data["y"])


def vector_to_dict(vector: "Vector2D") -> VectorDict:
    """
    Convert a Vector2D object to a dictionary.

    :param vector: A Vector2D object.
    :return: A dictionary with 'x' and 'y' keys representing the vector components.
    """
    return {"x": vector.x, "y": vector.y}


class Vector2D:
    """A class representing a 2D vector."""

    def __init__(self, x: float, y: float):
        """
        Initialize a vector with x and y coordinates.

        :param x: The x-coordinate of the vector.
        :param y: The y-coordinate of the vector.
        """
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        """
        Return a string representation of the vector with 2 decimal places.

        :return: A string representation of the vector.
        """
        return f"({self.x:.2f}, {self.y:.2f})"

    def __eq__(self, other: "Vector2D") -> bool:
        """
        Check if two vectors are equal.

        :param other: The other vector to compare.
        :return: True if the vectors are equal, False otherwise.
        """
        return self.x == other.x and self.y == other.y

    def __add__(self, other: "Vector2D") -> "Vector2D":
        """
        Add another vector to this vector using the + operator.

        :param other: The other vector to add.
        :return: The resulting vector from the addition.
        """
        return self.add(other)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        """
        Subtract another vector from this vector using the - operator.

        :param other: The other vector to subtract.
        :return: The resulting vector from the subtraction.
        """
        return self.subtract(other)

    def __mul__(self, other: Union["Vector2D", float]) -> "Vector2D":
        """
        Multiply this vector by another vector or a scalar using the * operator.

        :param other: The other vector or scalar to multiply by.
        :return: The resulting vector from the multiplication.
        """
        return self.multiply(other)

    def __truediv__(self, other: Union["Vector2D", float]) -> "Vector2D":
        """
        Divide this vector by another vector or a scalar using the / operator.

        :param other: The other vector or scalar to divide by.
        :return: The resulting vector from the division.
        :raises ZeroDivisionError: If any component of the other vector is zero or if dividing by zero.
        """
        return self.divide(other)

    def __neg__(self) -> "Vector2D":
        """
        Negate this vector using the - operator.

        :return: The negated vector.
        """
        return Vector2D(-self.x, -self.y)

    def to_dict(self) -> VectorDict:
        """
        Convert this vector to a dictionary.

        :return: A dictionary with 'x' and 'y' keys representing the vector components.
        """
        return vector_to_dict(self)

    def add(self, other: "Vector2D") -> "Vector2D":
        """
        Add another vector to this vector.

        :param other: The other vector to add.
        :return: The resulting vector from the addition.
        """
        result = add(self.to_dict(), other.to_dict())
        return Vector2D(result["x"], result["y"])

    def subtract(self, other: "Vector2D") -> "Vector2D":
        """
        Subtract another vector from this vector.

        :param other: The other vector to subtract.
        :return: The resulting vector from the subtraction.
        """
        result = subtract(self.to_dict(), other.to_dict())
        return Vector2D(result["x"], result["y"])

    def multiply(self, other: Union["Vector2D", float]) -> "Vector2D":
        """
        Multiply this vector by another vector or a scalar.

        :param other: The other vector or scalar to multiply by.
        :return: The resulting vector from the multiplication.
        """
        if isinstance(other, Vector2D):
            result = multiply(self.to_dict(), other.to_dict())
            return Vector2D(result["x"], result["y"])
        else:
            result = scale(self.to_dict(), other)
            return Vector2D(result["x"], result["y"])

    def divide(self, other: Union["Vector2D", float]) -> "Vector2D":
        """
        Divide this vector by another vector or a scalar.

        :param other: The other vector or scalar to divide by.
        :return: The resulting vector from the division.
        :raises ZeroDivisionError: If any component of the other vector is zero or if dividing by zero.
        """
        if isinstance(other, Vector2D):
            result = divide(self.to_dict(), other.to_dict())
            return Vector2D(result["x"], result["y"])
        else:
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = scale(self.to_dict(), 1 / other)
            return Vector2D(result["x"], result["y"])

    def scale(self, ratio: float) -> "Vector2D":
        """
        Scale this vector by a given ratio.

        :param ratio: The ratio to scale the vector by.
        :return: The resulting scaled vector.
        """
        result = scale(self.to_dict(), ratio)
        return Vector2D(result["x"], result["y"])

    def normalize(self) -> "Vector2D":
        """
        Normalize this vector.

        :return: The normalized vector.
        :raises ValueError: If the vector is a zero vector.
        """
        result = normalize(self.to_dict())
        return Vector2D(result["x"], result["y"])

    def magnitude(self) -> float:
        """
        Calculate the magnitude of this vector.

        :return: The magnitude of the vector.
        """
        return magnitude(self.to_dict())

    def angle(self) -> float:
        """
        Calculate the angle of this vector with respect to the x-axis.

        :return: The angle of the vector in radians.
        """
        return angle(self.to_dict())

    def cross(self, other: "Vector2D") -> float:
        """
        Calculate the cross product of this vector and another vector.

        :param other: The other vector.
        :return: The cross product as a scalar.
        """
        return cross(self.to_dict(), other.to_dict())

    def dot(self, other: "Vector2D") -> float:
        """
        Calculate the dot product of this vector and another vector.

        :param other: The other vector.
        :return: The dot product as a scalar.
        """
        return dot(self.to_dict(), other.to_dict())
