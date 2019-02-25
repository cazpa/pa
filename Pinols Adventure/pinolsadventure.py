#!/usr/bin/env python3
# by Felix Valentin de Caspary

## GPLv3
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame
import sys
import os
import time

"""
OBJECTS (classes and functions)
"""
# CHARACTERS
mainCharacterImg = pygame.image.load('assets/pepo.png')
demonLeftImg = pygame.image.load('assets/demon.png')
demonRightImg = pygame.image.load('assets/demon_right.png')

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self) # Call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    elif size == "dialogue":
        textSurface = dialoguefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, x_displace = 0, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2) + x_displace, (display_height / 2) + y_displace
    world.blit(textSurf, textRect)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    L1_cutscene()
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        world.fill(color_darkgray)
        message_to_screen("Piñol's adventure", color_red, 0, -100, "large")
        message_to_screen("This is Red Points. But in Piñol's mad head.", color_red, 0, 0, "medium")
        message_to_screen("You're schizophrenic. Haunted by your voices. Your lust overcomes you...", color_red, 0, 30, "small")
        message_to_screen("All these years, working in Red Points, you've always been recognized as one badass motherfucker.", color_red, 0, 55, "small")
        message_to_screen("But also a crazy motherfucker. Blood. Gore. Kidnapping. Murder. You think about it. You dream about it.", color_red, 0, 80, "small")
        message_to_screen("What are you going to do about it?", color_red, 0, 105, "small")
        message_to_screen("Press [N] to start the game.", color_white, 0, 300, "small")
        pygame.display.update()

def L1_cutscene():
    L1_cs = True
    mainCharX = 30
    mainCharY = display_height - 416
    demonCharX = 600
    demonCharY = 300

    while L1_cs:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        BG = Background('assets/L1_bg.jpg', [0, 0])
        world.fill([255, 255, 255])
        world.blit(BG.image, BG.rect)
        world.blit(mainCharacterImg, (mainCharX, mainCharY))
        world.blit(demonLeftImg, (demonCharX, demonCharY))
        pygame.display.update()
        message_to_screen("Pepo: What is this...", color_white, 0, 330, "dialogue")
        # Add delay
        message_to_screen("Voice: Your dome. Your head. Enter.", color_white, 300, -100, "dialogue")

        pygame.display.update()

"""
SETUP (singe-run)
"""
display_width = 960
display_height = 720
fps = 40
ani = 4 # Animation cycles
clock = pygame.time.Clock()
pygame.init()

color_white = (255, 255, 255)
color_darkgray = (25, 25, 25)
color_black = (0, 0, 0)
color_red = (255, 0, 0)
color_green = (0, 155, 0)

smallfont = pygame.font.SysFont(None, 26)
medfont = pygame.font.SysFont(None, 45)
largefont = pygame.font.SysFont(None, 80)
dialoguefont = pygame.font.SysFont(None, 30)


world = pygame.display.set_mode((display_width, display_height))
backdropbox = world.get_rect()

"""
MAIN LOOP (game-loop)
"""
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                gameExit = True
    game_intro()
    pygame.display.update()
    L1_cutscene()
    pygame.display.update()
