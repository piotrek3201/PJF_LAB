import pygame

def text(text, x, y, color, font, screen):
    text_surface = font.render(text, False, color)
    screen.blit(text_surface, (x, y))