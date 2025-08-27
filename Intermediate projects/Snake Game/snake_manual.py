import pygame
import sys
import random
import tkinter as tk
from tkinter import messagebox

pygame.init()

WIDTH, HEIGHT = 1200, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()

snake_block = 20
snake_speed = 10

x = WIDTH // 2
y = HEIGHT // 2

def random_food():
    return (random.randrange(0, WIDTH - snake_block, snake_block),
            random.randrange(0, HEIGHT - snake_block, snake_block))

food_x, food_y = random_food()

x_change = 0
y_change = 0

snake_body = []
snake_length = 2
score = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_change = -snake_block
        y_change = 0
    elif keys[pygame.K_RIGHT]:
        x_change = snake_block
        y_change = 0
    elif keys[pygame.K_UP]:
        x_change = 0
        y_change = -snake_block
    elif keys[pygame.K_DOWN]:
        x_change = 0
        y_change = snake_block

    x += x_change
    y += y_change

    WINDOW.fill(BLACK)
    snake_head = [x, y]
    snake_body.append(snake_head)

    if snake_head[0] == food_x and snake_head[1] == food_y:
        snake_length += 1
        score += 1
        food_x, food_y = random_food()

    if len(snake_body) > snake_length:
        del snake_body[0]
    
    pygame.draw.rect(WINDOW, (255, 0, 0), (food_x, food_y, snake_block, snake_block))
    pygame.display.set_caption(f'Score:  {score}                                                                        Snake Game')
    for segment in snake_body:
        pygame.draw.rect(WINDOW, WHITE, (segment[0], segment[1], snake_block, snake_block))

    if x >=  WIDTH or x < 0 or y >= HEIGHT or y < 0:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo('Game Over!', "You hit the wall")
        pygame.quit()
        sys.exit()
    
    for block in snake_body[:-1]:
        if snake_body[0] == block[0] and snake_body[1] == block[1]:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo('Game Over!', 'You bit Yourself')
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(10)






