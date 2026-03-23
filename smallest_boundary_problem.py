from matplotlib.patches import Polygon
from copy import deepcopy
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import random
import math


NUMBER_OF_RANDOM_POINTS = 5
NUMBER_OF_POLYGON_POINTS = 5
RADIUS = 5
ITERATIONS = 5000
STEP_SIZE = 0.05

#================================================
#               POINT CLASS
#================================================

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


#================================================
#               INITIALIZE POINTS
#================================================

def initialize_random_points(lo:float, hi: float) -> list[Point]:
    points = []
    
    x = 0.0
    y = 0.0

    x_avg = 0.0
    y_avg = 0.0

    for i in range(NUMBER_OF_RANDOM_POINTS):
        x = random.uniform(lo, hi)
        y = random.uniform(lo, hi)
        x_avg += x
        y_avg += y
        points.append(Point(x,y))

    return points, Point((x_avg/NUMBER_OF_RANDOM_POINTS), (y_avg/NUMBER_OF_RANDOM_POINTS))

def initialize_polygon(center_point: Point, radius: int) -> list[Point]:
    polygon = []
    
    x = 0.0
    y = 0.0

    angles = sorted([random.uniform(0, 2 * math.pi) for i in range(NUMBER_OF_POLYGON_POINTS)])
    angles.reverse()

    for i in range(NUMBER_OF_POLYGON_POINTS):
        x = radius * math.cos(angles[i]) + center_point.x
        y = radius * math.sin(angles[i]) + center_point.y
        polygon.append(Point(x,y))

    return polygon

#================================================
#               DRAW POINTS
#================================================
#just a comment it's harmless... really

fig, axs = plt.subplots()
axs.set_xlim(0,10)
axs.set_ylim(0,10)
axs.set_autoscale_on(False)

def draw_random_points(random_points: list[Point]):
    for i in range(len(random_points)):
        axs.plot(random_points[i].x,random_points[i].y,color='red',marker='.')

def draw_polygon(polygon_points: list[Point]) -> Polygon:
    polygon_coords = [(p.x, p.y) for p in polygon_points]
    polygon_patch = Polygon(polygon_coords,closed=True,facecolor='skyblue',edgecolor='navy',alpha=0.5)

    # for i in range(len(polygon_points)):
    #     axs.plot(polygon_points[i].x,polygon_points[i].y,color='navy',marker='.')

    return polygon_patch


#================================================
#               HILL CLIMB FUNCTION
#================================================

def hill_climb(solution: list[Point], points: list[Point], step_size: float) -> list[Point]:
    indx = random.randrange(len(solution))
    old_point = solution[indx]

    dx = random.uniform(-step_size,step_size)
    dy = random.uniform(-step_size,step_size)

    new_solution = deepcopy(solution)
    new_solution[indx].x = old_point.x + dx
    new_solution[indx].y = old_point.y + dy

    old_area = check_polygon_perimeter(solution)
    new_area = check_polygon_perimeter(new_solution)

    if new_area < old_area and all_points_inside_polygon(new_solution, points):
        return new_solution
    
    return solution

def anim_func(solution: list[Point], points: list[Point]):

    polygon = None

    for i in range(ITERATIONS):
        polygon = hill_climb(solution, points,STEP_SIZE)

    return polygon

#================================================
#               HELPER FUNCTION
#================================================

def check_polygon_perimeter(solution: list[Point]) -> float:
    perimeter = 0.0
    n = len(solution)

    for i in range(n):
        p1 = solution[i]
        p2 = solution[(i + 1) % n]
        perimeter += math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))
    
    return perimeter

def distance_from_line(p1: Point, p2: Point, point: Point):
    return ((p2.y - p1.y) * point.x - (p2.x - p1.x) * point.y + p2.x * p1.y - p2.y * p1.x) / (math.sqrt(math.pow((p2.y - p1.y), 2)) + math.pow((p2.x - p1.x),2))

def all_points_inside_polygon(solution: list[Point], points_to_check: list[Point]) -> bool:
    distance = 0.0
    for i in range(len(points_to_check)):
        for j in range(len(solution)):
            distance = distance_from_line(solution[j], solution[(j+1) % len(solution)], points_to_check[i])
            if distance < 0:
                return False
                break
    return True

#================================================
#               MAIN FUNCTION
#================================================

def main():

    random_points, center_point = initialize_random_points(5.0, 7.0)
    polygon = initialize_polygon(center_point,RADIUS)
    
    if all_points_inside_polygon(polygon,random_points): 
        print(f'Start perimeter: {check_polygon_perimeter(polygon)}')       
        
        draw_random_points(random_points)
        
        polygon_patch = draw_polygon(polygon)
        axs.add_patch(polygon_patch)
        polygon_state = {'polygon': polygon}

        def update(frame):
            nonlocal polygon
            polygon = hill_climb(polygon,random_points,STEP_SIZE)
            coords = [(p.x, p.y) for p in polygon]
            polygon_patch.set_xy(coords)
            return [polygon_patch]

        anim = FuncAnimation(fig,
                            update,
                            ITERATIONS,
                            interval=30,
                            blit=True,
                            repeat=False)
        plt.show()
    else:
        print(f'Generated point is outside polygon!')

if __name__ == '__main__':
    main()



# ez egy komment. azért raktam ide, hogy gyakoroljam a git-elést.... ami amúgy egy faszság... mert nem értek hozzá még