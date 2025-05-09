import matplotlib.pyplot as plt
import numpy as np

SIZE = (100, 100)


def ex1():
    array_1d = np.array([1, 2, 3, 4, 5, 6], dtype=np.uint8)
    array_2d = np.array([[1, 2, 3], [4, 5, 6]])

    print(f"array_1d: {array_1d}, shape: {array_1d.shape}, dtype: {array_1d.dtype}")
    print(f"array_2d: {array_2d}, shape: {array_2d.shape}, dtype: {array_2d.dtype}")


def ex2():
    img = np.zeros(SIZE, dtype=np.uint8)
    img[77, 77] = 1
    plt.imshow(img, cmap="grey")
    plt.show()


def ex3():
    img = np.random.randint(0, 256, size=SIZE)
    plt.imshow(img, cmap="gray")
    plt.show()


def ex4(show=False):
    img_normal = np.random.normal(loc=127, scale=1, size=SIZE)
    img_uniform = np.random.randint(0, 256, size=SIZE)
    _, (ax_normal, ax_uniform) = plt.subplots(1, 2)
    if show:
        ax_normal.imshow(img_normal, cmap="grey")
        ax_uniform.imshow(img_uniform, cmap="grey")
        plt.show()
    return img_normal, img_uniform


if __name__ == "__main__":
    ex4()
