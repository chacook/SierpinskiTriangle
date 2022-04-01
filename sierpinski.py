import random
import matplotlib.pyplot as plt

num_dots = 25000

# initially just the x and y coordinates of vertices of the triangle
x = [-2, 0, 2]
y = [0, 5, 0]

# add a random starting point within the triangle
x.append(0)
y.append(0)

# repeatedly choose a new point that is halfway between 
# the last point and a random vertex of the triangle
while len(x) < num_dots:    
    random_vertex = random.randint(0, 2)
    
    new_x = (x[-1] + x[random_vertex]) / 2
    new_y = (y[-1] + y[random_vertex]) / 2
    
    x.append(new_x)
    y.append(new_y)
    
plt.scatter(x, y, s=0.1)
plt.savefig("triangle.png")
