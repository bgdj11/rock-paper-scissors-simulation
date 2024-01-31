import pygame
import sys
import random
from pygame.locals import*

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 770

rock_num = 15
sc_num = 15
paper_num = 15

SPEED_FACTOR = 1.6

BACKGROUND = (161, 219, 251)
WHITE = (255, 255, 255)

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ROCK PAPER SCISSORS SIMULATION")

class Rock:
    def __init__(self):
        self.image = pygame.image.load("Assets/rock.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.dx = 0
        self.dy = 0
        while abs(self.dx) <= 0.32 and abs(self.dy) <= 0.32:
            self.dx = random.uniform(-1, 1) * SPEED_FACTOR
            self.dy = random.uniform(-1, 1) * SPEED_FACTOR

    def draw(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.dx = -self.dx
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.dy = -self.dy
        window.blit(self.image, self.rect)

    def update(self, objects):
        for obj in objects:
            if obj != self and self.rect.colliderect(obj.rect):
                if isinstance(obj, Paper):
                    
                    self.__class__ = Paper
                    self.image = pygame.image.load("Assets/paper.png")
                    self.image = pygame.transform.scale(self.image, (60, 60))
                    self.dx = random.uniform(-1, 1) * SPEED_FACTOR
                    self.dy = random.uniform(-1, 1) * SPEED_FACTOR
                    while abs(self.dx) <= 0.32 and abs(self.dy) <= 0.32:
                        self.dx = random.uniform(-1, 1) * SPEED_FACTOR
                        self.dy = random.uniform(-1, 1) * SPEED_FACTOR
                

class Paper:
    def __init__(self):
        self.image = pygame.image.load("Assets/paper.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.dx = 0
        self.dy = 0
        while abs(self.dx) <= 0.32 and abs(self.dy) <= 0.32:
            self.dx = random.uniform(-1, 1) * SPEED_FACTOR
            self.dy = random.uniform(-1, 1) * SPEED_FACTOR

    def draw(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.dx = -self.dx
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.dy = -self.dy
        window.blit(self.image, self.rect)

    def update(self, objects):
        for obj in objects:
            if obj != self and self.rect.colliderect(obj.rect):
                if isinstance(obj, Scissors):
                    
                    self.__class__ = Scissors
                    self.image = pygame.image.load("Assets/scissors.png")
                    self.image = pygame.transform.scale(self.image, (60, 60))
                    self.dx = random.uniform(-1, 1) * SPEED_FACTOR
                    self.dy = random.uniform(-1, 1) * SPEED_FACTOR
                    while abs(self.dx) <= 0.32 and abs(self.dy) <= 0.32:
                        self.dx = random.uniform(-1, 1) * SPEED_FACTOR
                        self.dy = random.uniform(-1, 1) * SPEED_FACTOR
    

class Scissors:
    def __init__(self):
        self.image = pygame.image.load("Assets/scissors.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.dx = 0
        self.dy = 0
        while abs(self.dx) <= 0.32 and abs(self.dy) <= 0.32:
            self.dx = random.uniform(-1, 1) * SPEED_FACTOR
            self.dy = random.uniform(-1, 1) * SPEED_FACTOR

    def draw(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.dx = -self.dx
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.dy = -self.dy
        window.blit(self.image, self.rect)

    def update(self, objects):
        for obj in objects:
            if obj != self and self.rect.colliderect(obj.rect):
                if isinstance(obj, Rock):
                    
                    self.__class__ = Rock
                    self.image = pygame.image.load("Assets/rock.png")
                    self.image = pygame.transform.scale(self.image, (60, 60))
                    self.dx = random.uniform(-1, 1) * SPEED_FACTOR
                    self.dy = random.uniform(-1, 1) * SPEED_FACTOR
                    while abs(self.dx) <= 0.32 and abs(self.dy) <= 0.32:
                        self.dx = random.uniform(-1, 1) * SPEED_FACTOR
                        self.dy = random.uniform(-1, 1) * SPEED_FACTOR

class Slider:
        def __init__(self, x, y, width, height, min_val, max_val, initial_val):
            self.x = x;
            self.y = y;
            self.width = width
            self.height = height
            self.min_value = min_val
            self.max_value = max_val
            self.value = initial_val
            self.dragging = False
        
        def draw(self, surface):
            pygame.draw.rect(surface, (0, 0, 0), (self.x, self.y, self.width, self.height), 2)
            pos = self.x + (self.value - self.min_value) / (self.max_value - self.min_value) * self.width
            pygame.draw.circle(surface, (0, 0, 0), (int(pos), self.y + self.height // 2), self.height // 2)

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
                    self.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
            elif event.type == pygame.MOUSEMOTION and self.dragging:
                mouse_pos = pygame.mouse.get_pos()
                pos = max(self.x, min(self.x + self.width, mouse_pos[0]))
                self.value = self.min_value + (self.max_value - self.min_value) * (pos - self.x) / self.width
                
objects = []

for i in range(rock_num):
    rock = Rock()
    objects.append(rock)
for i in range(paper_num):
    paper = Paper()
    objects.append(paper)
for i in range(sc_num):
    scissors = Scissors()
    objects.append(scissors)


def restart_game():
    for o in objects:
        objects.remove(o);
    for i in range(rock_num):
        rock = Rock()
        objects.append(rock)
    for i in range(paper_num):
        paper = Paper()
        objects.append(paper)
    for i in range(sc_num):
        scissors = Scissors()
        objects.append(scissors)


slider = Slider(30, 30, 200, 20, 1.0, 5.0,  SPEED_FACTOR)

#MAIN
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        slider.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                restart_game()

    window.fill(BACKGROUND)

    button_rect = pygame.Rect(SCREEN_WIDTH - 150, 15, 130, 55)
    pygame.draw.rect(window, (98, 145, 100), button_rect)
    font = pygame.font.Font(None, 24)
    text = font.render("RESTART", True, BACKGROUND)
    text_rect = text.get_rect(center=button_rect.center)
    window.blit(text, text_rect)

    for obj in objects:
        obj.update(objects)  

    for obj in objects:
        obj.draw()
    

    rock_count = len([obj for obj in objects if isinstance(obj, Rock)])
    paper_count = len([obj for obj in objects if isinstance(obj, Paper)])
    scissors_count = len([obj for obj in objects if isinstance(obj, Scissors)])

    if rock_count == 0 and scissors_count == 0:
        font = pygame.font.SysFont(None, 130)
        text = font.render("PAPERS WON!", True, (255, 10, 10))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        window.blit(text, text_rect)

    elif paper_count == 0 and scissors_count == 0:
        font = pygame.font.SysFont(None, 130)
        text = font.render("ROCKS WON!", True, (255, 10, 10))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        window.blit(text, text_rect)
        
    elif rock_count == 0 and scissors_count > paper_count == 0:
        font = pygame.font.SysFont(None, 130)
        text = font.render("SCISSORS WON!", True, (255, 10, 10))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        window.blit(text, text_rect)

    #slider
    SPEED_FACTOR = slider.value
    slider.draw(window)

    font = pygame.font.Font(None, 20)
    text_surface = font.render(f"SPEED: {SPEED_FACTOR:.1f}", True, (0, 0, 0))
    text_speed_rect = text_surface.get_rect()
    text_speed_rect.center = (slider.x + slider.width // 2, slider.y - text_rect.height // 2)
    window.blit(text_surface, text_speed_rect)

    slider.draw(window)
    
    pygame.display.update()
