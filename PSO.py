from swarm import Swarm
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x_max = 4.5
x_min = -4.5

y_max = 4.5
y_min = -4.5

def f(x:float,y:float)->...:
    return (1.5 - x -x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2

if __name__ == "__main__":
    s = Swarm(f, 10, stop=0.1)
    s.initialize()
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    x = [particle.position.x for particle in s.particles]
    y = [particle.position.y for particle in s.particles]
    z = [particle.position.z for particle in s.particles]
    print(z)
    ax.scatter3D(x, y, z, c=z, cmap='plasma')

    # X, Y = np.meshgrid(np.linspace(-1.5, 1.5, 1000), np.linspace(-1.5, 1.5, 1000))
    # Z = f(X, Y)
    # ax.contour3D(X, Y, Z, 50, cmap='viridis')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()
    s.run()

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    x = [particle.position.x for particle in s.particles]
    y = [particle.position.y for particle in s.particles]
    z = [particle.position.z for particle in s.particles]
    print(z)
    ax.scatter3D(x, y, z, c=z, cmap='plasma')
    plt.show()