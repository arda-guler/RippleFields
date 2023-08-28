import math
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm

G_PI = math.pi
G_2PI = 2 * math.pi

# redundantly redefine trigonometric funcs. because I can't be bothered typing 'math.' every time
def sin(x, unit="rad"):
    if unit=="deg":
        x = math.radians(x)
    return math.sin(x)

def cos(x, unit="rad"):
    if unit=="deg":
        x = math.radians(x)
    return math.cos(x)

def tan(x, unit="rad"):
    if unit=="deg":
        x = math.radians(x)
    return math.tan(x)

def cot(x, unit="rad"):
    if unit=="deg":
        x = math.radians(x)
    return 1/math.tan(x)

def create_ripples(size, level, smoothing=2, init_wavelength=None, use_numpy=False):
    if type(size) == list:

        # 2D
        if len(size) == 2:
            data = []
            for i in range(size[1]):
                data.append([0] * size[0])

            if not init_wavelength:
                wavelength_x = size[0]
                wavelength_y = size[1]
            else:
                wavelength_x = init_wavelength[0]
                wavelength_y = init_wavelength[1]

            for i in range(level):
                amplitude_x = random.uniform(-1, 1) / (i + 1)**smoothing
                amplitude_y = random.uniform(-1, 1) / (i + 1)**smoothing

                for ex in range(size[0]):
                    for ey in range(size[1]):
                        data[ey][ex] += sin(ex / wavelength_x * G_2PI) * amplitude_x
                        data[ey][ex] += sin(ey / wavelength_y * G_2PI) * amplitude_y

                wavelength_x *= 0.5
                wavelength_y *= 0.5

            plt.imshow(data)
            plt.show()

            if use_numpy:
                import numpy as np
                fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
                X = list(range(size[0]))
                Y = list(range(size[1]))
                X, Y = np.meshgrid(X, Y)
                Z = np.array(data)

                surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
                plt.show()

        # 3D
        elif len(size) == 3:
            pass

    # 1D
    else:
        data = [0] * size
        if not init_wavelength:
            wavelength = size
        else:
            wavelength = init_wavelength
        for i in range(level):
            amplitude = random.uniform(-1, 1) / (i + 1)**smoothing

            for e in range(size):
                data[e] += sin(e/wavelength * G_2PI) * amplitude

            wavelength *= 0.5

        plt.plot(data)
        plt.grid()
        plt.show()

    return data

create_ripples(1000, 8) # 1D
create_ripples([100, 100], 10, 1.8, use_numpy=True) # 2D
