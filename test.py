import pygame as pg
import sys
import os

wall = 0

WIDTH = 800
HEIGHT = 600
TITLE = 'Importing A Map'
CLOCK = pg.time.Clock()
FPS = 60

DARKGRAY = (40, 40, 40)
RED = (255, 0, 0)

game_folder = os.path.dirname(__file__)

# create tiles, (WIDTH = 20 tiles, HEIGHT = 15 tiles)
TILESIZE = 40
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)

def load_map():
    map_data = []
    with open(path.join(game_folder, 'map.txt'), 'rt') as f:
        for line in f:
            map_data.append(line)

def new_game():
    global wall
    for row, tiles in enumerate(map_data):
        for col, tile in enumerate(tiles):
             if tile == '1':
                Wall(col, row)

             wall = Wall(col, row)

def draw_tiles():
    for x in range(0, WIDTH, TILESIZE):
        pg.draw.line(screen, DARKGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pg.draw.line(screen, DARKGRAY, (0, y), (WIDTH, y))

class Wall(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


def game_loop():
    pg.init()

    all_sprites = pg.sprite.Group()
    all_sprites.add(wall)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        draw_tiles()
        all_sprites.update()
        all_sprites.draw(screen)

        pg.display.update()
        CLOCK.tick(FPS)

    pg.quit()

game_loop()
