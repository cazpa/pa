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
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    world.blit(textSurf, textRect)

def game_intro():
    intro = True
    while intro:
        world.fill(color_darkgray)
        message_to_screen("Piñol's adventure", color_red, -100, "large")
        message_to_screen("This is Red Points. ", color_red, 0, "medium")
        pygame.display.update()
        time.sleep(2)
        message_to_screen("But in Piñol's mad head...", color_red, 0, "small")
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

smallfont = pygame.font.SysFont(None, 25)
medfont = pygame.font.SysFont(None, 45)
largefont = pygame.font.SysFont(None, 80)


world = pygame.display.set_mode((display_width, display_height))
backdropbox = world.get_rect()

"""
MAIN LOOP (game-loop)
"""
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                gameExit = True
    game_intro()
    pygame.display.update()
clock.tick(fps)
