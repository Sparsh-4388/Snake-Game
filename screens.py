import pygame
import sys

def game_over(screen, win = False):
    msg = "You Win!" if win else "Game Over"
    font = pygame.font.SysFont(None, 60)
    small_font = pygame.font.SysFont(None, 40)

    try_again_rect = pygame.Rect(220, 300, 160, 50)

    pygame.event.clear()
    pygame.time.delay(200)

    while True:
        screen.fill((30, 30, 30))

        game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_text, (200, 150))

        pygame.draw.rect(screen, (0, 200, 0), try_again_rect)
        try_again_text = small_font.render("Try Again", True, (255, 255, 255))
        screen.blit(try_again_text, (try_again_rect.x + 25, try_again_rect.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                elif event.key == pygame.K_SPACE:
                        return 'retry'

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if try_again_rect.collidepoint(event.pos):
                    return 'retry'
