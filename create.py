import numpy as np


def create(x, y):
    size = (y, x)
    size_real = (size[0] + 2, size[1] + 2)
    img = np.ones(size_real, dtype=np.uint8)
    for i in range(0, size_real[0]):
        img[i, 0] = 0
        img[i, size_real[1] - 1] = 0
    for j in range(1, size_real[1] - 1):
        img[0, j] = 0
        img[size_real[0] - 1, j] = 0
    # np.random.seed(0)
    p = np.array([0.3, 0.06, 0.07, 0.03, 0.05, 0.03, 0.04, 0.05, 0.09, 0.05, 0.06, 0.08, 0.04, 0.05])

    def rand():
        num = np.random.choice(a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], p=p.ravel())
        return num

    for ii in range(1, size_real[0] - 1):
        for jj in range(1, size_real[1] - 1):
            img[ii, jj] = rand()
    return img
