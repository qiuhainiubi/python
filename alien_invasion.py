#胡小小Python学习之路
#外星人入侵小游戏
# alien_invasion.py
import sys
# 模块sys用来退出游戏
import pygame
from settings import Setting
# 导入刚创建的设置类
from ship import Ship
# 导入管理飞船行为的类
import game_functions as gf
from pygame.sprite import Group
#Group类类似于列表
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init() #初始化屏幕对象
    ai_settings = Setting() 
    # 创建Setting类的实例，并存储在ai_settings变量中
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #创建显示窗口
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings,screen,"Play")#创建play按钮
    stats = GameStats(ai_settings)
    #创建储存游戏统计信息的实例
    sb = Scoreboard(ai_settings, screen, stats)
    #绘制一艘飞船
    ship = Ship(ai_settings,screen)
    bullets = Group() #创建一个存储子弹的编组
    aliens = Group() #创建一个外星人编组
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats,sb, play_button, ship,aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        
        gf.update_screen(ai_settings,screen,stats,sb,ship, aliens, bullets,play_button)
run_game()

