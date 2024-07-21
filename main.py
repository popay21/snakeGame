import pygame
import sys
from constants import *
from utils import draw_text, show_high_scores, get_player_name, get_high_scores, save_high_scores
from game import gameLoop

# מציג את התפריט הראשי ומטפל בקלט מהמשתמש
def main_menu(screen):
    while True:
        screen.blit(BACKGROUND_USER, (0, 0))
        draw_text("Snake Game", LARGE_FONT, BLUE, screen, WIDTH // 2 - 100, 50)
        draw_text("1. Start Game", FONT, GREEN, screen, WIDTH // 2 - 70, 150)
        draw_text("2. High Scores", FONT, ORANGE, screen, WIDTH // 2 - 70, 200)
        draw_text("3. Quit", FONT, RED, screen, WIDTH // 2 - 70, 250)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 'start'  # התחלת המשחק
                elif event.key == pygame.K_2:
                    show_high_scores(screen)  # הצגת ניקוד גבוה
                elif event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()  # יציאה מהמשחק

# לולאת המשחק הראשית, מנהלת את זרימת המשחק
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Advanced Snake Game')

    while True:
        choice = main_menu(screen)
        if choice == 'start':
            score = gameLoop(screen)  # משחק ומקבל את הניקוד
            player_name = get_player_name(screen)  # קבלת שם השחקן
            high_scores = get_high_scores()  # קבלת רשימת ניקוד גבוה
            high_scores.append({"name": player_name, "score": score})  # הוספת ניקוד חדש
            high_scores.sort(key=lambda x: x["score"], reverse=True)  # מיון הניקודים
            save_high_scores(high_scores[:10])  # שמירת עשרת הניקודים הגבוהים ביותר
            show_high_scores(screen)  # הצגת הניקודים הגבוהים

if __name__ == "__main__":
    main()  # הרצת לולאת המשחק הראשית

