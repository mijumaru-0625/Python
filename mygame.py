# 1.準備
import pygame as pg, sys
import player

pg.init()
screen = pg.display.set_mode((600, 650))
pg.display.set_caption("MYGAME")
player = player.Player()

# 2.メインループ
while True:
    # 3.画面の初期化
    screen.fill(pg.Color("NAVY"))
    # 4.入力チェックや判断処理
    player.update()
    # 5.描画処理
    player.draw(screen)
    # 6.画面の表示
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンチェック
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()