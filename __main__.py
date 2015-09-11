#!/usr/bin/env python3
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
    print("isoarc Copyright (C) 2015 Václav Mach\nThis program comes with ABSOLUTELY NO WARRANTY\nThis is free software, and you are welcome to redistribute it under certain conditions, see LICENSE for details.")

# =======================================================================================
def init():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    return screen

# =======================================================================================
class Map:
    def __init__(self, screen, tile_width, tile_height):
        self.screen = screen
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tiles = self.loadImages()
        self.game_map = [[[0,0,0,0,0,0],
                          [0,0,0,0,0,0],
                          [0,0,-1,-1,0,0],
                          [0,0,0,-1,-1,0],
                          [0,0,0,0,0,0],
                          [0,0,-1,-1,0,0]],

                         [[0,0,0,0,-1,-1],
                          [0,0,0,-1,-1,-1],
                          [0,0,-1,-1,-1,-1],
                          [-1,-1,-1,-1,-1,-1],
                          [0,-1,-1,-1,-1,-1],
                          [0,-1,-1,-1,-1,-1]],

                         [[0,0,-1,-1,-1,-1],
                          [0,-1,-1,-1,-1,-1],
                          [-1,-1,-1,-1,-1,-1],
                          [-1,-1,-1,-1,-1,-1],
                          [-1,-1,-1,-1,-1,-1],
                          [-1,-1,-1,-1,-1,-1]]]

    def loadImages(self):
        images = []
        images.append(pygame.image.load("res/land.png"))
        return images

    def getTile(self, coord_x, coord_y, coord_z):
        if self.game_map[coord_z][coord_x][coord_y] != -1:
            return self.tiles[self.game_map[coord_z][coord_x][coord_y]]
        else:
            return None

    def getMaxCoordX(self):
        return len(self.game_map[0][0])

    def getMaxCoordY(self):
            return len(self.game_map[0])

    def getMaxCoordZ(self):
            return len(self.game_map)

    def renderMap(self, pos_x, pos_y):
        for k in range(0,self.getMaxCoordZ()):
            for i in range(0, self.getMaxCoordX()):
                for j in range(0, self.getMaxCoordY()):
                    if self.getTile(i,j,k) is not None:
                        self.screen.blit(self.getTile(i,j,k), (pos_x + (j - i) * self.tile_width / 2, pos_y + (i + j) * self.tile_height / 2 - self.tile_height * k ))

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
    #inital position of 0,0,0 tile
    pos_x = 250
    pos_y = 400
    tile_width = 60
    tile_height = 30
    map = Map(screen, tile_width, tile_height)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    screen.fill(black)
                    pos_x -= 10
                if event.key == pygame.K_RIGHT:
                    screen.fill(black)
                    pos_x += 10
                if event.key == pygame.K_UP:
                    screen.fill(black)
                    pos_y -= 10
                if event.key == pygame.K_DOWN:
                    screen.fill(black)
                    pos_y += 10

        map.renderMap(pos_x, pos_y)

	# 30 fps
        pygame.time.Clock().tick(30)
        pygame.display.flip()

    return 0

# =======================================================================================
if __name__ == "__main__":
    sys.exit(main())
