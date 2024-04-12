import pygame as pg
import player, enemy

class GemeManager:
    """ ゲーム管理 """
    def __init__(self) -> None:
        self._player = player.Player()
        self._enemies: list[enemy.Enemy] = []
        self._effects: list[enemy.BombEffect] = []
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
        for i in range(2):
            self._enemies.append(enemy.Enemy())
        for i in range(1):
            self._enemies.append(enemy.FlameEnemy())
        for i in range(1):
            self._enemies.append(enemy.IceEnemy())

    def update(self):
        """ 更新処理 """
        for e in self._effects:
            e.update()
        self._player.update()
        for e in self._enemies:
            e.update()
            # 敵が下に落ちたら停止
            if e.rect.y >= 580:
                self._is_playing = False
            # 敵と主人公が接触したら、敵を上に移動
            if e.rect.colliderect(self._player.rect):
                self._player.damage()
                e.rect.y = self._player.rect.y - 70
                e.vy = -abs(e.vy)
                e.hp -= 50
                if e.hp <= 0:
                    b = enemy.BombEffect(e.rect, self._effects)
                    self._effects.append(b)
                    self._enemies.remove(e)
                    return # おそらく for ループがおかしくなるんだろう

        if len(self._enemies + self._effects) == 0: # クリア画面に移行する
            self._is_playing = False
            self._is_cleared = True

    def draw(self, screen):
        """ 描画処理 """
        for e in self._effects:
            e.draw(screen)
        self._player.draw(screen)
        for e in self._enemies:
            e.draw(screen)