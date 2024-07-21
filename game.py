import pygame
import random
import os
from constants import *
from utils import draw_text, our_snake

# טוען אנימציות תפוח
def load_apple_animation():
    apple_images = []
    base_path = os.path.dirname(os.path.abspath(__file__))
    apple_folder = os.path.join(base_path, 'Animations', 'Apple')

    for i in range(10):  # מניח שיש 10 תמונות, יש להתאים אם יש מספר שונה
        img_path = os.path.join(apple_folder, f'img_{i}.png')
        if os.path.exists(img_path):
            img = pygame.image.load(img_path)
            img = pygame.transform.scale(img, (BLOCK_SIZE, BLOCK_SIZE))
            apple_images.append(img)
        else:
            print(f"אזהרה: לא נמצאה תמונה {img_path}")

    if not apple_images:
        # אם לא נטענו תמונות, יצירת ריבוע אדום כברירת מחדל
        fallback_surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        fallback_surface.fill(RED)
        apple_images.append(fallback_surface)

    return apple_images

# לולאת המשחק הראשית
def gameLoop(screen):
    game_over = False
    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
    score = 0
    level = 1
    snake_speed = INITIAL_SNAKE_SPEED

    # טעינת אנימציית התפוח
    apple_images = load_apple_animation()
    apple_animation_index = 0

    # יצירת מכשולים
    obstacles = []
    for _ in range(5):
        obstacle_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
        obstacle_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
        obstacles.append((obstacle_x, obstacle_y))

    # פרי מיוחד
    special_fruit = None
    special_fruit_timer = 0

    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            GAMEOVER_SOUND.play()
            return score

        x1 += x1_change
        y1 += y1_change
        screen.blit(BACKGROUND, (0, 0))

        # ציור מכשולים
        for obstacle in obstacles:
            pygame.draw.rect(screen, WHITE, [obstacle[0], obstacle[1], BLOCK_SIZE, BLOCK_SIZE])

        # ציור תפוח מונפש
        screen.blit(apple_images[apple_animation_index], (foodx, foody))
        apple_animation_index = (apple_animation_index + 1) % len(apple_images)

        # ציור פרי מיוחד
        if special_fruit:
            pygame.draw.rect(screen, GOLD, [special_fruit[0], special_fruit[1], BLOCK_SIZE, BLOCK_SIZE])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                GAMEOVER_SOUND.play()
                return score

        for obstacle in obstacles:
            if snake_Head[0] == obstacle[0] and snake_Head[1] == obstacle[1]:
                GAMEOVER_SOUND.play()
                return score

        our_snake(screen, snake_List)
        draw_text(f"Score: {score}", FONT, PURPLE, screen, 10, 10)
        draw_text(f"Level: {level}", FONT, BLUE, screen, WIDTH - 100, 10)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            Length_of_snake += 1
            score += 10
            EAT_SOUND.play()

            # עלייה ברמה כל 50 נקודות
            if score % 50 == 0:
                level += 1
                snake_speed += 2

        # טיפול בפרי מיוחד
        if special_fruit:
            if x1 == special_fruit[0] and y1 == special_fruit[1]:
                score += 50
                special_fruit = None
                EAT_SOUND.play()
        else:
            special_fruit_timer += 1
            if special_fruit_timer >= 100:  # הופעת פרי מיוחד כל 100 פריימים
                special_fruit = (round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0,
                                 round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0)
                special_fruit_timer = 0

        clock.tick(snake_speed)
