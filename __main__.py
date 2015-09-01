#!/usr/bin/env python2
# encoding: utf-8

# =======================================================================================
# simple isometric game in python
# Copyright (C) 2015 Václav Mach
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# =======================================================================================

import sys
import pygame

# =======================================================================================
def info():
    print "isoarc Copyright (C) 2015 Václav Mach
    This program comes with ABSOLUTELY NO WARRANTY
    This is free software, and you are welcome to redistribute it under certain conditions, see LICENSE for details."
# =======================================================================================
def init():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    return screen

# =======================================================================================
def load_images():
    images = []

    images.append(pygame.image.load("tile3.png"))
    images.append(pygame.image.load("land.png"))
    images.append(pygame.image.load("horiz.png"))
    # index v poli musi odpovidat cislu reprezentujicimu dany objekt v mape
    # viz vykreslovaci logika

    return images

# =======================================================================================
# isometric version
def place_tile(tile_type, pos_x, pos_y, screen):
    #screen.blit(tile_type, ((2 * pos_y + pos_x) / 2, (2 * pos_y - pos_x) / 2))
    #screen.blit(tile_type, ((2 * pos_y + pos_x) / 2 - pos_x / 4, (2 * pos_y - pos_x) / 2 + pos_y / 4))
    #screen.blit(tile_type, ((2 * pos_y + pos_x) / 2 + pos_x / 4, (2 * pos_y - pos_x) / 2 + pos_x / 8))
    screen.blit(tile_type, ((2 * pos_y + pos_x) / 2 + pos_x / 4, (2 * pos_y - pos_x) / 2 + pos_x / 8))

# =======================================================================================
def main():
    info()
    screen = init()

    running = True
    red = (255, 0, 0)
    black = (0, 0, 0)
    width = height = 50
    position = [0, 0]
    direction = (0, 0)

    images = load_images()
    tile_width = tile_height = 40

    #game_map = [[1,1,1,1,1,1],
    #            [1,0,0,0,0,1],
    #            [1,0,0,0,0,1],
    #            [1,0,0,0,0,1],
    #            [1,0,0,0,0,1],
    #            [1,1,1,1,1,1]]



    game_map = [[0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0],
                [0,0,0,0,0,0]]


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        for i in range(0, len(game_map)):
            #for j in range(0, len(game_map[i])):
                # zaporny range, aby bylo vizualne spravne
            for j in range(len(game_map[i]), 0, -1):
                #print j
                #place_tile(images[game_map[i][j]], 100 + j * tile_width, 400 + i * tile_height, screen)
                #place_tile(images[game_map[i][j - 1]], 100 + j * tile_width, 400 + i * tile_height, screen)
                place_tile(images[game_map[i][j - 1]], 100 + j * tile_width, 400 + i * tile_height / 2, screen)


            # TODO vice klaves najednou

        #    if event.type == pygame.KEYDOWN:
        #        if event.key == pygame.K_DOWN:
        #            direction = (0, 2)

        #        if event.key == pygame.K_UP:
        #            direction = (0, -2)

        #        if event.key == pygame.K_RIGHT:
        #            direction = (2, 0)

        #        if event.key == pygame.K_LEFT:
        #            direction = (-2, 0)

        #    if event.type == pygame.KEYUP:
        #        direction = (0, 0)

        #position[0] += direction[0]
        #position[1] += direction[1]


        #screen.fill(black)

        pygame.time.Clock().tick(30)  # 30 fps
        pygame.display.flip()


    return 0

# =======================================================================================
if __name__ == "__main__":
    sys.exit(main())
