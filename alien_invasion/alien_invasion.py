import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
def run_game():

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建用于存储有效外星人的编组
    aliens = Group()
    # 创建用于存储有效子弹的编组
    bullets = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        '''
        每次while循环都会绘制一个空屏幕并抹去旧屏幕
        游戏元素移动时将会不断重绘屏幕达到动态的效果
        '''
        # 监视键盘和鼠标
        gf.check_events(ai_settings, screen, ship, bullets)
        # 游戏状态为True时运行游戏
        if stats.game_active:
            # 飞船移动
            ship.update()
            # 子弹绘出和删除
            gf.update_bullet(ai_settings, screen, ship, bullets, aliens)
            # 外星人的移动
            gf.update_aliens(ai_settings, stats, screen, ship, aliens,bullets)
        # 设置背景颜色，让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()