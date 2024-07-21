import pygame

# אתחול Pygame
pygame.init()

# הגדרת צבעים
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# הגדרת תצוגה
WIDTH = 600
HEIGHT = 400

# הגדרת גודל בלוק ומהירות התחלתית של הנחש
BLOCK_SIZE = 10
INITIAL_SNAKE_SPEED = 15

# הגדרת פונטים
FONT = pygame.font.SysFont(None, 25)
LARGE_FONT = pygame.font.SysFont(None, 50)

# טעינת תמונות רקע
BACKGROUND = pygame.image.load('background.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
BACKGROUND_USER = pygame.image.load('backgroundUser.jpg')
BACKGROUND_USER = pygame.transform.scale(BACKGROUND_USER, (WIDTH, HEIGHT))

# טעינת צלילים
EAT_SOUND = pygame.mixer.Sound('eat.wav')
GAMEOVER_SOUND = pygame.mixer.Sound('gameover.wav')
