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
        self._vy = random.uniform(-1, -3) # 本当は (-1, -4)
        self._maxhp = 100
        self._hp = 100

    @property
    def maxhp(self):
        return self._maxhp
    
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, value):
        self._hp = value

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
        # hpbar
        rect1 = pg.Rect(self._rect.x, self._rect.y - 20, 4, 20)
        h = (self._hp / self._maxhp) * 20
        rect2 = pg.Rect(self._rect.x, self._rect.y - h, 4, h)
        pg.draw.rect(screen, pg.Color("RED"), rect1)
        pg.draw.rect(screen, pg.Color("GREEN"), rect2)