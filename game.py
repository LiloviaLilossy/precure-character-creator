import pygame
from defs.sprite import Base
pygame.init()

sc = pygame.display.set_mode((1280,720))

body = Base()

game=True
while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game=False
    sc.fill((255,255,255))
    sc.blit(body.base_image, body.rect)
    sc.blit(body.base_eyes, body.eyes_rect)
    pygame.display.update()