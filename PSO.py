
x_max = 4.5
x_min = -4.5

y_max = 4.5
y_min = -4.5

def f(x:float,y:float):
    return (1.5 - x -x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2
