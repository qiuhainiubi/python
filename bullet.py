#外星人入侵小游戏
# bullet.py
#管理子弹类
import pygame
from pygame.sprite import Sprite 
# 从模块pygame.sprite中导入Sprite类。
# 通过使用精灵类，可将游戏中相关的元素编组，进而可以同时操作编组中的元素。
class Bullet(Sprite):

    #创建子弹对象
    def __init__(self,ai_settings,screen,ship):
        super().__init__() #继承Sprite类
        self.screen = screen
        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top #实现效果为子弹从飞船顶部射出
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed
    
    # 管理子弹位置
    def update(self):
        self.y -= self.speed #坐标y不断减少可实现向上移动子弹
        self.rect.y = self.y #更新表示子弹的rect的位置

    #屏幕上绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


