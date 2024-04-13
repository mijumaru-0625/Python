import pygame as pg
import random

class SoundManager:
    """ サウンドマネージャー """
    _instance = None

    @classmethod
    def get_instance(cls):
        """ 1 つだけのインスタンスを取得 """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self) -> None:
        pg.mixer.music.load("sounds/bgm.wav")
        self._over = pg.mixer.Sound("sounds/over.wav")
        self._clear = pg.mixer.Sound("sounds/clear.wav")
        self._clap1 = pg.mixer.Sound("sounds/clap1.wav")
        self._clap2 = pg.mixer.Sound("sounds/clap2.wav")
        self._clap3 = pg.mixer.Sound("sounds/clap3.wav")
        self._blast = pg.mixer.Sound("sounds/blast.wav")
        self._bomb = pg.mixer.Sound("sounds/bomb.wav")

    def bgmstart(self):
        """ BGM 再生 """
        pg.mixer.music.play(-1)

    def bgmstop(self):
        """ BGM 停止 """
        pg.mixer.music.stop()

    def playover(self):
        """ ゲームオーバー音 """
        self._over.play()

    def playerclear(self):
        """ ゲームクリア音 """
        self._clear.play()

    def playattack(self):
        """ 攻撃音 """
        r = random.randint(0, 3)
        if r == 0:
            self._clap1.play()
        elif r == 1:
            self._clap2.play()
        else:
            self._clap3.play()

    def playblast(self):
        """ 敵破壊音 """
        self._blast.play()

    def playbomb(self):
        """ 自機爆発音 """
        self._bomb.play()


