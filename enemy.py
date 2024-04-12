import pygame as pg
import random

class Enemy:
    """ 敵 """
    def __init__(self) -> None:
        x = random.randint(100, 500)
        y = random.randint(100, 200)
        # プロパティ
        self._image = pg.image.load("images/enemy1.png")
        self._rect = pg.Rect(x, y, 50, 50)
        self._vx = random.uniform(-4, 4)
        self._vy = random.uniform(-1, -4)

    @property
    def rect(self):
        return self._rect
    @rect.setter
    def rect(self, value):
        self._rect = value

    @property
    def vy(self):
        return self._vy
    @vy.setter
    def vy(self, value):
        self._vy = value

    def update(self):
        if self._rect.x < 0 or self._rect.x > 500:
            self._vx = -self._vx
        if self._rect.y < 0:
            self._vy = -self._vy
        self._rect.x += self._vx
        self._rect.y += self._vy

    def draw(self, screen):
        screen.blit(self._image, self._rect)