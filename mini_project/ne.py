import numpy as np
import pygame
from pygame.locals import *

def plot_cube(screen, vertices, polygons):
    pygame.draw.polygon(screen, (255, 255, 255), [(vertices[i, 0], vertices[i, 1]) for i in polygons[0]])
    pygame.draw.polygon(screen, (255, 255, 255), [(vertices[i, 0], vertices[i, 1]) for i in polygons[1]])
    pygame.draw.polygon(screen, (255, 255, 255), [(vertices[i, 0], vertices[i, 1]) for i in polygons[2]])
    pygame.draw.polygon(screen, (255, 255, 255), [(vertices[i, 0], vertices[i, 1]) for i in polygons[3]])
    pygame.draw.polygon(screen, (255, 255, 255), [(vertices[i, 0], vertices[i, 1]) for i in polygons[4]])
    pygame.draw.polygon(screen, (255, 255, 255), [(vertices[i, 0], vertices[i, 1]) for i in polygons[5]])

def rotate(points, axis, angle):
    rot_matrix = np.zeros((points.shape[0], 3, 3))
    for i in range(points.shape[0]):
        x, y, z = points[i, 0], points[i, 1], points[i, 2]
        if axis == "x":
            rot_matrix[i] = np.array([[1, 0, 0],
                                        [0, np.cos(angle), -np.sin(angle)],
                                        [0, np.sin(angle), np.cos(angle)]])
        elif axis == "y":
            rot_matrix[i] = np.array([[np.cos(angle), 0, np.sin(angle)],
                                        [0, 1, 0],
                                        [-np.sin(angle), 0, np.cos(angle)]])
        elif axis == "z":
            rot_matrix[i] = np.array([[np.cos(angle), -np.sin(angle), 0],
                                        [np.sin(angle), np.cos(angle), 0],
                                        [0, 0, 1]])
        points[i, :] = np.dot(rot_matrix[i], np.array([x, y, z, 1]))[:3]
    return points

# Vertex Coordinates
vertices = np.array([[0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1], [1, 0, 1]])

# Polygon Vertex Indices
polygons = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [2, 3, 7, 6], [0, 3, 7, 4], [1, 2, 6, 5]])

pygame.init()
screen = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF)

angle = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen