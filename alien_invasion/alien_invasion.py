import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建用于存储有效子弹的编组
    bullets = Group()

    while True:
        '''
        每次while循环都会绘制一个空屏幕并抹去旧屏幕
        游戏元素移动时将会不断重绘屏幕达到动态的效果
        '''
        # 监视键盘和鼠标
        gf.check_events(ai_settings, screen, ship, bullets)
        # 飞船移动
        ship.update()
        # 子弹绘出和删除
        gf.update_bullet(bullets)
        # 设置背景颜色，让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()