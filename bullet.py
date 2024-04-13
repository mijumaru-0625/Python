import pygame as pg

class Bullet:
    """ 弾 """
    def __init__(self, rect) -> None:
        x = rect.x + 17
        y = rect.y - 10
        self._image = pg.image.load("images/bullet.png")
        self._rect = self._image.get_rect()
        self._rect.topleft = (x, y)
        self._vy = -8
        self._is_alive = True

    @property
    def rect(self):
        return self._rect
    @rect.setter
    def rect(self, value):
        self._rect = value

    def update(self):
        """ 更新処理 """
        self._rect.y += self._vy
        if self._rect.y < -100:
            self._is_alive = False

    def draw(self, screen: pg.Surface):
        """ 描画処理 """
        screen.blit(self._image, self._rect)
