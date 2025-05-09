import numpy as np


def ex1():
    array_1d = np.array([1, 2, 3, 4, 5, 6], dtype=np.uint8)
    array_2d = np.array([[1, 2, 3], [4, 5, 6]])

    print(f"array_1d: {array_1d}, shape: {array_1d.shape}, dtype: {array_1d.dtype}")
    print(f"array_2d: {array_2d}, shape: {array_2d.shape}, dtype: {array_2d.dtype}")


if __name__ == "__main__":
    ex1()
