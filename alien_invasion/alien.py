import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''
    创建和管理外星人的类
    '''
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像并设置其rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 外星人的准确位置
        self.x = float(self.rect.x)


    def check_edges(self):
        # 若外星人到达左右边缘，返回True
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        # 向右移动外星人
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        # 在指定位置绘制外星人
        self.screen.blit(self.image, self.rect)