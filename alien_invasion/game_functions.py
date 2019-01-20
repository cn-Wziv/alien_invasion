import sys
import pygame
from bullet import Bullet

def check_keydown_event(event, ai_settings, screen, ship, bullets):
    # 响应文件
    if event.key == pygame.K_RIGHT:
        # 左键向左移动
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 右键向右移动
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 空格发射子弹
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹并加入bullets编组中，限制屏幕上出现的子弹数最多为3
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship,bullets):
    # 相应按键和鼠标时间
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 按键按下
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        # 按键抬起
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    # 更新屏幕上的图像，每次循环重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 绘制编组中所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 绘制飞船
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullet(bullets):
    # 更新子弹位置，并删除已小时的子弹
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
