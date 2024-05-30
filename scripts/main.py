#!/usr/bin/env python3

from linear_math import Vector2D, vector_from_dict

if __name__ == "__main__":
    position = vector_from_dict({"x": 2, "y": 3})
    acceleration = Vector2D(0.1, 0)
    velocity = Vector2D(0, 0)

    new_velocity = velocity + acceleration
    new_position = position + new_velocity

    info = {
        "position": position,
        "acceleration": acceleration,
        "velocity": velocity,
        "new_velocity": new_velocity,
        "new_position": new_position,
    }

    for key, value in info.items():
        print(f"{key:12s} => {value}")
