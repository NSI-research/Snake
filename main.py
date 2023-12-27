# -------------------
#
#   Date : 2023-12-21
#   Auteur : Lodjo28
#   Nom du fichier : main
#   Version : 0.1
#
# -------------------

import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = WIDTH * 0.8
direction = "RIGHT"
change_direction = direction
snake_pos = [100, 50]
snake_body = [[100, 50]]
snake_size = 30


apple_size = 30
apple_pos = [random.randrange(1, (WIDTH//apple_size)) * apple_size, 
             random.randrange(1, (HEIGHT//apple_size)) * apple_size]
apple_spawned = True

def spawn_apple():
    return [random.randrange(1, (WIDTH//apple_size)) * apple_size, 
            random.randrange(1, (HEIGHT//apple_size)) * apple_size]



root = pygame.display.set_mode((WIDTH, HEIGHT))
run = True

speed = 10
clock = pygame.time.Clock()

while run:

    key = pygame.key.get_pressed()
    if key[pygame.K_q]:
        change_direction = "LEFT"
    elif key[pygame.K_d]:
        change_direction = "RIGHT"
    elif key[pygame.K_z]:
        change_direction = "UP"
    elif key[pygame.K_s]:
        change_direction = "DOWN"


    if change_direction == "UP" and direction != "DOWN":
        direction = "UP"
    if change_direction == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_direction == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_direction == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"


    if direction == "UP":
        snake_pos[1] -= snake_size
    if direction == "DOWN":
        snake_pos[1] += snake_size
    if direction == "LEFT":
        snake_pos[0] -= snake_size
    if direction == "RIGHT":
        snake_pos[0] += snake_size


    snake_head_rect = pygame.Rect(snake_pos[0], snake_pos[1], snake_size, snake_size)
    apple_rect = pygame.Rect(apple_pos[0], apple_pos[1], apple_size, apple_size)

    if snake_head_rect.colliderect(apple_rect):
        apple_pos = spawn_apple()
        snake_body.insert(0, list(snake_pos))
    else:
        snake_body.insert(0, list(snake_pos))
        snake_body.pop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Game closed.")
            run = False

    root.fill((0, 0, 0))
    for pos in snake_body:
        pygame.draw.rect(root, (0, 255, 0), pygame.Rect(pos[0], pos[1], snake_size, snake_size))
    pygame.draw.rect(root, (255, 0, 0), pygame.Rect(apple_pos[0], apple_pos[1], apple_size, apple_size))



    pygame.display.flip()

    clock.tick(speed)

pygame.quit()