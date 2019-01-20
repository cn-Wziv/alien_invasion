import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_event(event, ai_settings, screen, ship, bullets):
    # 响应文件
    if event.key == pygame.K_RIGHT:
        # 左键向左移动
        ship.moving_right = True
    elif event.key == pygame.K_q:
        # 按Q快捷键关闭游戏
        sys.exit()
    elif event.key == pygame.K_LEFT:
        # 右键向右移动
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 空格发射子弹
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹并加入bullets编组中，限制屏幕上出现的子弹数最多为3
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


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


def get_number_aliens_x(ai_settings, alien_width):
    # 计算每行可容纳的外星人数
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    # 计算屏幕可容纳多少行外星人
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)

    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建多行外星人
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height = 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    # 创建一批外星人
    # 创建一个外星人并计算一行可以容纳多少外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建一批外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    # 更新屏幕上的图像，每次循环重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 绘制编组中所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 绘制飞船
    ship.blitme()
    # 绘制外星人
    aliens.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullet(ai_settings, screen, ship, bullets, aliens):
    # 更新子弹位置
    bullets.update()
    # 更新子弹位置，并删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collosion(ai_settings, screen,ship, aliens, bullets)


def check_bullet_alien_collosion(ai_settings, screen, ship, aliens, bullets):
    # 响应子弹和外星人的碰撞

    # 遍历bullets和aliens中的所有对象，将发生碰撞的都删除掉
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 子弹向上飞
    if len(aliens) == 0:
        # 删除现有子弹并创建一匹新的外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def check_fleet_edges(ai_settings, aliens):
    # 当外形人移动到左右边缘
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    '''
    响应被外星人撞到的飞船
    '''
    # 将ships_left减1，机会用光后游戏状态设为False
    if stats.ships_left > 0:
        stats.ships_left -= 1
    else:
        stats.game_active = False

    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()

    # 创建一组新的外星人，并将飞船放到屏幕底端中央
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # 暂停
    sleep(0.5)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    '''
    检查是否有外星人到达屏幕底端
    '''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 与飞船被外星人撞到做相同处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings,stats, screen, ship, aliens, bullets):
    # 检测外星人是否到达左右边缘更新所有外星人的位置
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
        print("飞船死亡一次")

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
