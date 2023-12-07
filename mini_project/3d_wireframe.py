import pygame
import math
from pygame.locals import *

# Initialize Pygame
pygame.init()


WIDTH, HEIGHT = 800, 600
FPS = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Wireframe Animation")
clock = pygame.time.Clock()

# 3D cube vertices
vertices = [
    [-50, -50, -50],
    [50, -50, -50],
    [50, 50, -50],
    [-50, 50, -50],
    [-50, -50, 50],
    [50, -50, 50],
    [50, 50, 50],
    [-50, 50, 50]
]

# Cube edges (vertex indices)
edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]


angleX, angleY = 0, 0

# Function to project 3D points to 2D screen
def project(vertex, cosX, sinX, cosY, sinY):
    x = vertex[0] * cosY - vertex[2] * sinY
    y = vertex[1] * cosX + (vertex[2] * cosY + vertex[0] * sinY) * sinX
    z = vertex[1] * -sinX + (vertex[2] * cosY + vertex[0] * sinY) * cosX

    scale = 400 / (z + 400)
    return [x * scale + WIDTH / 2, y * scale + HEIGHT / 2]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Drawing logic
    cosX = math.cos(angleX)
    sinX = math.sin(angleX)
    cosY = math.cos(angleY)
    sinY = math.sin(angleY)

    for edge in edges:
        p1 = project(vertices[edge[0]], cosX, sinX, cosY, sinY)
        p2 = project(vertices[edge[1]], cosX, sinX, cosY, sinY)
        pygame.draw.line(screen, WHITE, p1, p2, 2)

    pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 5)

    angleX += 0.01
    angleY += 0.01

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
