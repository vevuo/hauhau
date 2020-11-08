import pygame


def setup():
    pygame.init()
    screen = pygame.display.set_mode((240, 240))
    return screen


def start_game(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 255), (120, 120), 40)
        pygame.display.flip()

    pygame.quit()


screen = setup()
start_game(screen)
