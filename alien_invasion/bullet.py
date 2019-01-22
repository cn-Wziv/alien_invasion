import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''
    管理飞船发射的子弹的类, 子弹是一个画出来的矩形
    '''
    def __init__(self, ai_settings, screen, ship):
        # 在飞船所在位置创建一个子弹对象
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置(飞船矩形的上边缘的中心)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        # 颜色和速度
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # 子弹向上移动
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        # 在屏幕上绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)