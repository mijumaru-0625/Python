import pygame as pg
import gamecontrol

class ResultScene:
    """ 結果画面 """
    def __init__(self, game: gamecontrol.GemeManager):
        font = pg.font.Font(None, 50)
        self._game = game
        self._msg = font.render("Press SPACE to replay.", True, pg.Color("WHITE"))
        self._gameover = pg.image.load("images/gameover.png")
        self._gameclear = pg.image.load("images/gameclear.png")

    def update(self):
        """ 更新処理 """
        key = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self._game.reset()

    def draw(self, screen: pg.Surface):
        """ 描画処理 """
        screen.blit(self._msg, (120, 380))
        if self._game.is_playing == False:
            if self._game.is_cleared == True:
                screen.blit(self._gameclear, (50, 200))
            else:
                screen.blit(self._gameover, (50, 200))