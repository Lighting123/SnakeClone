import pygame

# pygame setup
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

# constants
DIRECTION_LEFT = 0
DIRECTION_RIGHT = 1
DIRECTION_UP = 3
DIRECTION_DOWN = 4

size = 1

def draw_snake(direction):
    snake = pygame.Surface((50, 50))
    snake.fill('lightgreen')
    snake_rect_list = []
    for i in range(size):
        if len(snake_rect_list) == 0:
            snake_rect_list.append(pygame.draw.rect(snake, 'darkgreen', (0, 0, 8, 6)))
        else:
            last_snake_rect = snake_rect_list[-1]
            snake_rect_list.append(pygame.draw.rect(snake, 'darkgreen', (last_snake_rect.left+8, 0, 8, 6)))
    snake_rect_list.append(pygame.draw.rect(snake, 'darkgreen', (snake_rect_list[-1].left+8, 0, 8, 6)))

    return snake

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render game
    screen.fill('lightgreen')
    screen.blit(draw_snake(DIRECTION_LEFT), (0, 0))

    pygame.display.update()

    # limit fps to 60
    clock.tick(60)

pygame.quit()