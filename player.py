import pygame as pg

class Player:
    """ 主人公 """
    def __init__(self) -> None:
        self.reset()

    @property
    def rect(self):
        return self._rect
    @rect.setter
    def rect(self, value):
        self._rect = value

    def reset(self):
        """ このキャラのリセット """
        self._images = [
            pg.image.load("images/kaeru1.png"),
            pg.image.load("images/kaeru2.png"),
            pg.image.load("images/kaeru3.png"),
            pg.image.load("images/kaeru4.png")
        ]
        self._cnt = 0
        self._image = self._images[0]
        self._rect = pg.Rect(250, 550, 50, 50)
        self._speed = 10

    def update(self):
        """ 更新処理 """
        key = pg.key.get_pressed()
        vx = 0
        if key[pg.K_RIGHT]:
            vx = self._speed
        if key[pg.K_LEFT]:
            vx = -self._speed
        if self._rect.x + vx < 0 or self._rect.x + vx > 550:
            vx = 0
        self._rect.x += vx
        self._cnt += 1
        self._image = self._images[self._cnt // 7 % 4]

    def draw(self, screen):
        """ 描画処理 """
        screen.blit(self._image, self._rect)
