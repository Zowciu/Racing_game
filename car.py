import pygame
import time
import math
from functions import image_size, rotate_image_center

GRASS = image_size(pygame.image.load("textures/grass.jpg"), 2.5)
TRACK = image_size(pygame.image.load("textures/track.png"), 0.8)
TRACK_BORDER = image_size(pygame.image.load("textures/track-border.png"), 0.8)
FINISH = image_size(pygame.image.load("textures/finish.png"), 0.9)

GREEN_CAR = image_size(pygame.image.load("textures/green-car.png"), 0.7)
RED_CAR = image_size(pygame.image.load("textures/red-car.png"), 0.7)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RACING GAME")

FPS = 60


class Car:
    def __int__(self, max_velocity, rotation_velocity):
        self.img = self.IMG
        self.start_velocity = 0
        self.start_angle = 0
        self.max_velocity = max_velocity
        self.rotation_velocity = rotation_velocity

    def rotate(self, left=False, right=False):
        if left:
            self.start_angle += self.rotation_velocity
        if right:
            self.start_angle -= self.rotation_velocity

    def draw(self, win):
        rotate_image_center(win, self.img)


class PlayerCar(Car):
    IMG = GREEN_CAR


def draw(win, image, player_car):
    for img, pos, in image:
        win.blit(img, pos)

    player_car.draw()
    pygame.display.update()


run = True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0))]
player_car = PlayerCar(4, 4)

while run:

    clock.tick(FPS)

    draw(WINDOW, images, player_car)
    #WINDOW.blit(GREEN_CAR, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break


pygame.quit()




