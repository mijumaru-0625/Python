import pygame as pg
import player, enemy, bullet, status, sound

class Subject:
    """ 配信者の基本形 """
    def __init__(self) -> None:
        self._observers: list[status.Observer] = []

    def attach(self, observer):
        """ 受信者の追加 """
        self._observers.append(observer)

    def notify(self, ntype):
        """ 通知 """
        for observer in self._observers:
            observer.update(ntype)

class GemeManager(Subject):
    """ ゲーム管理 """
    def __init__(self) -> None:
        super().__init__()
        self._player = player.Player()
        self._enemies: list[enemy.Enemy] = []
        self._effects: list[enemy.BombEffect] = []
        self._bullets: list[bullet.Bullet] = []
        self._factory = enemy.EnemyFactory()
        self._status = status.Status()
        self.attach(self._status)
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
        self._spawn_count = 0
        self._bullets.clear()
        self._bullet_count = 0
        self._status.reset()
        sound.SoundManager.get_instance().bgmstart()

    def update(self):
        """ 更新処理 """
        self.notify("distance")
        self._bullet_count += 1
        if self._bullet_count > 10: # 弾発生のカウンタが条件を満たした
            key = pg.key.get_pressed()
            if key[pg.K_a]: # A キーで弾発射
                self._bullets.append(bullet.Bullet(self._player.rect))
                self._bullet_count = 0
        for e in self._effects:
            e.update()
        for b in self._bullets:
            b.update()

        self._player.update()
        self._spawn_count += 1
        if self._spawn_count > 15: # 敵発生のカウンタが条件を満たした
            self._spawn_count = 0
            self._enemies.append(self._factory.random_create())

        for e in self._enemies:
            for b in self._bullets:
                if e.rect.colliderect(b.rect):
                    sound.SoundManager.get_instance().playattack()
                    #self._bullets.remove(b)
                    b.hit_enemy()
                    e.hp -= 50
                    if e.hp <= 0:
                        self.notify("score")
                        b = enemy.BombEffect(e.rect, self._effects)
                        sound.SoundManager.get_instance().playblast()
                        self._effects.append(b)
                        #self._enemies.remove(e)
                        e.clear()
                        if self._status.score == 30: # クリア条件
                            self._is_playing = False
                            self._is_cleared = True
                            sound.SoundManager.get_instance().bgmstop()
                            sound.SoundManager.get_instance().playerclear()
            # if e.is_alive == False:
            #     self._enemies.remove(e)
            #     break
            e.update()
                
            # 敵と主人公が接触したらダメージ
            if e in self._enemies:
                if e.rect.colliderect(self._player.rect):
                    sound.SoundManager.get_instance().playbomb()
                    #self._enemies.remove(e)
                    e.clear()
                    self._player.damage()
                    self._player.hp -= 50
                    if self._player.hp <= 0:
                        self._is_playing = False
                        sound.SoundManager.get_instance().bgmstop()
                        sound.SoundManager.get_instance().playover()

        # リストの更新
        self._bullets = [b for b in self._bullets if b.is_alive]
        self._enemies = [e for e in self._enemies if e.is_alive]

    def draw(self, screen):
        """ 描画処理 """
        for b in self._bullets:
            b.draw(screen)
        for e in self._effects:
            e.draw(screen)
        self._player.draw(screen)
        for e in self._enemies:
            e.draw(screen)
        self._status.draw(screen)