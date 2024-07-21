import pygame
import json
from constants import *


# מצייר טקסט על המסך
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    pygame.draw.rect(surface, BLACK, (x - 5, y - 5, textrect.width + 10, textrect.height + 10))
    surface.blit(textobj, textrect)


# מצייר את הנחש על המסך
def our_snake(screen, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])


# מקבל את רשימת הניקוד הגבוה מקובץ JSON
def get_high_scores():
    try:
        with open("high_scores.json", "r") as file:
            return json.load(file)
    except:
        return []


# שומר את רשימת הניקוד הגבוה בקובץ JSON
def save_high_scores(scores):
    with open("high_scores.json", "w") as file:
        json.dump(scores, file)


# מציג את רשימת הניקוד הגבוה על המסך
def show_high_scores(screen):
    high_scores = get_high_scores()
    screen.blit(BACKGROUND, (0, 0))
    draw_text("High Scores", LARGE_FONT, GOLD, screen, WIDTH // 2 - 100, 50)
    for i, score in enumerate(high_scores[:5]):
        draw_text(f"{i + 1}. {score['name']}: {score['score']}", FONT, WHITE, screen, WIDTH // 2 - 100, 100 + i * 30)
    draw_text("Press any key to return", FONT, ORANGE, screen, WIDTH // 2 - 100, HEIGHT - 50)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                waiting = False


# מקבל את שם השחקן מהמשתמש
def get_player_name(screen):
    player_name = ""
    input_active = True
    while input_active:
        screen.blit(BACKGROUND, (0, 0))
        draw_text("Enter your name:", FONT, BLUE, screen, WIDTH // 2 - 100, HEIGHT // 2 - 50)
        draw_text(player_name, FONT, WHITE, screen, WIDTH // 2 - 100, HEIGHT // 2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode
    return player_name
