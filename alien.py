#胡小小Python学习之路
#外星人入侵小游戏
# alien.py
#控制外星人类
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #表示单个外星人的类
    def __init__(self, ai_settings, screen):
        #初始化外星人并设置其起始位置
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图片，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width #每个外星人的左边距都设置为外星人的宽度
        self.rect.y = self.rect.height #每个外星人的上边距都设置为外星人的高度

        #存储外星人的准确位置
        self.x = float(self.rect.x)

    #在指定位置绘制外星人
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_settings.alien_speed *
                    self.ai_settings.fleet_direction)
        #将外星人的移动量设置为外星人的速度和fleet_direction值的乘积
        #当fleet_direction值为1，则将外星人当前的x坐标增大alien_speed，实现外星人向右移动
        #当fleet_direction值为-1，则将外星人当前的x坐标减去alien_speed，实现了外星人向左移动

        self.rect.x = self.x

    #检查外星人是否撞到了屏幕边缘
    def check_edges(self):
        #如果外星人位于屏幕边缘就返回True
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            #如果外星人的rect的right属性大于或等于屏幕的rect的right属性
            #就说明外星人位于屏幕的右边缘
            return True
        elif self.rect.left <= 0:
            #如果外星人的rect的left属性小于或等于0
            #说明外星人位于屏幕的左边缘
            return True
