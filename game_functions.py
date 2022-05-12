#胡小小Python学习之路
#外星人入侵小游戏
# game_functions.py
# 存储让游戏运行的函数
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
#从模块time中导入了函数sleep()，使用它来使游戏暂停

#响应按键函数
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        # 玩家按下右箭头键时标志设为true
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        # 玩家按下左箭头键时标志设为true
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        #添加游戏结束快捷键，玩家按下q键时游戏结束

#响应松开按键函数
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        # 玩家松开右箭头键时标志设为false
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        #玩家松开左箭头键时标志设为false

def check_events(ai_settings, screen, stats,sb, play_button, ship,aliens,bullets):  
    #在玩家按右箭头键时需要将飞船向右移动，所以给函数加上了形参ship
    #将之前写的监听键盘鼠标事件相关代码移到此处
    for event in pygame.event.get():
            #监视键盘和鼠标事件
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,ai_settings,screen,ship,bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings,screen,stats,sb, play_button,ship,aliens,bullets, mouse_x, mouse_y)

def check_play_button(ai_settings,screen,stats,sb, play_button,ship,aliens,bullets, mouse_x, mouse_y):
    #在玩家单击play按钮时开始新游戏
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #标志button_clicked的值为true或false，仅当玩家点击了play按钮
        #且游戏当前处于非活跃状态时，游戏才会重新开始

        #重置游戏设置
        ai_settings.initialize_dynamic_settings()
        #隐藏光标
        pygame.mouse.set_visible(False)
        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        #重置记分图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #清空现有外星人和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新外星人、让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    # 将更新屏幕的代码移到此处
    screen.fill(ai_settings.bg_color) #每次循环时都重新绘制屏幕
    # 重新绘制所有子弹
    for bullet in bullets.sprites(): #遍历编组中的所有子弹，对每个子弹都调用draw_bullet()
        bullet.draw_bullet()
    ship.blitme() # 每次循环时重新绘制飞船
    aliens.draw(screen) #在屏幕上绘制编组中的每个外星人
    sb.show_score() #显示得分
    #如果游戏处于非活动状态，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()
    #绘制完成其他元素后再绘制play按钮，按钮就会显示在最上层

    pygame.display.flip() #让绘制的屏幕可见

def update_bullets(ai_settings, screen,stats,sb, ship, aliens,bullets):
    bullets.update()
        # 向右移动已经设置完成，现在设置向左移动，逻辑一样
        #删除已经消失的子弹
    for bullet in bullets.copy():
        #在此循环中，不应从编组中直接删除子弹，所以必须遍历编组的副本
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #检查是否有子弹击中了外星人
    check_bullet_alien_collisions(ai_settings, screen,stats,sb, ship, aliens, bullets)
def fire_bullets(ai_settings, screen, ship, bullets):
    #发射子弹
    if len(bullets) < ai_settings.bullets_allowed:
            #创建一颗子弹
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet) #向编组中添加新子弹，用法类似列表
#检查子弹和外星人的碰撞
def check_bullet_alien_collisions(ai_settings, screen,stats,sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens) == 0:
        #删除现有的子弹并创建一群新外星人
        bullets.empty()
        #方法empty()可以删除编组中余下的精灵
        ai_settings.increase_speed()

        #提高玩家等级
        stats.level += 1
        sb.prep_level()
        
        create_fleet(ai_settings, screen, ship, aliens)


#创建外星人群
def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #创建外星人群
    for row_number in range(number_rows):
        #创建一行外星人
        for alien_number in range(number_aliens_x):
        #创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
#为创建多行外星人，使用了嵌套循环：内部循环创建一行外星人，外部循环创建多行外星人，循环次数为number_rows

def get_number_aliens_x(ai_settings, alien_width):
    # 计算一行可用于放置外星人的宽度
    available_space_x = ai_settings.screen_width - 2 * alien_width
    # 计算一行实际可放置外星人图片的个数
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
    aliens.add(alien)

#计算屏幕可容纳多少行外星人
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - (3*alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #对编组aliens调用方法update，可以自动对每一个外星人调用方法update
    #更新所有外星人的位置

    #检查外星人和飞船的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    #讲外星人下移并改变方向
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    #在外星人下移后，将fleet_direction的值修改为当前值与-1的乘积就可以改变外星人的移动方向

def ship_hit(ai_settings,screen, stats, sb, ship, aliens, bullets):
    #响应被外星人撞到的飞船
    #将ship_left减1
    if stats.ship_left > 0:
        stats.ship_left -= 1

    #更新记分牌
        sb.prep_ships()
    #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

    #创建一群新的外星人，并将飞船放到底部中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
    #稍后再添加center_ship方法在ship类中
    #暂停游戏
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        #如果ship_left<=0，即玩家没有飞船了
        #则标志量game_active设置为false,游戏结束

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #检查外星人是否撞到屏幕底端
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
        #当外星人rect的bottom属性值大于或等于屏幕rect的bottom属性值
        #表示外星人到达屏幕底端
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break

def check_high_score(stats, sb):
    #检查是否诞生了新的最高分
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()