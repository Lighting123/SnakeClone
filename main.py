import pygame

# pygame setup
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake clone')
clock = pygame.time.Clock()
running = True

# constants
DIRECTION_LEFT = 0
DIRECTION_RIGHT = 1
DIRECTION_UP = 3
DIRECTION_DOWN = 4

size = 1


class Snake:
    def __init__(self, direction):
        self.direction = direction
        self.snake = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.snake_rect = pygame.Rect(0, 0, 0, 0)

    def draw_snake_on_screen(self):
        self.snake.fill('lightgreen')

        if self.snake_rect.left >= WINDOW_WIDTH:
            self.snake_rect.left = 0
        elif self.snake_rect.left <= 0:
            self.snake_rect.left = WINDOW_WIDTH

        for i in range(size):
            # if it is the first snake part, draw it at coordinate 0, 0
            if i == 0:
                pygame.draw.rect(self.snake, 'darkgreen', (self.snake_rect.left, 0, 8, 6))
            else:
                pygame.draw.rect(self.snake, 'darkgreen', (self.snake_rect.left + 8*i, 0, 8, 6))

        pygame.draw.rect(self.snake, 'darkgreen', (self.snake_rect.left + 8*size, 0, 8, 6))

    def move(self):
        if self.direction == DIRECTION_LEFT:
            self.snake_rect.left -= 2
        elif self.direction == DIRECTION_RIGHT:
            self.snake_rect.left += 2
        elif self.direction == DIRECTION_UP:
            pass
        elif self.direction == DIRECTION_DOWN:
            pass

    def change_direction(self, direction):
        self.direction = direction


snake = Snake(DIRECTION_LEFT)
snake.draw_snake_on_screen()

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render game
    screen.fill('lightgreen')

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake.change_direction(DIRECTION_UP)
    if keys[pygame.K_s]:
        snake.change_direction(DIRECTION_DOWN)
    if keys[pygame.K_a]:
        snake.change_direction(DIRECTION_LEFT)
    if keys[pygame.K_d]:
        snake.change_direction(DIRECTION_RIGHT)

    snake.move()
    snake.draw_snake_on_screen()
    screen.blit(snake.snake, (0, 0))

    pygame.display.update()

    # limit fps to 60
    clock.tick(60)

pygame.quit()
