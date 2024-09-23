import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        z = z ** 2 + c
        if abs(z) > 2:
            return n
    return max_iter

width, height = 800, 800

real_min, real_max = -2, 1
imag_min, imag_max = -1.5, 1.5

mandelbrot_set = np.zeros((width, height))

max_iter = 100

for x in range(width):
    for y in range(height):
        real = real_min + (x / width) * (real_max - real_min)
        imag = imag_min + (y / height) * (imag_max - imag_min)
        c = complex(real, imag)

        mandelbrot_set[y, x] = mandelbrot(c, max_iter)

plt.imshow(mandelbrot_set.T, cmap="hot", extent=[real_min, real_max, imag_min, imag_max])
plt.colorbar()
plt.title("Mandelbrot Set")
plt.show()
