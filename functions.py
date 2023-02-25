import pygame


def image_size(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def rotate_image_center(win, img, top_left, angle):
    rotated_image = pygame.transform.rotate(img, angle)
    new_rect = rotated_image.get_rect(center=img.get_rect(top_left=top_left).center)

    win.blit(rotated_image, new_rect)