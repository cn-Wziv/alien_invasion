import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    # 背景颜色
    bg_color = (230, 230, 230)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建用于存储有效子弹的编组
    bullets = Group()
    # 创建用于存储有效外星人的编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        # 监视键盘和鼠标
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        # 游戏状态为True时运行游戏
        if stats.game_active:
            # 飞船移动
            ship.update()
            # 子弹绘出和删除
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            # 外星人的移动
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
        # 设置背景颜色，让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)


run_game()