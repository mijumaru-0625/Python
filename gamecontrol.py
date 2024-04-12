import pygame as pg
import random, player, enemy

class GemeManager:
    """ ゲーム管理 """
    def __init__(self) -> None:
        self._player = player.Player()
        self._enemies: list[enemy.Enemy] = []
        self.reset()

    @property
    def is_playing(self):
        return self._is_playing
    
    @property
    def is_cleared(self):
        return self._is_cleared

    def reset(self):
        """ ゲームのリセット """
        self._is_playing = True
        self._is_cleared = False
        self._player.reset()
        self._enemies.clear()
        for i in range(8):
            self._enemies.append(enemy.Enemy())


    def update(self):
        """ 更新処理 """
        self._player.update()
        for e in self._enemies:
            e.update()
            # 敵が下に落ちたら停止
            if e.rect.y >= 580:
                self._is_playing = False
            # 敵と主人公が接触したら、敵を上に移動
            if e.rect.colliderect(self._player.rect):
                e.rect.y = self._player.rect.y - 70
                e.vy = -abs(e.vy)
                e.hp -= 50
                if e.hp <= 0:
                    self._enemies.remove(e)
                    if len(self._enemies) == 0:
                        self._is_playing = False
                        self._is_cleared = True
                    return # おそらく for ループがおかしくなるんだろう

    def draw(self, screen):
        """ 描画処理 """
        self._player.draw(screen)
        for e in self._enemies:
            e.draw(screen)