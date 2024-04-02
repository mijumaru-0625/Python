import pygame as pg

class Player:
    """ 主人公 """
    def __init__(self) -> None:
        self._image = pg.image.load("images/kaeru1.png")
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

    def draw(self, screen):
        """ 描画処理 """
        screen.blit(self._image, self._rect)
