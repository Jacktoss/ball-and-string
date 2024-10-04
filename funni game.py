## slingy game where your mouse controls a little guy who is holding a string which has a ball on the end of it. the ball can be swung around and when you let go of the mouse button, the ball is flung in the direction the mouse was pointing.


import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slingy Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

player_pos = [WIDTH // 2, HEIGHT // 2]
ball_pos = [WIDTH // 2, HEIGHT // 2 + 100]
ball_velocity = [0, 0]
ball_radius = 20
string_length = 100
gravity = 0.5
damping = 0.995
angle = 0
speed = 0.05

running = True
mouse_pressed = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False

    mouse_x, mouse_y = pygame.mouse.get_pos()

    if mouse_pressed:
        dx = mouse_x - player_pos[0]
        dy = mouse_y - player_pos[1]
        angle = math.atan2(dy, dx)
        target_x = player_pos[0] + string_length * math.cos(angle)
        target_y = player_pos[1] + string_length * math.sin(angle)

        ball_velocity[0] = (target_x - ball_pos[0]) * 0.1
        ball_velocity[1] = (target_y - ball_pos[1]) * 0.1
    else:
        ball_velocity[1] += gravity

    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    dx = ball_pos[0] - player_pos[0]
    dy = ball_pos[1] - player_pos[1]
    distance = math.sqrt(dx**2 + dy**2)
    if distance > string_length:
        angle = math.atan2(dy, dx)
        ball_pos[0] = player_pos[0] + string_length * math.cos(angle)
        ball_pos[1] = player_pos[1] + string_length * math.sin(angle)

        radial_x = math.cos(angle)
        radial_y = math.sin(angle)
        tangent_x = -math.sin(angle)
        tangent_y = math.cos(angle)

        radial_velocity = ball_velocity[0] * radial_x + ball_velocity[1] * radial_y
        tangent_velocity = ball_velocity[0] * tangent_x + ball_velocity[1] * tangent_y

        ball_velocity[0] = tangent_x * tangent_velocity * damping
        ball_velocity[0] = tangent_y * tangent_velocity * damping

    screen.fill(WHITE)

    pygame.draw.circle(screen, BLACK, player_pos, 10)
    pygame.draw.circle(screen, BLACK, [int(ball_pos[0]), int(ball_pos[1])], ball_radius)
    pygame.draw.line(screen, BLACK, player_pos, [int(ball_pos[0]), int(ball_pos[1])], 2)

    pygame.display.flip()
    
    pygame.time.Clock().tick(60)

pygame.quit()



















