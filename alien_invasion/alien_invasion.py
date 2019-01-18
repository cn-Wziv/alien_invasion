import pygame
from setting import Setting
from ship import Ship
import game_functions as gf

def run_game():

    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width,
                                      ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_setting, screen)

    while True:
        '''
        每次while循环都会绘制一个空屏幕并抹去旧屏幕
        游戏元素移动时将会不断重绘屏幕达到动态的效果
        '''
        # 监视键盘和鼠标
        gf.check_events(ship)
        # 飞船移动
        ship.update()
        # 设置背景颜色，让最近绘制的屏幕可见
        gf.update_screen(ai_setting, screen, ship)

run_game()